from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "eduspark_secret"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    score = 0
    if request.method == "POST":
        answers = {
            "q1": "a",
            "q2": "b",
            "q3": "c",
            "q4": "a",
            "q5": "b"
        }

        for key in answers:
            if request.form.get(key) == answers[key]:
                score += 1

        flash(f"Your Score: {score}/5")
        return redirect(url_for("quiz"))

    return render_template("quiz.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Message Sent Successfully!")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)