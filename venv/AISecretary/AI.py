import speech_recognition
import pyttsx3
from datetime import date, datetime

AI_ear = speech_recognition.Recognizer()
AI_mouth = pyttsx3.init()
voices = AI_mouth.getProperty('voices')
AI_mouth.setProperty('voice', voices[1].id)
AI_brain = ""

while True:

    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = AI_ear.record(mic, duration=3)
    try:
        you = AI_ear.recognize_google(audio)
    except:
        you = ""

    if you == "":
        AI_brain = "Sorry. I can't hear you."
    elif "hi" in you or "hello" in you:
        AI_brain = "Hello Tri"
    elif "today" in you:
        today = date.today()
        AI_brain = today.strftime("%b-%d-%Y")
    elif "time" in you:
        now = datetime.now()
        AI_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        AI_brain = "Goodbye"
        print(AI_brain)
        AI_mouth.say(AI_brain)
        AI_mouth.runAndWait()
        break
    else:
        AI_brain = "How can I help you?"

    print(AI_brain)
    AI_mouth.say(AI_brain)
    AI_mouth.runAndWait()