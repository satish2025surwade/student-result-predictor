============================================
   STUDENT RESULT PREDICTOR — BCA PROJECT
============================================
Developed By : Surwade Satish Sanjay
PRN Number   : 2022015400251545
Project Guide: Tajhshree Patil 
College      : PDUSPM's IMR Jamner, Jalgaon
Subject      : BCA 605 — Project Work (Semester VI)
Domain       : Artificial Intelligence / Machine Learning
Year         : 2025 - 2026
============================================


============================================
   FIRST TIME SETUP (Do this only ONCE)
============================================

STEP 1: Place this folder anywhere on your computer
        (Recommended: Desktop or Documents)

STEP 2: Open the folder in VS Code
        → Open VS Code
        → Click: File > Open Folder
        → Select the "student_predictor" folder
        → Click OK

STEP 3: Open the Terminal inside VS Code
        → Press: Ctrl + ` (backtick key)
        → OR go to top menu: Terminal > New Terminal

STEP 4: Install Flask (requires internet connection)
        Type the following command and press Enter:

            pip install flask

        Wait for installation to complete.
        This step is required only ONCE.


============================================
   HOW TO RUN THE PROJECT (Every time)
============================================

Open VS Code Terminal and type:

    python app.py

Then open your browser and go to:

    http://127.0.0.1:5000

Login Credentials:
    Username : admin
    Password : admin123


============================================
   PROJECT FILES — WHAT EACH FILE DOES
============================================

app.py               → Main Python code (brain of the application)
students.csv         → All student data is stored here
requirements.txt     → List of required Python libraries

templates/
    login.html       → Admin login page
    base.html        → Common layout (navbar, styles)
    dashboard.html   → Home page with charts and statistics
    add_student.html → Add new student and get prediction
    all_students.html→ View all students with delete option
    predict.html     → Quick prediction page (without saving)

static/              → Folder for CSS and JS files (if any)
README.txt           → This instruction file


============================================
   TROUBLESHOOTING — COMMON ERRORS
============================================

Problem  : "flask not found" or "ModuleNotFoundError: flask"
Solution : Run this command in terminal:
               pip install flask

--------------------------------------------

Problem  : "'python' is not recognized"
Solution : Reinstall Python from: https://python.org
           During installation, make sure to check:
           "Add Python to PATH"

--------------------------------------------

Problem  : "Port 5000 already in use"
Solution : Open app.py, go to the last line and change it to:
               app.run(debug=True, port=5001)
           Then open browser and go to:
               http://127.0.0.1:5001

--------------------------------------------

Problem  : "No such file or directory: app.py"
Solution : Make sure you opened the correct folder in VS Code.
           The terminal must be inside the student_predictor folder.
           Check the terminal path — it should show:
               C:\Users\...\student_predictor>

--------------------------------------------

Problem  : Page opens but shows error
Solution : Check that students.csv exists in the project folder.
           If missing, delete it and restart — it will be recreated.


============================================
   HOW THE ML PREDICTION WORKS
============================================

The system uses a Weighted Scoring Algorithm:

    Attendance (40%)  +  Internal Marks (35%)
  + Assignment (15%)  +  Previous Result (10%)
  = Total Score out of 100

    Score >= 60  →  Result: PASS
    Score  < 60  →  Result: FAIL

The confidence percentage shows how certain
the model is about its prediction.


============================================
   DEPLOYMENT (Run Online)
============================================

To make this project accessible online for free:

Option 1 — render.com (Easiest):
    Website  : https://render.com/
    Plan     : Free Beginner Account
    Live URL : https://yourusername.pythonanywhere.com

Option 2 — Render.com:
    Website  : www.render.com
    Plan     : Free (requires GitHub account)
    Live URL : https://student-result-predictor-1.onrender.com/


============================================
   TECHNOLOGY STACK
============================================

Language   : Python 3.x
Framework  : Flask 3.0.0
Database   : CSV File (students.csv)
Frontend   : HTML5, CSS3 (Jinja2 Templates)
Hosting    : Render.com (Free)


============================================
   PROJECT FEATURES
============================================

    Login / Logout with session management
    Add new student with all academic data
    ML-based Pass / Fail prediction
    Confidence score with progress bar
    Dashboard with pass rate and charts
    View all students in a table
    Delete student records
    Quick predict without saving data
    Data stored permanently in CSV file


============================================
   CONTACT & SUPPORT
============================================

University : Kavayitri Bahinabai Chaudhari
             North Maharashtra University, Jalgaon
Course     : Bachelor of Computer Applications (BCA)
Subject    : BCA 605 — Project Work
Semester   : VI (Sixth Semester)
MY Insta   : https://www.instagram.com/its_coding_time_tech/
============================================
