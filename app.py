from flask import Flask, render_template, request
import requests
import html

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    categories = {
        "random": "Random Quiz",
        "9": "General Knowledge",
        "17": "Science & Nature",
        "18": "Technology (Computers)",
        "19": "Science: Mathematics",
        "21": "Sports",
        "22": "Geography",
        "23": "History",
        "27": "Animals"
    }
    return render_template("index.html", categories=categories)

# Quiz page
@app.route("/quiz")
def quiz():
    categories = {
        "random": "Random Quiz",
        "9": "General Knowledge",
        "17": "Science & Nature",
        "18": "Technology (Computers)",
        "19": "Science: Mathematics",
        "21": "Sports",
        "22": "Geography",
        "23": "History",
        "27": "Animals"
    }

    category = request.args.get("category", "9")
    if category not in categories:
        category = "9"

    api_url = (
        "https://opentdb.com/api.php?amount=5&type=multiple"
        if category == "random"
        else f"https://opentdb.com/api.php?amount=5&type=multiple&category={category}"
    )

    response = requests.get(api_url)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return render_template("quiz.html", questions=[], error="No questions found for this category. Please try another.")

    questions = []
    for q_index, item in enumerate(data["results"]):
        question_text = html.unescape(item["question"])
        correct_answer = html.unescape(item["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in item["incorrect_answers"]]

        options = incorrect_answers + [correct_answer]

        question_dict = {"question": question_text, "options": [], "correct": None}
        for j, option in enumerate(options):
            opt_id = f"q{q_index}_opt{j}"
            question_dict["options"].append({"id": opt_id, "text": option})
            if option == correct_answer:
                question_dict["correct"] = opt_id

        questions.append(question_dict)

    return render_template("quiz.html", questions=questions, category_name=categories[category])

# Result page
@app.route("/result", methods=["POST"])
def result():
    total_questions = int(request.form.get("total_questions"))

    # Collect selected answers
    submitted_ids = []
    for q in range(total_questions):
        selected = request.form.get(f"option_{q}")
        if selected:
            submitted_ids.append(selected)

    all_questions = []

    for q in range(total_questions):
        q_text = request.form.get(f"question_{q}")
        q_correct = request.form.get(f"correct_{q}")

        # Dynamically collect all options
        q_options = []
        j = 0
        while True:
            opt_id = request.form.get(f"q{q}_optid_{j}")
            opt_text = request.form.get(f"q{q}_opttext_{j}")
            if not opt_id or not opt_text:
                break
            q_options.append({"id": opt_id, "text": opt_text})
            j += 1

        all_questions.append({
            "question": q_text,
            "options": q_options,
            "correct": q_correct
        })

    # Calculate score
    score = 0
    results = []
    for q in all_questions:
        correct_id = q["correct"]
        selected_ids = [opt["id"] for opt in q["options"] if opt["id"] in submitted_ids]

        is_correct = len(selected_ids) == 1 and selected_ids[0] == correct_id
        if is_correct:
            score += 1

        results.append({
            "question": q["question"],
            "options": q["options"],
            "correct_id": correct_id,
            "selected_ids": selected_ids,
            "is_correct": is_correct
        })

    return render_template("result.html", score=score, total=total_questions, results=results)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
