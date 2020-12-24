import speech_recognition as sr
import pyttsx3
listener= sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.say("Good Evening Sir. My self Licifer, I am alway's Prasent for your help.")
    engine.runAndWait()

with sr.Microphone() as source:
    listener.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
    print("say anything : ")

    try:
        audio = listener.listen(source)
        commend= listener.recognize_google(audio)

        commend=commend.lower()
        if "licifer" in commend:
            print(commend)
    except:
        pass
