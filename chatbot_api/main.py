import random
import pyttsx3
import speech_recognition as sr
import pandas as pd

greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
questions = ['Please say your name', 'Please say your age', 'Please say your sex']
appointment = ['Please choose the index of the doctor you would like to see']
confirm = ['Is this correct', 'Are you sure']


def start1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("ComputerJi: {}".format(random.choice(greetings)))
        print("You: ")
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            start1()


def start2(aptmnt):
    for s in questions:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            while True:
                print("ComputerJi: {}".format(s))
                print("You: ")
                audio = r.listen(source)
                try:
                    data = r.recognize_google(audio)
                    print(data)
                    if 'name' in s:
                        aptmnt['Name'] = data
                    elif 'age' in s:
                        aptmnt['Age'] = data
                    elif 'sex' in s:
                        aptmnt['Sex'] = data
                    break
                except sr.UnknownValueError:
                    print("Could not understand audio")
                    print("ComputerJi: {}".format("I didn't get that. Rerunning the code"))

    return aptmnt

def start3(aptmnt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        data_doctors = pd.read_csv(r'../doctors.csv')
        while True:
            print("ComputerJi: {}".format(appointment[0]))
            i = 1
            for doctor_name in data_doctors['Department']:
                print("{}. {}".format(i,doctor_name))
                i+=1
            print("You: ")
            audio = r.listen(source)
            try:
                data = int(r.recognize_google(audio))-1
                print(data)
                aptmnt['Doctor'] = data_doctors.iloc[data]['Department']
                aptmnt['Token'] = data_doctors.iloc[data]['Token_num']+1
                data_doctors.at[data, 'Token_num'] = aptmnt['Token']
                break
            except sr.UnknownValueError:
                print("Could not understand audio")

        data_doctors.to_csv('../doctors.csv', index=False)

        while True:
            print("ComputerJi: {}".format('Would you like to submit?'))
            print(aptmnt)
            print("You: ")
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

    return aptmnt

aptmnt = {'Name':None,
        'Age':None,
        'Sex':None,
        'Doctor':None,
        'Token':None
        }
# start1()
# aptmnt = start2(aptmnt)
aptmnt = start3(aptmnt)
print(aptmnt)
