from flask import Flask, render_template, request, redirect, url_for, session
from data import question_data

app = Flask(__name__)
app.secret_key = "aws_quiz_secret_key"

@app.route("/")
def home():
    session.clear()  # reset quiz every time you go home
    return render_template("home.html")

@app.route("/questions", methods=["GET", "POST"])
def questions():
    # start quiz - set index to 0
    if "q_index" not in session:
        session["q_index"] = 0
        session["score"] = 0
        session["answers"] = []

    if request.method == "POST":
        user_answer = request.form.get("answer")  # will be "true" or "false"
        q_index = session["q_index"]
        current_q = question_data[q_index]

        # use the check_answer method from Question class
        is_correct = current_q.check_answer(user_answer == "true")

        # save result using dot notation
        session["answers"] = session["answers"] + [{
            "question": current_q.question,
            "correct": is_correct,
            "explanation": current_q.explanation,
            "correct_answer": current_q.correct_answer
        }]

        if is_correct:
            session["score"] += 1

        session["q_index"] += 1

        # if all questions done, go to results
        if session["q_index"] >= len(question_data):
            return redirect(url_for("results"))

    q_index = session["q_index"]
    current_q = question_data[q_index]
    total = len(question_data)
    progress = int((q_index + 1) / total * 100)  # ← added this

    return render_template("question.html",
                           question=current_q,
                           q_number=q_index + 1,
                           total=total,
                           progress=progress)  # ← added this

@app.route("/results")
def results():
    score = session.get("score", 0)
    answers = session.get("answers", [])
    total = len(question_data)
    return render_template("result.html",
                           score=score,
                           total=total,
                           answers=answers)

if __name__ == "__main__":
    app.run(debug=True)