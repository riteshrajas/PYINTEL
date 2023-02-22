from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import speech_recognition as sr
import pyttsx3

# Set up the chatbot and its training
bot = ChatBot(
    'PYINTEL Beta',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }
    ],
    database_uri='sqlite:///database.db'
)

trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot on the English corpus and the TimeLogicAdapter
trainer.train("chatterbot.corpus.english")
#trainer.train("chatterbot.corpus.time")

# Load additional training data from a JSON file
trainer.train("./trainingfile_indent.json")

# Set up text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Set up speech recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Greet the user


def greet_user():
    speak("Hello Ritesh, how can I help you?")
    print("Hello Ritesh, how can I help you?")

# Convert speech to text


def transcribe_speech():
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language='en-US')
        print(f"Ritesh said: {text}")
        return text
    except Exception as e:
        print(f"Error: {str(e)}")
        speak("I'm sorry, I didn't catch that.")
        return ""

# Convert text to speech


def speak(text):
    engine.say(text)
    engine.runAndWait()


# Run the chatbot
if __name__ == "__main__":
    greet_user()
    while True:
        user_input = transcribe_speech().lower()
        if user_input:
            response = bot.get_response(user_input)
            print(response)
            speak(str(response))
