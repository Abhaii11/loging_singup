from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for sessions

# Directory to store profile pictures
UPLOAD_FOLDER = 'static/profile_pictures'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database setup
DATABASE = 'users.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                profile_picture TEXT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                user_type TEXT NOT NULL,
                address_line1 TEXT,
                city TEXT,
                state TEXT,
                pincode TEXT
            )
        ''')
        conn.commit()

# Home route
@app.route('/')
def home():
    return redirect(url_for('signup'))

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Collect form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        user_type = request.form['user_type']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        address_line1 = request.form['address_line1']
        city = request.form['city']
        state = request.form['state']
        pincode = request.form['pincode']

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return render_template('signup.html')

        # Ensure the profile picture directory exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # Save profile picture
        profile_picture = None
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file.filename != '':
                profile_picture = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], profile_picture))

        # Hash password for security
        hashed_password = generate_password_hash(password)

        # Save user to database
        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (
                        first_name, last_name, profile_picture, username, email, password, user_type,
                        address_line1, city, state, pincode
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (first_name, last_name, profile_picture, username, email, hashed_password,
                      user_type, address_line1, city, state, pincode))
                conn.commit()
                flash('Signup successful! Please login.', 'success')
                return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or Email already exists!', 'error')

    return render_template('signup.html')
    
# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()

            if user and check_password_hash(user[6], password):  # Verify password
                session['user_id'] = user[0]
                session['username'] = user[4]
                session['user_type'] = user[7]

                if user[7] == 'Patient':
                    return redirect(url_for('dashboard_patient'))
                elif user[7] == 'Doctor':
                    return redirect(url_for('dashboard_doctor'))

            flash('Invalid username or password!', 'error')

    return render_template('login.html')

# Patient dashboard
@app.route('/dashboard/patient')
def dashboard_patient():
    if session.get('user_type') != 'Patient':
        return redirect(url_for('login'))
    return render_template('dashboard_patient.html', user=session)

# Doctor dashboard
@app.route('/dashboard/doctor')
def dashboard_doctor():
    if session.get('user_type') != 'Doctor':
        return redirect(url_for('login'))
    return render_template('dashboard_doctor.html', user=session)

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
