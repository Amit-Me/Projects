import pyttsx3

start = pyttsx3.init()               # To initialize pyttsx3

start.setProperty("rate",160)        # To set speed of speech

start.say("Hi")
start.say("Welcome Back Sir")
start.say("It's very long to see you again")

start.runAndWait()