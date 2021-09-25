import random
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)

greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
questions = ['Please say your name', 'Please say your age', 'Please say your gender',
             'Please choose the index of the doctor you would like to see',
             'Please choose the index of the appointment most suitable for you']
confirm = ['Is this correct', 'Are you sure']


def start1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        engine.say(engine.say(random.choice(greetings)))
        engine.runAndWait()
        print("You: ")
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say("I didn't get that. Rerunning the code")
            engine.runAndWait()
            start1()


def start2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        for s in questions:
            engine.say(engine.say(s))
            engine.runAndWait()
            print("You: ")
            audio = r.listen(source)
            try:
                print(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
                engine.say("I didn't get that. Rerunning the code")
                engine.runAndWait()
                start2()


def start3():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        engine.say("Would you like to submit?")
        engine.runAndWait()
        print("You: ")
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio))
            if r.recognize_google(audio) == "yes":
                engine.say('Your appointment has been confirmed, thank you and take care')
                engine.runAndWait()
            else:
                engine.say('Would you like to fill the form again?')
                engine.runAndWait()
                print("You: ")
                audio = r.listen(source)
                try:
                    if r.recognize_google(audio) == "yes":
                        start1()
                    else:
                        engine.say("Thank you for visiting")
                        engine.runAndWait()
                except sr.UnknownValueError:
                    print("Could not understand audio")
                    engine.say("I didn't get that. Rerunning the code")
                    engine.runAndWait()
                    start3()
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say("I didn't get that. Rerunning the code")
            engine.runAndWait()
            start3()


start1()
start2()
start3()
