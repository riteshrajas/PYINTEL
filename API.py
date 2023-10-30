from package_import import *
import requests
from bs4 import BeautifulSoup
class Declaration():
    wikipedia.set_lang("en")
    json_file_path = r"P:\PYINTEL_3.0\Utility\Pyintel_data\user_info.json"
    speech_engine = pyttsx3.init("sapi5")
    today = datetime.date.today()
    data = trainingData.get_data()
    time = time.strftime("%I:%M %p")
    Answer_Questions = {item[0]: item[1] for item in data[0]['conversations']}
    database = Server.Database()
    nodata_response = "I'm sorry, but I don't have that information right now. However, I'll make sure to record your question for future reference. Thank you for understanding, and sorry for any inconvenience caused."
    # Telegrammer.wait_until_receive_message()

with open(Declaration.json_file_path) as json_file:
    data = json.load(json_file)
    Username = data["name"]
    Age = data["age"]
    Gender = data["gender"]
    Email = data["email"]
    Phone = data["phone"]  
    Address = data["address"]

def speak(text):
    Declaration.speech_engine.say(text)
    Declaration.speech_engine.runAndWait()
    return text

def greetings():
    # speak(f"Hello {Username}, Currently Starting Services")
    speak("hi")
    
def get_answer(question):
    best_match = max(Declaration.Answer_Questions.keys(), key=lambda ques: similarity.getSimilarity(question.lower(), ques.lower()))
    similarity_score = similarity.getSimilarity(question.lower(), best_match.lower())
    answer = Declaration.Answer_Questions[best_match]
    return answer, similarity_score, best_match

