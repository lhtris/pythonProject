import pyttsx3

AI_brain = "Hello World"

AI_mouth = pyttsx3.init()
AI_mouth.say(AI_brain)
AI_mouth.runAndWait()