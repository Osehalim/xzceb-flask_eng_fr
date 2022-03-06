import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(text_to_translate):
    textToTranslate = request.args.get('text_to_translate')
    # Write your code here
    translated_text_to_french = language_translator.translate(
    text = text_to_translate,
    model_id='en-fr').get_result()
    return translated_text_to_french

@app.route("/french_to_english")
def frenchToEnglish(text_to_translate):
    text_to_translate = request.args.get('text_to_translate')
    # Write your code here
    translated_text_to_english = language_translator.translate(
    text = text_to_translate,
    model_id='fr-en').get_result()
    return translated_text_to_english

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html') 
        if __name__ == "__main__":
            app.run()
        if __name__ == "__main__":
            app.run(host="0.0.0.0", port=8080)
