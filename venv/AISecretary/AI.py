import speech_recognition
import pyttsx3
from datetime import date, datetime

AI_ear = speech_recognition.Recognizer()
AI_mouth = pyttsx3.init()
AI_brain = ""
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = AI_ear.listen(mic)
try:
    you = AI_ear.recognize_google(audio)
except:
    you = ""


if you == "":
    AI_brain = "Sorry. I can't hear you."
elif you == "hello":
    AI_brain = "Hello Tri"
elif you == "today":
    today = date.today()
    AI_brain = today.strftime("%b-%d-%Y")
elif you == "time":
    now = datetime.now()
    AI_brain = now.strftime("%H hours %M minutes %S seconds")
else:
    AI_brain = "How can I help you?"

print(AI_brain)

AI_mouth.say(AI_brain)
AI_mouth.runAndWait()