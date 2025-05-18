from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    word_count = None
    char_count = None
    if request.method == "POST":
        text = request.form["text"]
        word_count = len(text.split())
        char_count = len(text.replace(" ", ""))
    return render_template("index.html", word_count=word_count, char_count=char_count)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
