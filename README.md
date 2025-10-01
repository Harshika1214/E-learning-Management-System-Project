# E-Learning Management System

## Project Overview
This is a full-featured **E-Learning Management System** built using **Python** and **Flask**. The project allows students, teachers, and admins to manage courses, assignments, submissions, and feedback efficiently.

## Features
### User Authentication
- Register and login for students, teachers, and admins.
- Passwords are securely hashed using `werkzeug.security`.

### Courses
- Teachers/admins can **add, edit, delete**, and view courses.
- Students can view available courses.

### Assignments
- Teachers/admins can **add, edit, delete**, and view assignments.
- Students can view assignments linked to courses.

### Submissions
- Students can **submit assignments** (text-based content).
- Teachers/admins can **review submissions**, provide marks and feedback.

### Dashboards
- Separate dashboards for **students** and **teachers/admins**.
- Students see available courses and assignments.
- Teachers/admins see all courses, assignments, and submissions.

### Access Control & Validation
- Role-based access: Students cannot access teacher/admin pages.
- Flash messages for success/error notifications.
- Email validation during registration.

### Styling
- Basic **CSS** styling to make the interface clean and user-friendly.
- Responsive tables, navigation menus, and buttons.

## Tech Stack
- **Python 3.x**
- **Flask**
- **SQLite** (for database)
- **HTML/CSS**
- **Werkzeug** for password hashing

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Harshika1214/E-learning-Management-System-Project.git
