you = "hello"

if you == "":
    AI_brain = "Sorry. I can't hear you."
elif "hello" in you:
    AI_brain = "Hello"
elif you == "today":
    AI_brain = "Thursday"
else:
    AI_brain = "How can I help you?"

print(AI_brain)