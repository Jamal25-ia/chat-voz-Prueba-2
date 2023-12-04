from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files['audio']

    # Asegúrate de que la carpeta 'temp' exista en el directorio de la aplicación
    temp_folder = os.path.join(os.getcwd(), 'temp')
    os.makedirs(temp_folder, exist_ok=True)

    # Guarda el archivo en el sistema de archivos temporal
    audio_path = os.path.join(temp_folder, 'audio.wav')
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    transcription = recognizer.recognize_google(audio_data, language='es-ES')

    # Elimina el archivo temporal después de procesarlo
    os.remove(audio_path)

    return jsonify({'transcription': transcription})

if __name__ == '__main__':
    app.run(debug=True)








"""
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

"""