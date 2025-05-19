from flask import Flask, render_template, request
from langdetect import detect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    word_count = char_count = language = None
    if request.method == "POST":
        text = request.form["text"]
        word_count = len(text.split())
        char_count = len(text)
        try:
            language = detect(text)
        except:
            language = "غير معروفة"
    return render_template("index.html", text=text, word_count=word_count, char_count=char_count, language=language)

@app.route("/about")
def about():
    return render_template("pages/about.html")

@app.route("/contact")
def contact():
    return render_template("pages/contact.html")

@app.route("/privacy")
def privacy():
    return render_template("pages/privacy.html")

@app.route("/terms")
def terms():
    return render_template("pages/terms.html")

if __name__ == "__main__":
    app.run(debug=True)
