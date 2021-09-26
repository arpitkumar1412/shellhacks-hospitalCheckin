from flask import Flask, render_template, request
from face_recog import image_capture

app = Flask(__name__)
app.static_folder = 'static'

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

@app.route("/face_recognizer")
def chatbot():
    # val, person = image_capture(3,4)
    person = {'Name': "Arpit",
              'Age': 21,
              'Sex': 'm'}
    return render_template("face.html", val=1, person=person)

if __name__ == "__main__":
    app.run(debug=True)
