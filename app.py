import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime 
import pyjokes


def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeing...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not Understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':


    # if sptext().lower() == "hello jarvis":
        data1=sptext().lower()

        if "your name" in data1: 
            name = " my name is jarvis"
            speechtx(name)
        elif "old"  in data1:
            age = "I am two years old"
            speechtx(age)
        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com")
       
        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en",category="neutral")
            speechtx(joke_1)


    # else:
        # speechtx("Access Denied")


