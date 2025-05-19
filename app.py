from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    word_count = char_count = None
    if request.method == "POST":
        text = request.form["text"]
        word_count = len(text.split())
        char_count = len(text)
    return render_template("index.html", word_count=word_count, char_count=char_count)

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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)