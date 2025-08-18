from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text")
    target_languages = data.get("targetLanguages", [])

    translations = []
    for lang in target_languages:
        try:
            translated_text = GoogleTranslator(source="auto", target=lang).translate(text)
            translations.append({"language": lang, "translatedText": translated_text})
        except Exception as e:
            translations.append({"language": lang, "translatedText": f"Error: {str(e)}"})

    return jsonify(translations)

if __name__ == "__main__":
    app.run(debug=True)