def process_user_input(user_input):
    if "/start" in user_input:
        Telegrammer.send_message(f"Hello {Telegrammer.get_Username()}, Currently Starting Services")
        Telegrammer.send_message("I am a bot that can help you with your daily tasks. I am still under development, so please be patient. Thank you for your patience.")
        Telegrammer.send_message("As of now, I can do these things: \n  1.Search Stocks \n 2. Summarise your text \n 3. Open a website \n 4. Search in Google \n 5. Search in Bing \n 6. Search in DuckDuckGo \n 7. Search in Wikipedia \n 8. Search in Stackoverflow \n 9. Play Songs \n10. Take Pictures \n11. Record Video \n12. Record Audio \n13. Send Mail \n14. Create Events")
        return None
        
        
        
    if "/identify" in user_input:
        return Declaration.database.post(user_input, "identify", speak(Telegrammer.send_message(patternIdentifier.identify(user_input))))
    elif "/summarise_this" in user_input:
        return Telegrammer.send_message(Declaration.database.post("Too large Paragraph", "Summary_feature", models.Summarizers(user_input.replace("/search_in_google", ""))))
    elif "/open" in user_input:
        website = Declaration.database.post(user_input, "Web_App_Open_feature", speak(Telegrammer.send_message(patternIdentifier.identify(user_input))))
        webbrowser.open(str(website))
        return website
    elif "/google_it" in user_input:
        soup = str(f"https://www.google.com/search?q={str(user_input.replace('/google_it ', ''))}")
        SOUP = BeautifulSoup(requests.get(soup).content, "html.parser")
        
        return Declaration.database.post(user_input, "Search_in_google_feature", SOUP.find("div",class_ = "BNeawe"))
    elif "/search_in_google" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_google_feature",str(f"https://www.google.com/search?q={str(user_input.replace('/search_in_google ', ''))}")))
    elif "/search_in_bing" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Bing_feature",str(f"https://www.bing.com/search?form=&q={str(user_input.replace('/search_in_bing ', ''))}")))
    elif "/search_in_ddg" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_DuckDuckGo_feature",str(f"https://duckduckgo.com/?q={str(user_input.replace('/search_in_ddg ', ''))}")))
    elif "/search_in_stackoverflow" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Stackoverflow_feature",str(f"https://stackoverflow.com/search?q={str(user_input.replace('/search_in_stackoverflow ', ''))}")))
    elif "/search_in_amazon" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Amazon_feature",str(f"https://www.amazon.com/s?k={str(user_input.replace('/search_in_amazon ', ''))}")))
    elif "/search_in_reddit" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Reddit_feature",str(f"https://www.reddit.com/search/?q={str(user_input.replace('/search_in_reddit ', ''))}")))
    elif "/search_in_wikipedia" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_wikipedia_feature",str(f"https://en.wikipedia.org/wiki/{str(user_input.replace('/search_in_wikipedia ', ''))}")))
    elif "/search_in_google Maps" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Google_Maps_feature",str(f"https://www.google.com/maps/search/{str(user_input.replace('/search_in_google_maps ', ''))}")))
    elif "/search_in_images" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Google_Images_feature",str(f"https://www.google.com/search?tbm=isch&q={str(user_input.replace('/search_in_google_images ', ''))}")))
    elif "/search_in_youtube" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_YouTube_feature",str(f"https://www.youtube.com/results?search_query={str(user_input.replace('/search_in_youtube ', ''))}")))
    elif "/search_in_bing_maps" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Bing_Maps_feature",str(f"https://www.bing.com/maps?q={str(user_input.replace('/search_in_bing_maps ', ''))}")))
    elif "/search_in_google_books" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Google_Books_feature",str(f"https://www.google.com/books?q={str(user_input.replace('/search_in_google_books ', ''))}")))
    elif "/search_in_walmart" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Walmart_feature",str(f"https://www.walmart.com/search?query={str(user_input.replace('/search_in_walmart ', ''))}")))
    elif "/search_in_flipkart" in user_input:
        webbrowser.open(Declaration.database.post(user_input,"Search_in_Flipkart_feature",str(f"https://www.flipkart.com/search?q={str(user_input.replace('/search_in_flipkart ', ''))}")))
    elif "/stock_of" in user_input:
        return(Declaration.database.post(user_input,"Stock_feature",speak(Telegrammer.send_message(tools.get_stock(user_input.replace("/stock_of ", ""))))))
    elif "/wiki" in user_input:
        return(Declaration.database.post(user_input,"wiki_feature",speak(Telegrammer.send_message(wikipedia.summary(str(user_input.replace("/wiki ", "")), sentences=2)))))
    elif "/take_picture" in user_input:
        return(Declaration.database.post(user_input,"Take_Picture_feature",speak(Telegrammer.send_message_image(tools.take_picture()))))
    elif "/record_audio_for" in user_input:
        return(Declaration.database.post(user_input,"Record_audio_feature",speak(Telegrammer.send_message_audio(tools.record_audio(user_input.replace("/record_audio_for ", ""))))))  
    elif "/play_song_called" in user_input:
        return(Declaration.database.post(user_input,"Play_song_feature",webbrowser.open(Telegrammer.send_message(tools.play_song(user_input.replace("/play_song_called ", ""))))))
    elif "/take_video_for" in user_input:
        return(Declaration.database.post(user_input,"Take_Video_feature",speak(Telegrammer.send_message_video(tools.record_video(int(user_input.replace("/take_video_for ", "")))))))
    elif "/send_a_mail" in user_input:
        To_email = (patternIdentifier.identify(user_input)).pop(0) # type: ignore                                        
        speak("What is the subject of the mail?");subject = Telegrammer.check_messages()
        speak("What is the message of the mail?");body = Telegrammer.check_messages()
        tools.Send_email(To_email,subject,body)
        return(Declaration.database.post(user_input,f"Send Email to {To_email}",Telegrammer.send_message(f"----Email Query from {Username}---- \n\n To: {To_email} \n\n Subject: {subject} \n\n Body:\n    {body}")))
    elif "/create_a_calender_event" in user_input:
        speak("What is the event name?");Event_name = Telegrammer.check_messages()
        speak("when is it gonna happen?");Event_date = Telegrammer.check_messages()
        speak("what is it about,  I am pretty interested");Event_description = Telegrammer.check_messages()
        return(Declaration.database.post(user_input,"Create_calender_event_feature",speak(Telegrammer.send_message(tools.Create_Event(Event_date,Event_name,Description=Event_description)))))
        
    else:
        answer, similarity_score, best_match = get_answer(user_input)

        if similarity_score < 0.5:
            return Declaration.nodata_response
        else:
            if re.search("#Time#", answer):
                answer = answer.replace("#Time#", Declaration.time)
            if re.search("#joke#", answer):
                answer = answer.replace("#joke#", tools.get_jokes())
            if re.search("#weather_temperature", answer):
                answer = answer.replace("#weather_temperature#", Climate.WeatherService().current_weather()['Temperature (°C)'])
            if re.search("#weather_condidtion#", answer):
                answer = answer.replace("#weather_condidtion#", str(Climate.WeatherService().current_weather_condition()))
            return answer
        

if __name__ == "__main__":
    greetings()
    while True:
        try:
            while True:
                user_input = str(Telegrammer.get_message())
                print(user_input)
                result = process_user_input(user_input)
                if result is not None:
                    print(Telegrammer.send_message(result))
                continue
        except Exception as e:
            print(Telegrammer.send_message(f"Error: {e}"))
            continue