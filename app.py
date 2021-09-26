from flask import Flask, render_template, request
from face_recog import image_capture
import speech_recognition as sr
import time
from speech import appointment, check, fake
import pandas as pd

app = Flask(__name__)
app.static_folder = 'static'

questions = ['Hey there', 'Please choose the index of the doctor you would like to see', 'Is this correct']

aptmnt = {'Name':None,
        'Age':None,
        'Sex':None,
        'Doctor':None,
        'Token':None
        }

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

@app.route("/home")
def welcome():
    return render_template("welcome.html")

@app.route("/face_recognizer")
def face():
    val, person = image_capture(2,3)
    global aptmnt
    print(person['Name'])
    aptmnt['Name'] = person['Name']
    aptmnt['Age'] = person['Age']
    aptmnt['Sex'] = person['Sex']
    print(aptmnt['Name'])
    return render_template("face.html", val=val, person=person)

@app.route("/chatbot_q_0")
def chatbot_0():
    return render_template("chat.html", data = questions[0], type=0)

@app.route("/chatbot_r_0")
def chatbot_r_0():
    ans = get_voice()
    return render_template("chat_r.html", data = ans, type="voice")

@app.route("/chatbot_q_1")
def chatbot_1():
    data_doctors = pd.read_csv(r'doctors.csv')
    doctors = data_doctors['Department'].values.tolist()
    return render_template("chat.html", data = questions[1], type=1, doctors=doctors)

@app.route("/chatbot_r_1")
def chatbot_r_1():
    global aptmnt
    val_aptmnt = appointment(aptmnt)
    return render_template("chat_r.html", data = val_aptmnt['Doctor'], type="appointment")

@app.route("/chatbot_q_2")
def chatbot_2():
    return render_template("chat.html", data = questions[2], type=2, aptmnt = aptmnt)

@app.route("/chatbot_r_2")
def chatbot_r_2():
    ans = check()
    return render_template("chat_r.html", data = ans, type="check")

@app.route("/final")
def last():
    global aptmnt
    return render_template("result.html", data = aptmnt)

if __name__ == "__main__":
    app.run(debug=True)
