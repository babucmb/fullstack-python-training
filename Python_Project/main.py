"""A modern Streamlit university management dashboard."""

from dataclasses import dataclass, field

import streamlit as st


st.set_page_config(
    page_title="CampusFlow | University Management",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@500;600;700&display=swap');

        .stApp { background: #f6f8fc; color: #172033; font-family: 'DM Sans', sans-serif; }
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { padding: 2.2rem 3.1rem 3rem; max-width: 1440px; }
        [data-testid="stSidebar"] { background: #121b31; }
        [data-testid="stSidebar"] * { color: #eaf0ff; }
        [data-testid="stSidebar"] .stRadio label { border-radius: 9px; padding: .32rem .42rem; }
        [data-testid="stSidebar"] .stRadio label:hover { background: #24355c; }
        .brand { font-family: 'Outfit', sans-serif; font-size: 1.7rem; font-weight: 700; color: #ffffff; margin: .55rem 0 .15rem; }
        .brand span { color: #7dd3fc; }
        .brand-tagline { font-size: .78rem; color: #a8b6d3; margin-bottom: 2.3rem; }
        .eyebrow { color: #4f6df5; font-size: .76rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; margin-bottom: .35rem; }
        h1, h2, h3 { font-family: 'Outfit', sans-serif !important; color: #172033 !important; }
        h1 { font-size: 2.1rem !important; margin: 0 !important; }
        h2 { font-size: 1.35rem !important; padding-top: .8rem; }
        .hero-copy { color: #6a758b; font-size: 1rem; margin: .35rem 0 1.7rem; }
        .metric-card { background: #ffffff; border: 1px solid #e7ebf3; border-radius: 14px; padding: 1.05rem 1.2rem; box-shadow: 0 4px 15px rgba(27, 39, 71, .04); }
        .metric-label { color: #778197; font-size: .8rem; font-weight: 600; }
        .metric-value { color: #18233e; font-family: 'Outfit', sans-serif; font-size: 1.65rem; font-weight: 700; margin-top: .1rem; }
        .metric-icon { float: right; background: #eef2ff; border-radius: 9px; font-size: 1.05rem; padding: .35rem .5rem; }
        div[data-testid="stForm"] { background: #ffffff; border: 1px solid #e6ebf3; border-radius: 14px; padding: 1.3rem 1.45rem .55rem; box-shadow: 0 5px 18px rgba(25, 38, 70, .04); }
        div[data-testid="stForm"] > div:first-child { color: #18233e; }
        .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] > div { border-radius: 8px !important; border-color: #dbe2ee !important; }
        .stButton > button, .stFormSubmitButton > button { background: #4f6df5 !important; color: #ffffff !important; border: 0 !important; border-radius: 8px !important; font-weight: 700 !important; padding: .48rem 1rem !important; }
        .stButton > button:hover, .stFormSubmitButton > button:hover { background: #3f5be0 !important; }
        [data-testid="stDataFrame"] { border: 1px solid #e6ebf3; border-radius: 12px; overflow: hidden; }
        .section-note { color: #778197; margin-top: -.4rem; margin-bottom: 1rem; }
        .empty-card { background: #ffffff; border: 1px dashed #ccd6e8; border-radius: 14px; color: #66738d; padding: 1.5rem; text-align: center; }
        @media (max-width: 700px) { .block-container { padding: 1.3rem 1rem 2rem; } }
    </style>
    """,
    unsafe_allow_html=True,
)


@dataclass
class Person:
    name: str
    branch: str


@dataclass
class Student(Person):
    roll_no: int


@dataclass
class Teacher(Person):
    subject: str


@dataclass
class College:
    name: str
    students: list[Student] = field(default_factory=list)
    teachers: list[Teacher] = field(default_factory=list)


def find_college(name: str) -> College | None:
    """Return the matching college, ignoring letter case and extra spaces."""
    wanted_name = name.strip().casefold()
    return next((item for item in st.session_state.colleges if item.name.casefold() == wanted_name), None)


def college_names() -> list[str]:
    return [item.name for item in st.session_state.colleges]


def totals() -> tuple[int, int, int]:
    colleges = st.session_state.colleges
    return len(colleges), sum(len(item.students) for item in colleges), sum(len(item.teachers) for item in colleges)


def page_heading(title: str, description: str) -> None:
    st.markdown(f'<div class="eyebrow">Campus administration</div><h1>{title}</h1><p class="hero-copy">{description}</p>', unsafe_allow_html=True)


def empty_message(message: str) -> None:
    st.markdown(f'<div class="empty-card">{message}</div>', unsafe_allow_html=True)


if "colleges" not in st.session_state:
    st.session_state.colleges = []

with st.sidebar:
    st.markdown('<div class="brand">Campus<span>Flow</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-tagline">UNIVERSITY MANAGEMENT</div>', unsafe_allow_html=True)
    menu_choice = st.radio(
        "Navigation",
        ("Overview", "Create College", "Add Student", "Add Teacher", "Display Students", "Display Teachers", "List Colleges"),
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption("Manage your campus data in one place.")

college_count, student_count, teacher_count = totals()

if menu_choice == "Overview":
    page_heading("Welcome back 👋", "Here is a live snapshot of your university directory.")
    metric_columns = st.columns(3)
    metric_data = [("🏛️", "Colleges", college_count), ("🎒", "Students", student_count), ("👩‍🏫", "Teachers", teacher_count)]
    for column, (icon, label, value) in zip(metric_columns, metric_data):
        column.markdown(f'<div class="metric-card"><span class="metric-icon">{icon}</span><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Get started")
    if not college_count:
        empty_message("🏛️ Create your first college from the sidebar to start building your directory.")
    else:
        st.info("Use the sidebar to add people, explore each college, or view the complete directory.")

elif menu_choice == "Create College":
    page_heading("Create a college", "Add a college to begin organising its students and teaching staff.")
    with st.form("create_college_form", clear_on_submit=True):
        name = st.text_input("College name", placeholder="e.g. Greenfield Institute of Technology")
        submitted = st.form_submit_button("Create college")
    if submitted:
        name = name.strip()
        if not name:
            st.error("Enter a college name.")
        elif find_college(name):
            st.error("A college with that name already exists.")
        else:
            st.session_state.colleges.append(College(name=name))
            st.success(f"{name} was created successfully.")

elif menu_choice == "Add Student":
    page_heading("Add a student", "Register a student under the correct college and branch.")
    if not college_count:
        empty_message("🏛️ Create a college first, then you can add students here.")
    else:
        with st.form("add_student_form", clear_on_submit=True):
            college_name = st.selectbox("College", college_names())
            left, right = st.columns(2)
            with left:
                student_name = st.text_input("Student name", placeholder="Full name")
                roll_no = st.number_input("Roll number", min_value=1, step=1)
            with right:
                branch = st.text_input("Branch", placeholder="e.g. Computer Science")
            submitted = st.form_submit_button("Add student")
        if submitted:
            student_name, branch = student_name.strip(), branch.strip()
            selected_college = find_college(college_name)
            if not student_name or not branch:
                st.error("Enter both the student name and branch.")
            elif any(item.roll_no == roll_no for item in selected_college.students):
                st.error("That roll number already exists in this college.")
            else:
                selected_college.students.append(Student(student_name, branch, int(roll_no)))
                st.success("Student added successfully.")

elif menu_choice == "Add Teacher":
    page_heading("Add a teacher", "Register a faculty member and their teaching details.")
    if not college_count:
        empty_message("🏛️ Create a college first, then you can add teachers here.")
    else:
        with st.form("add_teacher_form", clear_on_submit=True):
            college_name = st.selectbox("College", college_names())
            left, right = st.columns(2)
            with left:
                teacher_name = st.text_input("Teacher name", placeholder="Full name")
                branch = st.text_input("Branch", placeholder="e.g. Electronics")
            with right:
                subject = st.text_input("Subject", placeholder="e.g. Data Structures")
            submitted = st.form_submit_button("Add teacher")
        if submitted:
            teacher_name, branch, subject = teacher_name.strip(), branch.strip(), subject.strip()
            selected_college = find_college(college_name)
            if not teacher_name or not branch or not subject:
                st.error("Enter the teacher name, branch, and subject.")
            else:
                selected_college.teachers.append(Teacher(teacher_name, branch, subject))
                st.success("Teacher added successfully.")

elif menu_choice == "Display Students":
    page_heading("Student directory", "Browse every student registered in a selected college.")
    if not college_count:
        empty_message("No colleges have been created yet.")
    else:
        college_name = st.selectbox("Choose a college", college_names())
        selected_college = find_college(college_name)
        st.subheader(selected_college.name)
        st.markdown(f'<p class="section-note">{len(selected_college.students)} student(s) registered</p>', unsafe_allow_html=True)
        if selected_college.students:
            st.dataframe([{"Roll no.": item.roll_no, "Name": item.name, "Branch": item.branch} for item in selected_college.students], hide_index=True, use_container_width=True)
        else:
            empty_message("🎒 No students have been registered for this college yet.")

elif menu_choice == "Display Teachers":
    page_heading("Faculty directory", "Browse teaching staff and their subjects for a selected college.")
    if not college_count:
        empty_message("No colleges have been created yet.")
    else:
        college_name = st.selectbox("Choose a college", college_names())
        selected_college = find_college(college_name)
        st.subheader(selected_college.name)
        st.markdown(f'<p class="section-note">{len(selected_college.teachers)} teacher(s) registered</p>', unsafe_allow_html=True)
        if selected_college.teachers:
            st.dataframe([{"Name": item.name, "Branch": item.branch, "Subject": item.subject} for item in selected_college.teachers], hide_index=True, use_container_width=True)
        else:
            empty_message("👩‍🏫 No teachers have been registered for this college yet.")

elif menu_choice == "List Colleges":
    page_heading("College directory", "See a complete view of every college and its registered people.")
    if not college_count:
        empty_message("🏛️ No colleges have been created yet.")
    else:
        st.dataframe([{"College": item.name, "Students": len(item.students), "Teachers": len(item.teachers)} for item in st.session_state.colleges], hide_index=True, use_container_width=True)
