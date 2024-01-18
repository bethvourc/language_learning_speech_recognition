from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_audio', methods=['POST'])
def analyze_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'})

    audio_file = request.files['audio']
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return jsonify({'text': text})
    except sr.UnknownValueError:
        return jsonify({'error': 'Speech recognition could not understand the audio'})
    except sr.RequestError as e:
        return jsonify({'error': f'Speech recognition request failed: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
