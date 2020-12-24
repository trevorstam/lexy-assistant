import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes

from skills import get_current_time, get_current_date

# listener
listener = sr.Recognizer()

# text to speech engine initialization
engine = pyttsx3.init()

# get all different voices from pyttsx3 engine
voices = engine.getProperty('voices') 
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.karen')

def receive_command():
    try:
        with sr.Microphone() as source:
            print('...listening')
            voice = listener.listen(source) 
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lexi' in command:
                command = command.replace('lexi', '')
                print(command)
                return command
    except:
        pass
    #return command

def speak_lexi(responseText):
    engine.say(responseText)
    engine.runAndWait()

def run_lexi():
    command = receive_command()
    print(command)

    if 'time' in command:
        time = get_current_time()
        speak_lexi(f'The current time is {time}')
    elif 'date' in command:
        current_date = get_current_date()
        speak_lexi(f'Today is {current_date}')
    elif 'play' in command:
        video = command.replace('play', '')
        speak_lexi(f'playing {video}')
        pywhatkit.playonyt(video)
    elif 'joke' in command:
        speak_lexi(pyjokes.get_joke())
    else:
        speak_lexi('Sorry I did not get that')



if __name__ == "__main__":
    while True:
        run_lexi()

