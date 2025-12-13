📝 Django Blogging Website

A modern, responsive Blogging Website built with Django, enabling users to explore, search, and engage with high-quality blog content. This project is ideal for learning Django best practices, demonstrating skills, or deploying a production-ready blog.

🚀 Features

🏠 Home Page showcasing featured and latest posts

🔍 Advanced Search by title, description, or full blog content

🗂️ Category-wise Blog Listing for easy navigation

📄 Single Blog Detail View with featured image and content

💬 Comment System for authenticated users

👤 User Authentication (Register / Login / Logout)

🧑‍💻 Admin Dashboard for managing blogs, categories, and comments

🖼️ Media Upload support (featured images)

📱 Fully Responsive with Bootstrap 4

⚡ SEO-friendly URLs using unique slugs

🛠️ Tech Stack

Backend: Django 6.0

Frontend: HTML, CSS, Bootstrap 4

Database: SQLite (Development), ready for PostgreSQL (Production)

📂 Project Structure

blog_main/
│── blog_main/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
│── blogs/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
│
│── dashboards/
│ ├── views.py
│ └── templates/
│
│── templates/
│ ├── base.html
│ ├── home.html
│ ├── search.html
│ ├── posts_by_category.html
│ └── blogs.html
│
│── static/
│── media/
│── manage.py
│── requirements.txt
│── README.md

🔍 Search Functionality

Search is available in the header.

Users can search using keywords in titles, descriptions, or full blog content.

Results are displayed dynamically on the search results page.

🔐 Authentication Flow

Register new accounts or login for existing users.

Only logged-in users can comment.

Admin can manage posts, categories, and comments.

📦 Deployment Notes

.gitignore includes db.sqlite3 and media/ to prevent sensitive files being pushed.

Configure ALLOWED_HOSTS, static files, and media paths for production.

Compatible with PythonAnywhere or any Django-supported hosting.

📸 Screenshots

Add screenshots here for Home, Blog Detail, Search, and Admin Dashboard (optional).

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m 'Add feature')

Push to the branch (git push origin feature-name)

Open a Pull Request

Authentication: Django Built-in Auth System

Version Control: Git & GitHub
