import pyttsx3
AI_mouth = pyttsx3.init()

voices = AI_mouth.getProperty('voices')
AI_mouth.setProperty('voice', voices[1].id)
AI_brain = "Hello World"
AI_mouth.say(AI_brain)
AI_mouth.runAndWait()