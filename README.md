📚 Library Book Management System API

A RESTful API built using Flask that allows users to manage library books with secure authentication and role-based access control. The system supports CRUD operations on books and uses JWT Authentication to restrict modifications to authorized users.

🚀 Features

User Registration & Login

JWT Authentication

Role-Based Access (Admin / User)

Add, View, Update, Delete Books

SQLite Database

Input Validation & Error Handling

Tested using Postman

🛠️ Tech Stack

Python

Flask

Flask-SQLAlchemy

Flask-JWT-Extended

Flask-Bcrypt

SQLite

Postman

📂 Project Structure
LibraryBookManagementSystem
 ┣ app.py
 ┣ database.py
 ┣ requirements.txt
 ┣ README.md
 ┣ models
 ┃ ┣ book_model.py
 ┃ ┗ user_model.py
 ┣ routes
 ┃ ┣ book_routes.py
 ┃ ┗ auth_routes.py
 ┗ instance
    ┗ library.db
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yourusername/LibraryBookManagementSystem.git
cd LibraryBookManagementSystem

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Application
python app.py


Server will start at:

http://127.0.0.1:5000/

🔐 Authentication APIs
➤ Register User
POST /register

{
  "username": "admin",
  "password": "admin123",
  "role": "admin"
}

➤ Login User
POST /login

{
  "username": "admin",
  "password": "admin123"
}


Response:

{
  "access_token": "your_jwt_token_here"
}

📚 Book APIs
Method	Endpoint	Description	Protected
POST	/books	Add Book	Yes (Admin)
GET	/books	Get All Books	No
GET	/books/{id}	Get Book by ID	No
PUT	/books/{id}	Update Book	Yes (Admin)
DELETE	/books/{id}	Delete Book	Yes (Admin)
🔑 Using JWT Token in Postman

Login and copy access_token

Open Postman

Authorization → Bearer Token

Paste token

Call protected APIs

✅ Sample Book JSON
{
  "id": 1,
  "title": "Python Basics",
  "author": "Guido van Rossum",
  "year": 2022
}
