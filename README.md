#  E-Learning Management System  

An online platform for managing courses, assignments, and student–teacher interactions.  
This project allows **teachers to create/manage courses and assignments**, while **students can enroll, submit assignments, and receive feedback & marks**.  

---

##  Features  

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
---

##  Tech Stack  

- **Frontend**: HTML, CSS  
- **Backend**: Flask (Python)  
- **Database**: SQLite / MySQL  
- **Version Control**: Git & GitHub  

---

## Project Structure
- app.py
- models.py
- templates/
   - index.html
   - login.html
   - dashboard.html
   - add_course.html
   - view_course.html
   - add_assignment.html
   - view_assignment.html
   - edit_course.html
   - edit_assignment.html
   - submit_assignment.html
   - review_submissions.html
- static/
   - style.css
- Project_Images/
   -Home_page.png
   -Login_page.png
   -Register_dashboard.png
   -Teacher_dashboard.png
   -Course_dashboard.png
   -Assignment_dashboard.png
   -Student_dashboard.png
   -Review_submission_dashboard.png
   -Result_dashboard.png
- README.md

---

## How to Run Locally

1. Clone this repository:
```bash
git clone https://github.com/Harshika1214/E-learning-Management-System-Project.git
cd E-learning-Management-System-Project
  

2. Install dependencies  
   ```bash
   pip install flask

## Run the project  

```bash
python app.py

## Open in browser  

[http://127.0.0.1:5000](http://127.0.0.1:5000)








