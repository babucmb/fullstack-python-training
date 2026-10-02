# 🌐 APIs, REST API & Flask API's

A complete learning guide covering **APIs, HTTP, REST APIs, JSON, CRUD operations, HTTP methods, status codes, request/response structure, authentication, and building REST APIs using Flask**.

---

## 📚 Table of Contents

1. [What is an API?](#-what-is-an-api)
2. [Why Do We Need APIs?](#-why-do-we-need-apis)
3. [Real-World API Example](#-real-world-api-example)
4. [Client and Server](#-client-and-server)
5. [What is HTTP?](#-what-is-http)
6. [HTTP Request and Response](#-http-request-and-response)
7. [Parts of an HTTP Request](#-parts-of-an-http-request)
8. [Parts of an HTTP Response](#-parts-of-an-http-response)
9. [What is REST?](#-what-is-rest)
10. [What is a REST API?](#-what-is-a-rest-api)
11. [API vs REST API](#-api-vs-rest-api)
12. [HTTP Methods](#-http-methods)
13. [CRUD Operations](#-crud-operations)
14. [HTTP Status Codes](#-http-status-codes)
15. [JSON](#-json)
16. [Path Parameters](#-path-parameters)
17. [Query Parameters](#-query-parameters)
18. [Request Body](#-request-body)
19. [HTTP Headers](#-http-headers)
20. [Content-Type](#-content-type)
21. [Authentication](#-authentication)
22. [API Endpoint](#-api-endpoint)
23. [Flask](#-flask)
24. [Creating a Simple Flask API](#-creating-a-simple-flask-api)
25. [GET API in Flask](#-get-api-in-flask)
26. [Query Parameters in Flask](#-query-parameters-in-flask)
27. [Path Parameters in Flask](#-path-parameters-in-flask)
28. [POST API in Flask](#-post-api-in-flask)
29. [PUT API in Flask](#-put-api-in-flask)
30. [PATCH API in Flask](#-patch-api-in-flask)
31. [DELETE API in Flask](#-delete-api-in-flask)
32. [Complete CRUD Flask API](#-complete-crud-flask-api)
33. [Calling an API Using Python](#-calling-an-api-using-python)
34. [API Testing Tools](#-api-testing-tools)
35. [Common API Errors](#-common-api-errors)
36. [API Security Basics](#-api-security-basics)
37. [REST API Best Practices](#-rest-api-best-practices)
38. [Flask Project Structure](#-flask-project-structure)
39. [Learning Roadmap](#-learning-roadmap)
40. [Interview Questions](#-interview-questions)
41. [Practice Tasks](#-practice-tasks)
42. [Key Takeaways](#-key-takeaways)

---

# 🔹 What is an API?

**API** stands for **Application Programming Interface**.

An API is a way for two different software applications to communicate with each other.

In simple words:

> **API acts as a bridge between two applications.**

For example:

```text
Frontend
   |
   | API Request
   ↓
Backend / Server
   |
   | Database
   ↓
Database
```

The frontend does not usually communicate directly with the database.

Instead:

```text
Frontend → API → Backend → Database
```

The backend processes the request and sends a response back through the API.

---

# 🔹 Why Do We Need APIs?

APIs allow different applications and services to communicate.

For example:

### Food Delivery Application

```text
Mobile App
    ↓
Restaurant API
    ↓
Restaurant Database
```

The application can use APIs to:

* Get restaurants
* Get food items
* Create orders
* Update orders
* Cancel orders
* Track orders
* Process payments

---

# 🔹 Real-World API Example

Suppose a weather application wants to display the current temperature.

The weather application can request:

```http
GET /weather?city=Hyderabad
```

The server may respond:

```json
{
    "city": "Hyderabad",
    "temperature": 29,
    "unit": "C"
}
```

The application receives this data and displays:

```text
Hyderabad
29°C
```

The application does not need to know how the weather service stores or calculates its data.

It only needs to know how to communicate with the API.

---

# 🔹 Client and Server

Most APIs follow a client-server communication model.

### Client

The client sends requests.

Examples:

* Web browser
* Mobile application
* React application
* Python program
* Postman
* Another server

### Server

The server receives requests, processes them, and returns responses.

Example:

```text
Client
  |
  | Request
  ↓
Server
  |
  | Process
  ↓
Database
  |
  | Data
  ↓
Server
  |
  | Response
  ↓
Client
```

---

# 🔹 What is HTTP?

**HTTP** stands for:

> HyperText Transfer Protocol

HTTP is a communication protocol used for transferring information between clients and servers.

Example:

```text
Client → HTTP Request → Server
Client ← HTTP Response ← Server
```

HTTP is commonly used by APIs.

---

# 🔹 HTTP Request and Response

Every API communication generally involves:

```text
REQUEST
   ↓
SERVER
   ↓
RESPONSE
```

Example request:

```http
GET /users/10
```

Example response:

```json
{
    "id": 10,
    "name": "Mahesh"
}
```

---

# 🔹 Parts of an HTTP Request

An HTTP request can contain:

```text
Method
URL
Headers
Body
```

Example:

```http
POST /users HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "name": "Mahesh",
    "age": 22
}
```

Here:

```text
POST                    → Method
/users                  → Path
Content-Type            → Header
JSON object             → Request Body
```

---

# 🔹 Parts of an HTTP Response

A response can contain:

```text
Status Code
Headers
Body
```

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "User found"
}
```

Here:

```text
200                     → Status Code
Content-Type            → Header
JSON                    → Response Body
```

---

# 🔹 What is REST?

**REST** stands for:

> Representational State Transfer

REST is an architectural style used for designing web APIs.

REST APIs commonly use:

* HTTP
* Resources
* URLs
* HTTP methods
* JSON
* Stateless communication

Example resource:

```text
/users
/products
/orders
/employees
```

---

# 🔹 What is a REST API?

A **REST API** is an API designed according to REST principles and usually communicates over HTTP.

Example:

```text
GET     /users
GET     /users/10
POST    /users
PUT     /users/10
PATCH   /users/10
DELETE  /users/10
```

The URL represents the resource.

The HTTP method represents the operation.

---

# 🔹 API vs REST API

| API                             | REST API                     |
| ------------------------------- | ---------------------------- |
| General concept                 | Specific architectural style |
| Can use different protocols     | Usually uses HTTP            |
| Can have different formats      | Commonly uses JSON           |
| Can be SOAP, GraphQL, RPC, etc. | Follows REST principles      |
| Broader term                    | Specific type of API         |

Therefore:

```text
REST API ⊂ API
```

REST API is one type of API.

---

# 🔹 HTTP Methods

HTTP methods tell the server what operation the client wants to perform.

| Method  | Purpose                                      |
| ------- | -------------------------------------------- |
| GET     | Retrieve data                                |
| POST    | Create/submit data                           |
| PUT     | Replace/update a resource                    |
| PATCH   | Partially update a resource                  |
| DELETE  | Delete a resource                            |
| HEAD    | Retrieve headers without response body       |
| OPTIONS | Ask what communication options are supported |

---

## GET

Used to retrieve data.

Example:

```http
GET /users
```

Response:

```json
[
    {
        "id": 1,
        "name": "Mahesh"
    },
    {
        "id": 2,
        "name": "Rahul"
    }
]
```

---

## POST

Used to send data to the server, commonly to create a new resource.

Example:

```http
POST /users
```

Body:

```json
{
    "name": "Mahesh",
    "age": 22
}
```

---

## PUT

Used to replace/update a resource.

Example:

```http
PUT /users/1
```

Body:

```json
{
    "name": "Mahesh Babu",
    "age": 23
}
```

PUT generally represents replacement of the target resource.

---

## PATCH

Used for partial updates.

Example:

```http
PATCH /users/1
```

Body:

```json
{
    "age": 23
}
```

Only the required field is changed.

---

## DELETE

Used to delete a resource.

Example:

```http
DELETE /users/1
```

---

# 🔹 CRUD Operations

CRUD stands for:

```text
C → Create
R → Read
U → Update
D → Delete
```

Mapping CRUD to HTTP:

| CRUD   | HTTP Method |
| ------ | ----------- |
| Create | POST        |
| Read   | GET         |
| Update | PUT / PATCH |
| Delete | DELETE      |

Example:

```text
POST   /users
GET    /users
GET    /users/1
PUT    /users/1
PATCH  /users/1
DELETE /users/1
```

---

# 🔹 HTTP Status Codes

Status codes tell the client what happened with the request.

They are divided into five major classes:

```text
1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client Error
5xx → Server Error
```

---

## Common 2xx Status Codes

### 200 OK

Request was successful.

```http
200 OK
```

Commonly used for successful GET requests.

---

### 201 Created

A new resource was successfully created.

```http
201 Created
```

Commonly used after POST.

---

### 202 Accepted

Request has been accepted for processing, but processing may not yet be complete.

```http
202 Accepted
```

---

### 204 No Content

Request was successful but there is no response body.

Often used after successful DELETE or update operations.

---

# 🔹 Common 4xx Status Codes

### 400 Bad Request

The request is invalid.

```http
400 Bad Request
```

Example:

```json
{
    "error": "Invalid input"
}
```

---

### 401 Unauthorized

Authentication is required or authentication credentials are invalid.

```http
401 Unauthorized
```

---

### 403 Forbidden

The client is authenticated but does not have permission.

```http
403 Forbidden
```

---

### 404 Not Found

Requested resource does not exist.

```http
404 Not Found
```

Example:

```http
GET /users/9999
```

if user `9999` doesn't exist.

---

### 405 Method Not Allowed

The HTTP method is not supported for that endpoint.

Example:

```http
POST /users/1
```

when that endpoint only allows GET.

---

# 🔹 Common 5xx Status Codes

### 500 Internal Server Error

Something went wrong on the server.

```http
500 Internal Server Error
```

---

### 502 Bad Gateway

A server acting as a gateway/proxy received an invalid response from another server.

---

### 503 Service Unavailable

The server is temporarily unavailable.

---

# 🔹 JSON

**JSON** stands for:

> JavaScript Object Notation

JSON is one of the most commonly used formats for API communication.

Example:

```json
{
    "name": "Mahesh",
    "age": 22,
    "skills": [
        "Python",
        "SQL",
        "Machine Learning"
    ]
}
```

---

## JSON Data Types

JSON supports:

```text
String
Number
Boolean
Array
Object
Null
```

Example:

```json
{
    "name": "Mahesh",
    "age": 22,
    "student": true,
    "skills": ["Python", "SQL"],
    "address": null
}
```

---

# 🔹 Python Dictionary vs JSON

Python:

```python
data = {
    "name": "Mahesh",
    "age": 22
}
```

JSON:

```json
{
    "name": "Mahesh",
    "age": 22
}
```

They look similar, but they are different formats/types.

Python can convert between Python objects and JSON using the `json` module.

---

# 🔹 Path Parameters

A path parameter is part of the URL path.

Example:

```text
/users/10
```

Here:

```text
10
```

is the user ID.

Example:

```text
GET /users/<id>
```

Possible requests:

```text
/users/1
/users/2
/users/100
```

---

# 🔹 Query Parameters

Query parameters appear after `?` in the URL.

Example:

```text
/users?city=Hyderabad
```

Here:

```text
city=Hyderabad
```

is a query parameter.

Multiple query parameters:

```text
/users?city=Hyderabad&age=22
```

Common use cases:

* Filtering
* Searching
* Sorting
* Pagination

Example:

```text
/products?category=laptop
```

```text
/products?category=laptop&page=2
```

---

# 🔹 Path Parameter vs Query Parameter

| Path Parameter                  | Query Parameter            |
| ------------------------------- | -------------------------- |
| `/users/10`                     | `/users?id=10`             |
| Identifies a resource           | Filters/customizes request |
| Usually required for that route | Often optional             |
| Part of path                    | Comes after `?`            |

Example:

```text
/users/10
```

means:

> Get user 10.

Whereas:

```text
/users?city=Hyderabad
```

means:

> Get users filtered by Hyderabad.

---

# 🔹 Request Body

The request body contains data sent to the server.

Commonly used with:

```text
POST
PUT
PATCH
```

Example:

```http
POST /users
```

Body:

```json
{
    "name": "Mahesh",
    "email": "mahesh@example.com",
    "age": 22
}
```

---

# 🔹 HTTP Headers

Headers provide additional information about a request or response.

Example:

```http
Content-Type: application/json
Authorization: Bearer TOKEN
Accept: application/json
```

Common headers:

| Header        | Purpose                       |
| ------------- | ----------------------------- |
| Content-Type  | Type of request/response data |
| Accept        | Data formats client accepts   |
| Authorization | Authentication credentials    |
| User-Agent    | Information about client      |
| Cache-Control | Caching behavior              |

---

# 🔹 Content-Type

`Content-Type` tells the server what type of data is being sent.

Example:

```http
Content-Type: application/json
```

means the body contains JSON.

Other examples:

```text
application/json
text/html
text/plain
multipart/form-data
application/x-www-form-urlencoded
```

---

# 🔹 Authentication

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to do?

---

## API Key

Example:

```http
X-API-Key: abc123
```

The client sends a key to identify/authenticate access.

---

## Basic Authentication

Example:

```text
Username + Password
```

Credentials are sent using the HTTP Authorization mechanism.

HTTPS should be used to protect credentials in transit.

---

## Token Authentication

The server provides a token after authentication.

Example:

```http
Authorization: Bearer <token>
```

The client sends the token with later requests.

---

## JWT

**JWT** stands for:

> JSON Web Token

A JWT can contain claims about the user/session and is commonly used in token-based authentication.

Typical flow:

```text
Login
  ↓
Username + Password
  ↓
Server validates
  ↓
JWT Token
  ↓
Client stores token
  ↓
Client sends token with requests
```

---

## OAuth 2.0

OAuth 2.0 is commonly used when an application needs delegated authorization.

Example:

```text
Login with Google
Login with GitHub
Login with Microsoft
```

OAuth is broader than simply sending a username/password to an API.

---

# 🔹 API Endpoint

An **endpoint** is a specific URL through which an API provides functionality.

Example:

```text
GET /users
```

Another:

```text
GET /users/10
```

Another:

```text
POST /users
```

These can be different endpoints/operations even when they use the same resource path.

---

# 🔹 Flask

**Flask** is a lightweight Python web framework.

It can be used to build:

* Web applications
* REST APIs
* Backend services
* Microservices
* Machine learning APIs

For API development, Flask allows Python functions to be exposed through HTTP routes.

---

# 🔹 Installing Flask

```bash
pip install flask
```

Check installation:

```bash
pip show flask
```

---

# 🔹 Creating a Simple Flask API

Create:

```text
app.py
```

Code:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, API!"


if __name__ == "__main__":
    app.run(debug=True)
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

Response:

```text
Hello, API!
```

---

# 🔹 Understanding the Flask Code

```python
from flask import Flask
```

Imports Flask.

```python
app = Flask(__name__)
```

Creates the Flask application.

```python
@app.route("/")
```

Defines a route.

```python
def home():
```

Defines the function that handles the request.

```python
return "Hello, API!"
```

Returns the response.

```python
app.run(debug=True)
```

Starts the development server.

---

# 🔹 GET API in Flask

```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/users", methods=["GET"])
def get_users():

    users = [
        {
            "id": 1,
            "name": "Mahesh"
        },
        {
            "id": 2,
            "name": "Rahul"
        }
    ]

    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
```

Request:

```text
GET /users
```

Response:

```json
[
    {
        "id": 1,
        "name": "Mahesh"
    },
    {
        "id": 2,
        "name": "Rahul"
    }
]
```

---

# 🔹 Query Parameters in Flask

Suppose the request is:

```text
/users?name=Mahesh
```

Flask:

```python
from flask import Flask, request

app = Flask(__name__)


@app.route("/users", methods=["GET"])
def get_user():

    name = request.args.get("name")

    return {
        "name": name
    }


if __name__ == "__main__":
    app.run(debug=True)
```

Request:

```text
GET /users?name=Mahesh
```

Response:

```json
{
    "name": "Mahesh"
}
```

---

# 🔹 Path Parameters in Flask

Example:

```text
/users/10
```

Flask:

```python
@app.route("/users/<int:user_id>")
def get_user(user_id):

    return {
        "user_id": user_id
    }
```

Request:

```text
GET /users/10
```

Response:

```json
{
    "user_id": 10
}
```

---

# 🔹 POST API in Flask

POST is commonly used to create data.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    return jsonify({
        "message": "User created",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
```

Request:

```http
POST /users
Content-Type: application/json
```

Body:

```json
{
    "name": "Mahesh",
    "age": 22
}
```

Response:

```json
{
    "message": "User created",
    "user": {
        "name": "Mahesh",
        "age": 22
    }
}
```

Status:

```text
201 Created
```

---

# 🔹 PUT API in Flask

```python
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    data = request.get_json()

    return jsonify({
        "message": "User replaced",
        "user_id": user_id,
        "data": data
    })
```

Request:

```http
PUT /users/1
```

Body:

```json
{
    "name": "Mahesh Babu",
    "age": 23
}
```

---

# 🔹 PATCH API in Flask

```python
@app.route("/users/<int:user_id>", methods=["PATCH"])
def update_user_partially(user_id):

    data = request.get_json()

    return jsonify({
        "message": "User partially updated",
        "user_id": user_id,
        "changes": data
    })
```

Request:

```http
PATCH /users/1
```

Body:

```json
{
    "age": 23
}
```

Only the specified field needs to be changed.

---

# 🔹 DELETE API in Flask

```python
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    return jsonify({
        "message": "User deleted",
        "user_id": user_id
    })
```

Request:

```http
DELETE /users/1
```

Response:

```json
{
    "message": "User deleted",
    "user_id": 1
}
```

---

# 🔹 Complete CRUD Flask API

Here is a simple CRUD API using an in-memory Python list.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Mahesh",
        "age": 22
    }
]


# GET - Get all users
@app.route("/users", methods=["GET"])
def get_users():

    return jsonify(users), 200


# GET - Get one user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    for user in users:

        if user["id"] == user_id:
            return jsonify(user), 200

    return jsonify({
        "error": "User not found"
    }), 404


# POST - Create user
@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "age": data["age"]
    }

    users.append(new_user)

    return jsonify(new_user), 201


# PUT - Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    data = request.get_json()

    for user in users:

        if user["id"] == user_id:

            user["name"] = data["name"]
            user["age"] = data["age"]

            return jsonify(user), 200

    return jsonify({
        "error": "User not found"
    }), 404


# DELETE - Delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            return jsonify({
                "message": "User deleted"
            }), 200

    return jsonify({
        "error": "User not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🔹 CRUD Flow

The above API provides:

```text
GET     /users
```

Get all users.

```text
GET     /users/1
```

Get one user.

```text
POST    /users
```

Create a user.

```text
PUT     /users/1
```

Update a user.

```text
DELETE  /users/1
```

Delete a user.

---

# 🔹 Calling an API Using Python

Python can consume APIs using libraries such as `requests`.

Install:

```bash
pip install requests
```

Example:

```python
import requests

url = "https://example.com/api/users"

response = requests.get(url)

print(response.status_code)
print(response.json())
```

---

# 🔹 POST Request Using Python

```python
import requests

url = "https://example.com/api/users"

data = {
    "name": "Mahesh",
    "age": 22
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
```

---

# 🔹 API Testing Tools

Popular tools for testing APIs:

### Postman

Useful for:

* GET
* POST
* PUT
* PATCH
* DELETE
* Headers
* Authentication
* Request bodies
* Testing responses

Example:

```text
Postman
   ↓
POST /users
   ↓
Flask API
   ↓
JSON Response
```

---

## cURL

APIs can also be tested from the terminal.

Example:

```bash
curl http://127.0.0.1:5000/users
```

POST:

```bash
curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d "{\"name\":\"Mahesh\",\"age\":22}"
```

---

# 🔹 Common API Errors

## 400 Bad Request

Possible reasons:

* Invalid JSON
* Missing required field
* Incorrect input format

---

## 401 Unauthorized

Possible reasons:

* Missing authentication
* Invalid token
* Expired token

---

## 403 Forbidden

Possible reason:

* User does not have required permission.

---

## 404 Not Found

Possible reasons:

* Incorrect URL
* Resource doesn't exist
* Incorrect ID

---

## 405 Method Not Allowed

Example:

```text
Endpoint supports GET
but client sends POST
```

---

## 500 Internal Server Error

Possible reasons:

* Python exception
* Database error
* Server-side bug
* Unexpected application failure

---

# 🔹 API Security Basics

When building real APIs:

### 1. Use HTTPS

Do not send sensitive information over unsecured HTTP.

---

### 2. Validate Input

Never blindly trust user input.

Example:

```python
if "name" not in data:
    return {
        "error": "Name is required"
    }, 400
```

---

### 3. Authenticate Users

Use appropriate authentication mechanisms.

Examples:

```text
API Keys
Tokens
JWT
OAuth 2.0
Sessions
```

---

### 4. Authorize Access

Authentication:

```text
Who are you?
```

Authorization:

```text
What can you access?
```

---

### 5. Avoid Exposing Sensitive Information

Do not return:

```text
Passwords
Private keys
Database credentials
Secret API keys
Internal stack traces
```

---

### 6. Use Environment Variables

Instead of:

```python
API_KEY = "my-secret-key"
```

Use environment variables.

Example:

```python
import os

API_KEY = os.getenv("API_KEY")
```

---

# 🔹 REST API Best Practices

## 1. Use nouns for resources

Prefer:

```text
/users
/products
/orders
```

Instead of:

```text
/getUsers
/createProduct
/deleteOrder
```

The HTTP method already describes the action.

---

## 2. Use HTTP methods correctly

```text
GET     /users
POST    /users
PUT     /users/1
PATCH   /users/1
DELETE  /users/1
```

---

## 3. Use meaningful status codes

Example:

```text
200 → Success
201 → Created
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Server Error
```

---

## 4. Return consistent JSON

Example:

```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "Mahesh"
    }
}
```

Error:

```json
{
    "success": false,
    "error": "User not found"
}
```

---

## 5. Use pagination for large data

Instead of:

```text
GET /users
```

returning millions of records, use:

```text
GET /users?page=1&limit=20
```

---

## 6. Support filtering

Example:

```text
/products?category=laptop
```

---

## 7. Support sorting

Example:

```text
/products?sort=price
```

---

# 🔹 API Versioning

As an API changes, versioning can help maintain compatibility.

Example:

```text
/api/v1/users
```

Later:

```text
/api/v2/users
```

This allows different clients to continue using supported API versions.

---

# 🔹 Flask Project Structure

For a small project:

```text
flask_api/
│
├── app.py
├── requirements.txt
└── README.md
```

For a larger project:

```text
flask_api/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── users.py
│   │   └── products.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   └── utils/
│
├── tests/
│   └── test_users.py
│
├── config.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🔹 Flask API + Database

A real application normally does not store data permanently in a Python list.

Instead:

```text
Client
   ↓
Flask API
   ↓
Business Logic
   ↓
Database
```

Possible databases:

```text
MySQL
PostgreSQL
SQL Server
SQLite
MongoDB
```

Example:

```text
POST /users
     ↓
Flask
     ↓
Validate Data
     ↓
SQL Query
     ↓
Database
     ↓
Response
```

---

# 🔹 API + Machine Learning

APIs are especially useful for deploying machine learning models.

Example:

```text
Frontend
   ↓
POST /predict
   ↓
Flask API
   ↓
ML Model
   ↓
Prediction
   ↓
JSON Response
```

Example request:

```json
{
    "age": 45,
    "glucose": 150,
    "blood_pressure": 80
}
```

API response:

```json
{
    "prediction": 1,
    "result": "Positive"
}
```

This allows applications to use a machine learning model without directly loading the model into the frontend.

---

# 🔹 Example ML API

```python
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    age = data["age"]
    glucose = data["glucose"]

    # Example logic only
    if glucose > 140:
        prediction = 1
    else:
        prediction = 0

    return jsonify({
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)
```

In a real ML application:

```text
Request
   ↓
Validation
   ↓
Preprocessing
   ↓
ML Model
   ↓
Prediction
   ↓
JSON Response
```

---

# 🔹 API Flow — Complete Understanding

A typical API request can be understood like this:

```text
                 CLIENT
                   |
                   |
              HTTP REQUEST
                   |
                   ↓
          ┌─────────────────┐
          │   Flask API     │
          └─────────────────┘
                   |
                   ↓
             Route Matching
                   |
                   ↓
            Input Validation
                   |
                   ↓
             Business Logic
                   |
             ┌─────┴─────┐
             ↓           ↓
          Database      ML Model
             |           |
             └─────┬─────┘
                   ↓
             Create Response
                   |
                   ↓
             JSON Response
                   |
                   ↓
                 CLIENT
```

---

# 🔹 Complete Example

Suppose we build a student API.

### Create Student

```http
POST /students
```

Body:

```json
{
    "name": "Mahesh",
    "course": "AIML",
    "cgpa": 8.0
}
```

Response:

```json
{
    "message": "Student created",
    "student": {
        "id": 1,
        "name": "Mahesh",
        "course": "AIML",
        "cgpa": 8.0
    }
}
```

---

### Get Students

```http
GET /students
```

Response:

```json
[
    {
        "id": 1,
        "name": "Mahesh",
        "course": "AIML",
        "cgpa": 8.0
    }
]
```

---

### Get One Student

```http
GET /students/1
```

---

### Update Student

```http
PUT /students/1
```

Body:

```json
{
    "name": "Mahesh Babu",
    "course": "AIML",
    "cgpa": 8.2
}
```

---

### Delete Student

```http
DELETE /students/1
```

---

# 🔹 Important API Concepts

Before moving to advanced API development, understand these concepts clearly:

```text
API
HTTP
Client
Server
Request
Response
URL
URI
Endpoint
HTTP Methods
GET
POST
PUT
PATCH
DELETE
CRUD
JSON
Headers
Content-Type
Status Codes
Path Parameters
Query Parameters
Request Body
Authentication
Authorization
REST
REST API
API Versioning
Pagination
Filtering
Validation
Error Handling
```

---

# 🔹 API Learning Roadmap

## Level 1 — Fundamentals

Learn:

```text
What is API?
What is HTTP?
Client vs Server
Request vs Response
URL
Endpoint
HTTP methods
Status codes
```

---

## Level 2 — REST API

Learn:

```text
REST
REST principles
Resources
CRUD
GET
POST
PUT
PATCH
DELETE
JSON
Path parameters
Query parameters
Headers
```

---

## Level 3 — Flask

Learn:

```text
Flask installation
Flask application
Routes
HTTP methods
request
jsonify
Path parameters
Query parameters
Request body
Error handling
```

---

## Level 4 — Database Integration

Learn:

```text
SQL
MySQL
PostgreSQL
SQLAlchemy
CRUD with database
Relationships
Transactions
```

---

## Level 5 — API Security

Learn:

```text
Authentication
Authorization
API Keys
JWT
OAuth 2.0
Password hashing
HTTPS
CORS
Input validation
Rate limiting
```

---

## Level 6 — Advanced API Development

Learn:

```text
Blueprints
Application Factory
Middleware
Logging
Pagination
Filtering
Sorting
API versioning
Testing
Documentation
Deployment
Docker
Cloud deployment
```

---

# 🔹 Interview Questions

## Beginner

### 1. What is an API?

An API is an interface that allows different software applications to communicate with each other.

---

### 2. What is REST?

REST is an architectural style for designing networked applications, commonly using HTTP and resource-oriented URLs.

---

### 3. What is a REST API?

A REST API is an API designed around REST principles and commonly accessed using HTTP methods.

---

### 4. What is HTTP?

HTTP is an application-layer protocol used for communication between clients and servers.

---

### 5. What is JSON?

JSON is a lightweight data-interchange format commonly used to send structured data through APIs.

---

### 6. Difference between GET and POST?

```text
GET  → Retrieve data
POST → Submit/create data
```

---

### 7. Difference between PUT and PATCH?

```text
PUT   → Replace/update the resource
PATCH → Partially modify the resource
```

---

### 8. What is a status code?

An HTTP status code indicates the outcome of an HTTP request.

Examples:

```text
200
201
400
401
403
404
500
```

---

### 9. What is an endpoint?

An endpoint is a specific API URL through which a client can access a particular resource or operation.

---

### 10. What is Flask?

Flask is a lightweight Python web framework that can be used to build web applications and APIs.

---

# 🔹 Intermediate Interview Questions

### 11. What is the difference between authentication and authorization?

```text
Authentication → Who are you?
Authorization  → What are you allowed to access?
```

---

### 12. What is a path parameter?

A value included directly in the URL path.

Example:

```text
/users/10
```

---

### 13. What is a query parameter?

A parameter passed after `?`.

Example:

```text
/users?city=Hyderabad
```

---

### 14. What is an HTTP header?

A header carries additional metadata about an HTTP request or response.

---

### 15. What is CRUD?

```text
Create
Read
Update
Delete
```

---

### 16. What is JWT?

JWT is a token format commonly used for transmitting claims between parties and for token-based authentication systems.

---

### 17. What is API versioning?

API versioning allows different versions of an API to coexist.

Example:

```text
/api/v1/users
/api/v2/users
```

---

### 18. What is pagination?

Pagination divides a large dataset into smaller pages.

Example:

```text
/users?page=1&limit=20
```

---

# 🔹 Practice Tasks

## Task 1 — Hello API

Create:

```text
GET /
```

Response:

```json
{
    "message": "Hello API"
}
```

---

## Task 2 — Student API

Create:

```text
GET /students
GET /students/<id>
POST /students
PUT /students/<id>
DELETE /students/<id>
```

---

## Task 3 — Product API

Create:

```text
GET /products
POST /products
GET /products/<id>
PUT /products/<id>
DELETE /products/<id>
```

---

## Task 4 — Search API

Create:

```text
GET /products?name=laptop
```

---

## Task 5 — ML Prediction API

Create:

```text
POST /predict
```

Input:

```json
{
    "feature1": 10,
    "feature2": 20
}
```

Output:

```json
{
    "prediction": 1
}
```

---

## Task 6 — Database API

Connect Flask with:

```text
MySQL
```

and implement complete CRUD.

---

# 🔹 Recommended Folder Structure for This Training

For your GitHub repository, APIs can be organized like this:

```text
10_APIs/
│
├── README.md
│
├── 01_API_Basics/
│   ├── API_Notes.md
│   └── API_Examples.ipynb
│
├── 02_HTTP/
│   ├── HTTP_Methods.md
│   └── HTTP_Status_Codes.md
│
├── 03_REST_API/
│   ├── REST_Notes.md
│   └── REST_Examples.md
│
├── 04_JSON/
│   └── JSON_Practice.py
│
├── 05_Flask/
│   ├── hello_flask.py
│   ├── get_api.py
│   ├── post_api.py
│   ├── put_api.py
│   ├── patch_api.py
│   └── delete_api.py
│
├── 06_CRUD_API/
│   └── crud_api.py
│
├── 07_API_Practice/
│   ├── student_api.py
│   ├── product_api.py
│   └── prediction_api.py
│
└── 08_API_Projects/
    └── README.md
```

---

# 🔹 Quick Revision

```text
API
 ↓
Allows applications to communicate

HTTP
 ↓
Communication protocol

REST
 ↓
Architectural style

REST API
 ↓
API designed using REST principles

JSON
 ↓
Common data format

HTTP Methods
 ↓
GET
POST
PUT
PATCH
DELETE

CRUD
 ↓
Create
Read
Update
Delete

Flask
 ↓
Python framework for building web applications/APIs

Request
 ↓
Method + URL + Headers + Body

Response
 ↓
Status Code + Headers + Body
```

---

# 🔹 One Complete API Example

```text
Client
   |
   | POST /users
   | JSON Data
   ↓
Flask API
   |
   | Validate
   ↓
Business Logic
   |
   ↓
Database
   |
   ↓
Flask API
   |
   | 201 Created
   | JSON Response
   ↓
Client
```

---

# 🔹 Final Understanding

The most important concept is to understand the complete flow:

```text
CLIENT
   ↓
HTTP REQUEST
   ↓
API ENDPOINT
   ↓
FLASK ROUTE
   ↓
VALIDATION
   ↓
BUSINESS LOGIC
   ↓
DATABASE / ML MODEL
   ↓
HTTP RESPONSE
   ↓
JSON
   ↓
CLIENT
```

For example:

```text
POST /predict
```

could mean:

```text
User sends data
      ↓
Flask receives request
      ↓
Extract JSON
      ↓
Validate input
      ↓
Preprocess data
      ↓
ML model prediction
      ↓
Create JSON response
      ↓
Return response
```

This is the basic foundation for building **Python backend applications, REST APIs, ML APIs, and production web services**.

---

# 📌 Key Takeaways

* API = communication interface between applications.
* HTTP = protocol commonly used for API communication.
* REST = architectural style.
* REST API = API designed around REST principles.
* JSON = common data format.
* GET = retrieve data.
* POST = submit/create data.
* PUT = replace a resource.
* PATCH = partially modify a resource.
* DELETE = delete a resource.
* CRUD = Create, Read, Update, Delete.
* Status codes communicate the result of a request.
* Path parameters identify resources.
* Query parameters filter/customize requests.
* Headers carry metadata.
* Authentication verifies identity.
* Authorization determines access.
* Flask can be used to build Python APIs.
* APIs can connect applications with databases and ML models.

---

## 🚀 Next Step

After understanding these fundamentals, the next practical progression is:

```text
API Basics
     ↓
HTTP
     ↓
REST API
     ↓
JSON
     ↓
Flask
     ↓
CRUD
     ↓
MySQL + Flask
     ↓
Authentication
     ↓
JWT
     ↓
API Testing
     ↓
ML Model API
     ↓
Deployment
```

**Goal:** Build at least one complete Flask REST API connected to a database and test it using Postman.
