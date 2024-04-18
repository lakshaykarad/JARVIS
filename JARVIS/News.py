
import requests
import json
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# apidict = {
#     "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4df1cba33ba549c395b9f7fe83969b74",
#     "Entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4df1cba33ba549c395b9f7fe83969b74",
#     "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=4df1cba33ba549c395b9f7fe83969b74",
#     "Sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4df1cba33ba549c395b9f7fe83969b74",
#     "Technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=4df1cba33ba549c395b9f7fe83969b74",
#     "Science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4df1cba33ba549c395b9f7fe83969b74"
#     "IPL": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4df1cba33ba549c395b9f7fe83969b74"
# }
apidict = {
    "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4df1cba33ba549c395b9f7fe83969b74",
    "Entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4df1cba33ba549c395b9f7fe83969b74",
    "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=4df1cba33ba549c395b9f7fe83969b74",
    "Sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4df1cba33ba549c395b9f7fe83969b74",
    "Technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=4df1cba33ba549c395b9f7fe83969b74",
    "Science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4df1cba33ba549c395b9f7fe83969b74",
    "IPL": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4df1cba33ba549c395b9f7fe83969b74"
}

content = None
url = None

# speak("Which field news do you want? [Business], [Entertainment], [Sports], [Technology], [Health]")

field = input("Type field name that you want: ")

found_url = False
for key, value in apidict.items():
    if key.lower() in field.lower():
        url = value
        print(url)
        print("URL was found")
        found_url = True
        break

if not found_url:
    print("URL not found")
else:
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here the first news is: ")
    
    articles = news["articles"]
    for article in articles:
        title = article["title"]
        print(title)
        speak(title)
        news_url = article["url"]
        print(f"For more information visit: {news_url}")
        
        a = input("[press Y to continue] and [press N to stop]")
        if a.lower() == 'y':
            pass
        elif a.lower() == 'n':
            break
        speak("That's all")
