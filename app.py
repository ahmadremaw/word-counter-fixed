from flask import Flask, render_template, request
from langdetect import detect
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    word_count = char_count = char_count_no_spaces = None
    detected_lang = corrected_text = None
    original_text = ""

    if request.method == "POST":
        original_text = request.form["text"]
        word_count = len(original_text.split())
        char_count = len(original_text)
        char_count_no_spaces = len(original_text.replace(" ", ""))
        
        # كشف اللغة
        try:
            detected_lang = detect(original_text)
        except:
            detected_lang = "غير معروفة"

        # تصحيح إملائي
        corrected_text = str(TextBlob(original_text).correct())

    return render_template(
        "index.html",
        word_count=word_count,
        char_count=char_count,
        char_count_no_spaces=char_count_no_spaces,
        detected_lang=detected_lang,
        corrected_text=corrected_text,
        original_text=original_text
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
