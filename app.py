from flask import Flask, render_template, request
from face_recog import image_capture
import speech_recognition as sr

app = Flask(__name__)
app.static_folder = 'static'

questions = ['Hey there', 'Please say your name', 'Please say your age', 'Please say your sex', 'Please choose the index of the doctor you would like to see', 'Is this correct']

def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)
        try:
            data = r.recognize_google(audio)
        except sr.UnknownValueError:
            data = "Could not understand audio"
    return data

app.jinja_env.globals.update(get_voice=get_voice)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/face_recognizer")
def face():
    # val, person = image_capture(3,4)
    person = {'Name': "Arpit",
              'Age': 21,
              'Sex': 'm'}
    return render_template("face.html", val=1, person=person)

@app.route("/chatbot")
def chatbot():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)
