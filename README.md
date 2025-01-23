# loging_singup

# Flask Signup and Login System

This project is a Flask-based application for user registration, login, and role-based redirection. Users can sign up as either "Patients" or "Doctors" and will be redirected to their respective dashboards upon logging in. The app also supports profile picture uploads and validates user inputs.

---

## **Features**

- **User-Specific Views**:
  - Separate views for doctors and patients to access blogs relevant to them.
  
- **Dynamic Blog Content**:
  - Blogs are dynamically rendered with title, category, status, and images.

- **Draft and Publish Options**:
  - Blogs can be saved as drafts or marked as published.

- **Image Support**:
  - Images are displayed for blogs, with a default placeholder if no image is provided.

- **Category Tagging**:
  - Predefined categories for blogs: Mental Health, Heart Disease, Covid19, and Immunization.

- **Responsive Design**:
  - Clean and responsive design for better user experience.

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

- **Responsive Design**:
   - Optimized UI for both desktop and mobile devices.
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
### Step 4: Set Up Directories for Uploads
Ensure the directory for profile picture uploads exists:
```bash
mkdir -p static/profile_pictures
```
### Step 5: Run the Application
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
4. Submit the form to create your account.
### Login
1. Visit `/login` or click the "Login" link.
2. Enter your username and password.
3. Upon successful login, you'll be redirected to your role-specific dashboard:
   - **Patient Dashboard**: Displays the patient's personal information.
   - **Doctor Dashboard**: Displays the doctor's personal information.
### Doctor Blogs View
1. URL: ` /doctor/blogs `
2. Displays blogs specific to doctors.
### Patient Blogs View
1. URL: `/patient/blogs`
2. Displays blogs curated for patients.
### Blog Details
1. Title, category, and status are displayed for each blog.
2. Images are loaded dynamically from `static/uploads/`.
---

## **Project Structure**

```
project/
├── app.py                 # Main Flask application file
├── sql                    # SQL database giles
|   ├── blog_app.blogs     # blog storage 
|   ├── schema.sql         # structure of database
|   ├── seed.sql           # test data entered
├── templates/             # HTML templates for the app
│   ├── patient_blogs.html # Patient-specific blog view
|   ├── base.html          # Base HTML template
|   ├── doctor_blogs.html   # Doctor-specific blog view
|   ├── base.html          # Base layout template
│   ├── signup.html        # Signup form
│   ├── login.html         # Login form
│   ├── dashboard_patient.html # Patient dashboard
│   └── dashboard_doctor.html  # Doctor dashboard
├── static/                # Static assets (CSS, images, etc.)
│   ├── styles.css         # Main stylesheet
|   ├── uploads            # upload files pngs
│   └── profile_pictures/  # Profile picture uploads
├── README.md              # Project documentation
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
