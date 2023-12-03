from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import base64
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        if "audioData" not in request.form:
            return redirect(request.url)

        audio_data_url = request.form["audioData"]
        audio_data = base64.b64decode(audio_data_url.split(',')[1])

        recognizer = sr.Recognizer()
        audioFile = io.BytesIO(audio_data)
        
        with sr.AudioFile(audioFile) as source:
            data = recognizer.record(source)

        transcript = recognizer.recognize_google(data, key=None)

    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
