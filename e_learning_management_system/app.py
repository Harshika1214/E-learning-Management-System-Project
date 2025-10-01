from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Course, Assignment, Submission
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elearning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# ---------------- Helper / Decorators -----------------
def login_required(role=None):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if 'user_id' not in session:
                flash("Please login first")
                return redirect(url_for('login'))
            if role and session.get('role') != role:
                flash("Access Denied")
                return redirect(url_for('home'))
            return f(*args, **kwargs)
        return decorated
    return decorator

# ---------------- Routes -----------------
@app.route('/')
def home():
    return render_template('home.html')

# Registration
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        if User.query.filter_by(email=email).first():
            flash("User already exists!")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please login.")
        return redirect(url_for('login'))

    return render_template('register.html')

# Login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password,password):
            flash("Invalid credentials!")
            return redirect(url_for('login'))

        session['user_id'] = user.id
        session['role'] = user.role
        if user.role=='student':
            return redirect(url_for('student_dashboard'))
        else:
            return redirect(url_for('teacher_dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully")
    return redirect(url_for('home'))

# Add/Edit/Delete Course
@app.route('/add-course', methods=['GET','POST'])
@login_required(role='teacher')
def add_course():
    if request.method=='POST':
        title = request.form['title']
        description = request.form['description']
        db.session.add(Course(title=title, description=description))
        db.session.commit()
        flash("Course added successfully")
        return redirect(url_for('view_courses'))
    return render_template('add_course.html')

@app.route('/courses')
@login_required()
def view_courses():
    courses = Course.query.all()
    return render_template('view_courses.html', courses=courses)

@app.route('/edit-course/<int:course_id>', methods=['GET','POST'])
@login_required(role='teacher')
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    if request.method=='POST':
        course.title = request.form['title']
        course.description = request.form['description']
        db.session.commit()
        flash("Course updated successfully")
        return redirect(url_for('view_courses'))
    return render_template('edit_course.html', course=course)

@app.route('/delete-course/<int:course_id>', methods=['POST'])
@login_required(role='teacher')
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash("Course deleted successfully")
    return redirect(url_for('view_courses'))

# Add/Edit/Delete Assignment
@app.route('/add-assignment', methods=['GET','POST'])
@login_required(role='teacher')
def add_assignment():
    courses = Course.query.all()
    if request.method=='POST':
        title = request.form['title']
        description = request.form['description']
        course_id = int(request.form['course_id'])
        db.session.add(Assignment(title=title, description=description, course_id=course_id))
        db.session.commit()
        flash("Assignment added successfully")
        return redirect(url_for('view_assignments'))
    return render_template('add_assignment.html', courses=courses)

@app.route('/assignments')
@login_required()
def view_assignments():
    assignments = Assignment.query.all()
    return render_template('view_assignments.html', assignments=assignments)

@app.route('/edit-assignment/<int:assignment_id>', methods=['GET','POST'])
@login_required(role='teacher')
def edit_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    courses = Course.query.all()
    if request.method=='POST':
        assignment.title = request.form['title']
        assignment.description = request.form['description']
        assignment.course_id = int(request.form['course_id'])
        db.session.commit()
        flash("Assignment updated successfully")
        return redirect(url_for('view_assignments'))
    return render_template('edit_assignment.html', assignment=assignment, courses=courses)

@app.route('/delete-assignment/<int:assignment_id>', methods=['POST'])
@login_required(role='teacher')
def delete_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    db.session.delete(assignment)
    db.session.commit()
    flash("Assignment deleted successfully")
    return redirect(url_for('view_assignments'))

# Student dashboard
@app.route('/student-dashboard')
@login_required(role='student')
def student_dashboard():
    courses = Course.query.all()
    assignments = Assignment.query.all()
    return render_template('student_dashboard.html', courses=courses, assignments=assignments)

# Teacher dashboard
@app.route('/teacher-dashboard')
@login_required(role='teacher')
def teacher_dashboard():
    courses = Course.query.all()
    assignments = Assignment.query.all()
    return render_template('teacher_dashboard.html', courses=courses, assignments=assignments)

# Submit assignment
@app.route('/submit-assignment/<int:assignment_id>', methods=['GET','POST'])
@login_required(role='student')
def submit_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    if request.method=='POST':
        content = request.form['content']
        db.session.add(Submission(student_id=session['user_id'], assignment_id=assignment.id, content=content))
        db.session.commit()
        flash("Assignment submitted successfully")
        return redirect(url_for('student_dashboard'))
    return render_template('submit_assignment.html', assignment=assignment)

# Review & Grade Submissions
@app.route('/review-submissions/<int:assignment_id>', methods=['GET','POST'])
@login_required(role='teacher')
def review_submissions(assignment_id):
    submissions = Submission.query.filter_by(assignment_id=assignment_id).all()
    if request.method=='POST':
        for sub in submissions:
            sub.marks = int(request.form.get(f'marks_{sub.id}', 0))
            sub.feedback = request.form.get(f'feedback_{sub.id}', '')
        db.session.commit()
        flash("Submissions graded successfully")
        return redirect(url_for('teacher_dashboard'))
    return render_template('review_submissions.html', submissions=submissions)

# Run server
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
