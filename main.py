import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def  record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            jarvis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            jarvis_speak('sorry, i did not get that')
        except sr.RequestError:
            jarvis_speak('Sorry, my speech service is dowm')
        return voice_data


def jarvis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 100000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if 'what is your name' in voice_data:
        jarvis_speak('my name is Scarlett')
    if 'how are you' in voice_data:
        jarvis_speak('i am doing great how can i help you')
    if 'tell me a joke' in voice_data:
        jarvis_speak('i suggest you look in the mirror')
    if 'what can you do' in voice_data:
        jarvis_speak('i can search anything, open apps, play music, ')
    if 'watch something' in voice_data:
        url = 'https://www.netflix.com/browse'
        webbrowser.get().open(url)
        jarvis_speak ('hope you like it')
    if 'what time is it' in voice_data:
        jarvis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you wat to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        jarvis_speak ('here is what I found on ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        jarvis_speak('here is the location of ' + location)
    if 'thanks' in voice_data:
        jarvis_speak('your welcome')
        exit()
    if 'start editing' in voice_data:
        os.system("open /Applications/iMovie.app")
        jarvis_speak('good luck')
    if 'open chat' in voice_data:
        os.system("open /Applications/WhatsApp.app")
        jarvis_speak('have fun')
    if 'play something' in voice_data:
        os.system("open /Applications/Spotify.app")
        jarvis_speak('happy listening')



time.sleep(1)
jarvis_speak('how can i help you boss')
while 1:
    voice_data = record_audio()
    respond(voice_data)

from flask import Flask,render_template

main = Flask(__name__)

@main.route("/")
@main.route("/home")
def home ():
    return render_template("index.html")

if __name__ == '__main__':
    main.run(debug= True,port=5001)

