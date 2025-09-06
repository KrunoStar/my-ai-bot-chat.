from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "HEAD"])
def home():
    if request.method == "HEAD":
        return "", 200  # Respond to HEAD requests with no error
    answer = None
    if request.method == "POST":
        question = request.form["question"]
        answer = f"You said: {question}"
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
