
import pyttsx3
import wolframalpha
import speech_recognition

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wolframAlpha(query):
    apikey = "9H29E3-EJ8R9LXLR8"
    requester = wolframalpha.Client(apikey)   
    requested = requester.query(query) 

    try:
        answer = next(requested.results)
        return answer
    except:
        speak("The value is not answerable")
        
def calc(query):
    Term = str(query)
    Term = Term.replace("Jarvis","")
    Term = Term.replace("Plus","+")
    Term = Term.replace("Minus","-")
    Term = Term.replace("Multiply","*")
    Term = Term.replace("Divide","/")   
    Term = Term.replace("Cube","**3")   
    Term = Term.replace("Square","**2")
    
    
    Final = str(Term)
    try:
        result = wolframAlpha(Final)
        plaintext = result['subpod']['plaintext']
        print(f"Result: {plaintext}")
        speak(plaintext)
    except:
        speak("The value is not answerable")
 