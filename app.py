from flask import Flask, render_template, request
from langdetect import detect
from spellchecker import SpellChecker
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    word_count = None
    char_count = None
    language = None
    misspelled = []
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        word_count = len(text.split())
        char_count = len(text.replace(" ", ""))
        try:
            language = detect(text)
        except:
            language = "غير معروف"

        # التدقيق الإملائي للإنجليزية فقط حالياً
        if language == "en":
            spell = SpellChecker()
            misspelled = spell.unknown(text.split())

    return render_template("index.html", word_count=word_count, char_count=char_count,
                           language=language, text=text, misspelled=misspelled)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
