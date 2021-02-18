import speech_recognition

AI_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = AI_ear.listen(mic)
try:
    you = AI_ear.recognize_google(audio)
except:
    you = ""
print("YOu" + you)