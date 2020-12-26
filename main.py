import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
listener= sr.Recognizer()
engine = pyttsx3.init()
# engine.say("Good Evening Sir. My self Licifer, I am alway's Prasent for your help.")
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.say("Good Evening Sir. My self sara, I am also Prasent for your help.")
# engine.runAndWait()

def talk(text):
    print(text)
    if "sara" in text:
        text=text.replace('sara','')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
    elif "lucifer" in text:
        text = text.replace('lucifer', '')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
    engine.runAndWait()
def take_command():

    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        print("say anything : ")
        try:
            audio = listener.listen(source)
            commend= listener.recognize_google(audio)
            commend=commend.lower()
            print(commend,"--------------?")
            #talk(commend)
        except:
            pass
        return commend

def run_AI():
    command = take_command()
    if 'play' in command:
        command = command.replace('play', '')
        pywhatkit.playonyt(command)
        talk('playing '+command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        if 'sara' in command:
            talk('Time is sara'+time)
        elif 'lucifer' in command:
            talk('Time is lucifer'+time)
run_AI()
