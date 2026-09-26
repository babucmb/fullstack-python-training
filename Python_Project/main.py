"""A small Streamlit application for managing colleges, students, and teachers."""

from dataclasses import dataclass, field

import streamlit as st


st.set_page_config(page_title="University Management System", layout="wide")


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
    """Return a college by name, ignoring case and surrounding whitespace."""
    wanted_name = name.strip().casefold()
    return next(
        (college for college in st.session_state.colleges
         if college.name.casefold() == wanted_name),
        None,
    )


def college_names() -> list[str]:
    return [college.name for college in st.session_state.colleges]


if "colleges" not in st.session_state:
    st.session_state.colleges = []

st.title("University Management System")
st.caption("Create colleges, then add and view their students and teachers.")

menu_choice = st.sidebar.radio(
    "Select an option",
    ("Create College", "Add Student", "Add Teacher", "Display Students",
     "Display Teachers", "List Colleges"),
)

if menu_choice == "Create College":
    with st.form("create_college_form", clear_on_submit=True):
        name = st.text_input("College name")
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
    if not st.session_state.colleges:
        st.info("Create a college before adding students.")
    else:
        with st.form("add_student_form", clear_on_submit=True):
            college_name = st.selectbox("College", college_names())
            roll_no = st.number_input("Roll number", min_value=1, step=1)
            student_name = st.text_input("Student name")
            branch = st.text_input("Branch")
            submitted = st.form_submit_button("Add student")

        if submitted:
            student_name, branch = student_name.strip(), branch.strip()
            selected_college = find_college(college_name)
            if not student_name or not branch:
                st.error("Enter both the student name and branch.")
            elif any(student.roll_no == roll_no for student in selected_college.students):
                st.error("That roll number already exists in this college.")
            else:
                selected_college.students.append(Student(student_name, branch, int(roll_no)))
                st.success("Student added successfully.")

elif menu_choice == "Add Teacher":
    if not st.session_state.colleges:
        st.info("Create a college before adding teachers.")
    else:
        with st.form("add_teacher_form", clear_on_submit=True):
            college_name = st.selectbox("College", college_names())
            teacher_name = st.text_input("Teacher name")
            branch = st.text_input("Branch")
            subject = st.text_input("Subject")
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
    if not st.session_state.colleges:
        st.info("No colleges have been created yet.")
    else:
        college_name = st.selectbox("College", college_names())
        selected_college = find_college(college_name)
        st.subheader(f"Students at {selected_college.name}")
        if selected_college.students:
            st.dataframe(
                [{"Roll no.": student.roll_no, "Name": student.name, "Branch": student.branch}
                 for student in selected_college.students],
                hide_index=True,
                use_container_width=True,
            )
        else:
            st.warning("No students found for this college.")

elif menu_choice == "Display Teachers":
    if not st.session_state.colleges:
        st.info("No colleges have been created yet.")
    else:
        college_name = st.selectbox("College", college_names())
        selected_college = find_college(college_name)
        st.subheader(f"Teachers at {selected_college.name}")
        if selected_college.teachers:
            st.dataframe(
                [{"Name": teacher.name, "Branch": teacher.branch, "Subject": teacher.subject}
                 for teacher in selected_college.teachers],
                hide_index=True,
                use_container_width=True,
            )
        else:
            st.warning("No teachers found for this college.")

elif menu_choice == "List Colleges":
    st.subheader("Colleges")
    if not st.session_state.colleges:
        st.info("No colleges have been created yet.")
    else:
        st.dataframe(
            [{"College": college.name, "Students": len(college.students),
              "Teachers": len(college.teachers)}
             for college in st.session_state.colleges],
            hide_index=True,
            use_container_width=True,
        )
