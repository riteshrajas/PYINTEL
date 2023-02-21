import datetime
import smtplib
import openai
import pyttsx3
import speech_recognition as sr

#############################################################################################
# Setting up the AI
Username = "YOUR_NAME"
UsersEmail = "YOUR_EMAIL"
UsersPwd = "YOUR_PASSWORD"
openai.api_key = 'YOUR_OPENAI_API_KEY'
#############################################################################################
# Setting up Voice of the AI
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#############################################################################################
# Set up email details
receiver_email = "RECIVER EMAIL"
subject = "Test email"
body = "This is a test email sent from Python."
#############################################################################################
# Set up SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587
message = f"From: {UsersEmail}\nTo: {receiver_email}\nSubject: {subject}\n\n{body}"


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
    speak(f"Hello Reateashh...(PRONONCE YOUR NAME) , How can I help you?")
    print(f"Hello {Username} , How can I help you?")
    while True:
        question = takecommand().lower()
        if 'what is the time' in question:
            TIME = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {TIME}")
            print(TIME)
        elif 'search' in question:
            queue = question.split("search")[1]
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=queue,
                temperature=0.7,
                max_tokens=64,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            print(queue)
            print(f"Answer: {response.choices[0].text}")
            speak(response.choices[0].text)
        elif 'send email' in question:
            speak("What is the subject about")

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(Username, UsersPwd)
                server.sendmail(UsersEmail, receiver_email, message
                                )
