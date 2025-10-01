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

##  Project Structure  
```bash
e_learning_management_system/
-- app.py
-- models.py
-- templates/
   -- index.html
   -- login.html
   -- dashboard.html
   -- add_course.html
   -- view_course.html
   -- add_assignment.html
   -- view_assignment.html
-- static/
   -- style.css
-- README.md


---

##  How to Run Locally  

1. Clone this repository  
   ```bash
   git clone https://github.com/Harshika1214/E-learning-Management-System-Project.git
   cd E-learning-Management-System-Project

2. Install dependencies
   ```bash
    pip install flask

3. Run the project
   ```bash
   python app.py

4. Open in browser
   ```bash
   http://127.0.0.1:5000

---

## Future Improvements
-  Add quiz/exam feature
-  Student progress tracking
-  Email notifications for deadlines
-  Dark mode UI

This project is created as part of learning Flask, Python, and web development. Open to contributions & improvements!


