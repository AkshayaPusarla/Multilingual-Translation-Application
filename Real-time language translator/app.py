from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)

# Initialize the translator
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Parse the incoming JSON payload
        data = request.get_json()
        source_lang = data.get('source_lang')
        target_lang = data.get('target_lang')
        input_text = data.get('text')

        # Validate inputs
        if not input_text or not target_lang:
            return jsonify({"error": "Invalid input"}), 400

        # Translate the input text
        translation = translator.translate(input_text, src=source_lang, dest=target_lang)
        translated_text = translation.text

        # Respond with the translated text
        return jsonify({"translated_text": translated_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
