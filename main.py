import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
listener= sr.Recognizer()
engine = pyttsx3.init()
hour = datetime.datetime.now().hour

print(hour)
prods=''
if ((hour < 4) & (hour > 8 )):
    prods = 'Early Morning'
elif ((hour< 8) & (hour > 12 )):
    prods = ' Good Morning'
elif ((hour < 12) & (hour > 16 )):
    prods = 'Good afterNoon'
elif ((hour < 16) & (hour > 20 )):
    prods = 'Good Evening'
elif ((hour < 20) & (hour > 24 )):
    prods = 'Hello'
else:
    prods = "Hello"
greeting = prods
engine.say(f"{greeting} Sir. My self Licifer, I am alway's Prasent for your help.")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say(f"{greeting} Sir. My self sara, I am also Prasent for your help.")
engine.runAndWait()

def talk(text):
    print(text)
    if "sara" in text:
        text=text.replace('sara','')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
    else:
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
            commend=''
            commend= listener.recognize_google(audio)
            commend=commend.lower()
            print(commend,"--------------?")
            # if 'say' in commend:
            #     talk(commend)
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
        else:
            talk('Time is lucifer'+time)
    elif 'terminate' in command:
        return 0
    elif 'are you there' in command:
        if "sara" in command:
            text = "Alway's prasent for you Sir."
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
        else:
            text = "Alway's prasent for you Sir."
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
        engine.runAndWait()
    else:
        talk(command)
    return 1

a=1
while (a):
    if a==2:
        break
    a=run_AI()
