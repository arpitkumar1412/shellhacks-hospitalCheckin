import random
import speech_recognition as sr
import pandas as pd
from face_recog import image_capture

def appointment(aptmnt):
    data=-1
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        data_doctors = pd.read_csv(r'doctors.csv')
        while True:
            i = 1
            for doctor_name in data_doctors['Department']:
                print("{}. {}".format(i,doctor_name))
                i+=1
            print("You: ")
            audio = r.listen(source)
            try:
                data = int(r.recognize_google(audio))-1
                aptmnt['Doctor'] = data_doctors.iloc[data]['Department']
                aptmnt['Token'] = data_doctors.iloc[data]['Token_num']+1
                data_doctors.at[data, 'Token_num'] = aptmnt['Token']
                break
            except sr.UnknownValueError:
                print("Could not understand audio")

    data_doctors.to_csv('doctors.csv', index=False)
    return aptmnt

def check():
    r = sr.Recognizer()
    data = ""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        while True:
            audio = r.listen(source)
            try:
                data = r.recognize_google(audio)
                print(data)
                if data == "yes":
                    print("ComputerJi: {}".format('Your appointment has been confirmed, thank you and take care'))
                    break
            except sr.UnknownValueError:
                print("Could not understand audio")
                print("ComputerJi: {}".format("I didn't get that. Rerunning the code"))
    return data

def fake(aptmnt):
    return aptmnt
