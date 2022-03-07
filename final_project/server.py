import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(text_to_translate):
    text_to_translate = request.args.get('text_to_translate')
    translated_text_to_french = english_to_french(text_to_translate)
    return translated_text_to_french

@app.route("/french_to_english")
def frenchToEnglish():
    text_to_translate = request.args.get('text_to_translate')
    translated_text_to_english = french_to_english(text_to_translate)
    return translated_text_to_english

@app.route("/")
def renderIndexPage():
    return render_template('index.html') 
        
if __name__ == "__main__":
    app.run(debug=True)
        
