import datetime
import chatterbot
import pyttsx3
import speech_recognition as sr
import smtplib
import requests

Username = "Ritesh"
UsersEmail = "YOUR_EMAIL"
UsersPwd = "helo"
#openai.api_key = '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'
#############################################################################################
# Setting up Voice of the AI
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#############################################################################################
# Set up email details
receiver_email = "code.ritesh@gmail.com"
subject = "Heelo"
body = "BODY"
sender_email = UsersEmail

#############################################################################################
# Set up SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587




#############################################################################################
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#############################################################################################
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        questionquiery = r.recognize_google(audio, language='en-us')
        print(f"{Username} said: {questionquiery}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return questionquiery


#############################################################################################
if __name__ == "__main__":
    speak(f"Hello Reateashh... , How can I help you?")
    print(f"Hello {Username} , How can I help you?")
    while True:
        question = takecommand().lower()
        if 'what is the time' in question:
            TIME = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {TIME}")
            print(TIME)
        elif 'send email' in question:
            speak("What is the body of the mail")
            print("What is the body of the mail?")
            BODY = takecommand()
            SUBJECT = takecommand()
            message = f"From: {sender_email}\nTo: {receiver_email}\nSubject: {subject}\n\n{body}"
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(UsersEmail, UsersPwd)
                server.sendmail(UsersEmail, receiver_email, message)
                print(f"Email Sent to {receiver_email}")
        elif 'current weather ' in question:
            api_key = "a0a54ca0ca899a7eda2059c8de6e1d0a"
            city_name = "New York"
            url = f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=a0a54ca0ca899a7eda2059c8de6e1d0a"
            response = requests.get(url)
            print(f"The temperature in {city_name} is {main['main']['temp']} degrees Celsius.")
