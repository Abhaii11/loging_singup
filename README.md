# loging_singup

# Flask Signup and Login System

This project is a Flask-based application for user registration, login, and role-based redirection. Users can sign up as either "Patients" or "Doctors" and will be redirected to their respective dashboards upon logging in. The app also supports profile picture uploads and validates user inputs.

---

## **Features**

- **Signup Form**:
  - Fields: First Name, Last Name, Profile Picture, Username, Email, Password, Address, etc.
  - Password and Confirm Password validation.
  - Profile picture upload with file type sanitization.

- **Login**:
  - Username and password authentication.
  - Role-based redirection to the respective dashboard (Patient or Doctor).

- **Dashboards**:
  - Displays user information based on the data entered during signup.
  - Separate dashboards for Patients and Doctors.

---

## **Requirements**

To run this application, you'll need the following:

- Python 3.8 or higher
- Flask Framework
- SQLite (comes pre-installed with Python)
- A web browser to test the app locally

---

## **Installation**

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone git@github.com:Abhaii11/loging_singup.git
cd loging_singup
```

### Step 2: Set Up a Virtual Environment
Create and activate a virtual environment (optional but recommended):
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
Install the required Python packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
Run the Flask application:
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your web browser to access the app.

---

## **Usage**

### Signup
1. Visit `/signup` or click the "Signup" link from the homepage.
2. Fill out the form with your details.
3. Submit the form to create your account.

### Login
1. Visit `/login` or click the "Login" link.
2. Enter your username and password.
3. Upon successful login, you'll be redirected to your role-specific dashboard:
   - **Patient Dashboard**: Displays the patient's personal information.
   - **Doctor Dashboard**: Displays the doctor's personal information.

---

## **Project Structure**

```
project/
├── app.py                 # Main Flask application file
├── templates/             # HTML templates for the app
│   ├── base.html          # Base layout template
│   ├── signup.html        # Signup form
│   ├── login.html         # Login form
│   ├── dashboard_patient.html # Patient dashboard
│   └── dashboard_doctor.html  # Doctor dashboard
├── static/                # Static assets (CSS, images, etc.)
│   ├── styles.css         # Main stylesheet
│   └── profile_pictures/  # Profile picture uploads
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Files and directories to ignore in Git
```

---

## **Screenshots**

### Signup Page
![Signup Page](https://via.placeholder.com/800x400?text=Signup+Page)

### Login Page
![Login Page](https://via.placeholder.com/800x400?text=Login+Page)

### Patient Dashboard
![Patient Dashboard](https://via.placeholder.com/800x400?text=Patient+Dashboard)

### Doctor Dashboard
![Doctor Dashboard](https://via.placeholder.com/800x400?text=Doctor+Dashboard)

---

## **Technologies Used**

- **Frontend**: HTML, CSS, Jinja2 templates
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Styling**: Custom CSS (responsive design)

---

## **Future Enhancements**

- Add validation for file uploads (only allow `.jpg`, `.png`, etc.).
- Implement password reset functionality.
- Add an admin panel for user management.
- Improve dashboards with dynamic charts and statistics.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For questions or suggestions, please reach out to me:

- **Email**: rautabhay66.com
- **GitHub**: [Abhii11]([https://github.com/Abhaii11])
