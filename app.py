from flask import Flask, render_template, request, redirect, session
import csv, os

app = Flask(__name__)
app.secret_key = "bca_project_2025"

CSV_FILE = "students.csv"

#  CSV file create by satish
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id","name","roll","attendance","marks","assignment","prev_result","result","confidence"])
            # Sample data
            writer.writerow([1,"Priya Patil","BCA001",88,42,17,"Pass","Pass",92])
            writer.writerow([2,"Rohit Desai","BCA002",42,28,9,"Fail","Fail",85])
            writer.writerow([3,"Sneha Joshi","BCA003",76,38,15,"Pass","Pass",78])

#  ML Prediction Logic 
def predict_result(attendance, marks, assignment, prev_result):
    score = (attendance / 100) * 40 + (marks / 50) * 35 + (assignment / 20) * 15
    if prev_result == "Pass":
        score += 10
    confidence = min(99, max(51, round(score)))
    result = "Pass" if score >= 60 else "Fail"
    return result, confidence, round(score)

#  Read Data of Students by CSV file
def get_all_students():
    students = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
    return students

# New Students Entry in CSV 
def save_student(student):
    students = get_all_students()
    new_id = len(students) + 1
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            new_id,
            student["name"],
            student["roll"],
            student["attendance"],
            student["marks"],
            student["assignment"],
            student["prev_result"],
            student["result"],
            student["confidence"]
        ])

#  Student delete
def delete_student(del_id):
    students = get_all_students()
    students = [s for s in students if s["id"] != del_id]
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id","name","roll","attendance","marks","assignment","prev_result","result","confidence"])
        for i, s in enumerate(students):
            writer.writerow([i+1, s["name"], s["roll"], s["attendance"],
                             s["marks"], s["assignment"], s["prev_result"],
                             s["result"], s["confidence"]])

# =================== ROUTES ===================

@app.route("/", methods=["GET","POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "Satish" and password == "admin123":
            session["user"] = "admin"
            return redirect("/dashboard")
        else:
            error = " Wrong username or password!"
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    students = get_all_students()
    total = len(students)
    passed = sum(1 for s in students if s["result"] == "Pass")
    failed = total - passed
    recent = students[-3:][::-1]
    return render_template("dashboard.html",
                           total=total, passed=passed, failed=failed,
                           recent=recent, students=students)

@app.route("/add", methods=["GET","POST"])
def add_student():
    if "user" not in session:
        return redirect("/")
    result_data = None
    error = ""
    if request.method == "POST":
        name       = request.form.get("name", "").strip()
        roll       = request.form.get("roll", "").strip()
        attendance = request.form.get("attendance", "")
        marks      = request.form.get("marks", "")
        assignment = request.form.get("assignment", "")
        prev       = request.form.get("prev_result", "Pass")

        if not name or not roll:
            error = "Name aur Roll Number zaroori hai!"
        elif not attendance or not marks or not assignment:
            error = "Saare fields bharo!"
        else:
            att  = float(attendance)
            mrk  = float(marks)
            asgn = float(assignment)
            res, conf, score = predict_result(att, mrk, asgn, prev)
            student = {
                "name": name, "roll": roll,
                "attendance": att, "marks": mrk,
                "assignment": asgn, "prev_result": prev,
                "result": res, "confidence": conf
            }
            save_student(student)
            result_data = {"name": name, "result": res, "conf": conf, "score": score}

    return render_template("add_student.html", result=result_data, error=error)

@app.route("/students")
def all_students():
    if "user" not in session:
        return redirect("/")
    students = get_all_students()
    return render_template("all_students.html", students=students)

@app.route("/delete/<student_id>")
def delete(student_id):
    if "user" not in session:
        return redirect("/")
    delete_student(student_id)
    return redirect("/students")

@app.route("/predict", methods=["GET","POST"])
def quick_predict():
    if "user" not in session:
        return redirect("/")
    result_data = None
    if request.method == "POST":
        att  = float(request.form.get("attendance", 0))
        mrk  = float(request.form.get("marks", 0))
        asgn = float(request.form.get("assignment", 0))
        prev = request.form.get("prev_result", "Pass")
        res, conf, score = predict_result(att, mrk, asgn, prev)
        result_data = {"result": res, "conf": conf, "score": score}
    return render_template("predict.html", result=result_data)

# =================== RUN ===================
if __name__ == "__main__":
    init_csv()
    print(" Server is Ready!")
    print(" Browser : http://127.0.0.1:5000")
    app.run(debug=True)
