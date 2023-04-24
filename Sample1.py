import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import time as t
import random
#import socket

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
p1 = 308.94567581453
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning!')

    elif hour >= 12 and hour < 16:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am buddy, sir Please enter the pin to help you')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 0.5
        r.energy_threshold = 350
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print('Recognizing.......')
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception:
        print ('say that again please......')
        return 'None'
    return query

x = (pow(p1, 2) / 951236874)

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maxwelljohn123123@gmail.com', 'qwerty0987!@#$')
    server.sendmail('maxwelljohn123123@gmail.com', to, content)
    server.close()

voice_num = 0
buddy = int(pow(x * 951236874, 2))


if __name__ == '__main__':
    wishme()
    print ('please enter the pin: ')
    while True:
        random_pin = random.randint(1000, 9999)
        email_id = 'maxwellj821@gmail.com'
        sendemail(email_id , str(random_pin))
        entered_pin = input()
        try:
            entered_pin = int(entered_pin)
        except:
            print('invalid input, enter only 4 digit pin')
            continue

        if entered_pin == buddy or entered_pin == random_pin:
            speak('sir, please tell me how may i help you?')
            while True:
                query = takeCommand().lower()
                if 'wikipedia' in query:
                    speak('searching wikipedia.....')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak('According to wikpedia')
                    print (results)
                    speak(results)

                elif 'open youtube' in query:
                    webbrowser.open('youtube.com')

                elif 'open google' in query:
                    webbrowser.open('google.com')

                elif 'open amazon' in query:
                    webbrowser.open('amazon.in')

                elif 'open flipkart' in query:
                    webbrowser.open('flipkart.com')

                elif 'stack overflow ' in query:
                    webbrowser.open('stackoverflow.com')

                elif 'github' in query:
                    webbrowser.open('githhub.com')

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime('%H:%M:%S')
                    print('sir, the time is ', strTime)
                    speak('sir, the time is ')
                    speak(strTime)

                elif 'date' in query:
                    strDate = datetime.datetime.now().strftime("%A %d. %B %Y")
                    print('sir, the date is ', strDate)
                    speak('sir, the date is ')
                    speak(strDate)

                elif 'open code' in query:
                    codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
                    os.startfile(codepath)

                elif 'open spotify' in query:
                    codepath = "C:\Users\91911\AppData\Roaming\Spotify\Spotify.exe"
                    os.startfile(codepath)

                elif 'play some song' in query:
                    codepath = "C:\Users\91911\AppData\Roaming\Spotify\Spotify.exe"
                    os.startfile(codepath)

                elif 'mail to anonymous' in query:
                    try:
                        speak('what should i say')
                        content = takeCommand()
                        to = 'maxwellj821@gmail.com'
                        sendemail(to, content)
                        speak('email has been sent!')
                    except Exception as e:
                        print (e)
                        speak('sorry my friend. I am not able to send this email')

                elif 'in google' in query:
                    taburl = 'https://google.com/?#q='
                    query = query.replace("in google", "")
                    query = query.replace('search', '')
                    webbrowser.open(taburl + query)

                elif 'in youtube' in query:
                    taburl = 'https://www.youtube.com/results?search_query='
                    query = query.replace("in youtube", "")
                    query = query.replace('search', '')
                    webbrowser.open(taburl + query)

                elif 'in amazon' in query:
                    taburl = 'https://www.amazon.in/s?k='
                    query = query.replace("in amazon", "")
                    query = query.replace('search', '')
                    webbrowser.open(taburl + query)

                elif 'in flipkart' in query:
                    taburl = 'https://www.flipkart.com/search?q='
                    query = query.replace("in flipkart", "")
                    query = query.replace('search', '')
                    webbrowser.open(taburl + query)

                elif 'weather' in query:
                    webbrowser.open('https://openweathermap.org/city/1264592')

                elif 'what is your age ' in query:
                    current_time = t.localtime().tm_year
                    if current_time == 2020:
                        speak('i am not an year old')
                        print('i am not an year old')
                        # time_created=1592626785.5378294
                    else:
                        speak('i am ', current_time, 'year old')

                elif 'how old are you' in query:
                    current_time = t.localtime().tm_year
                    if current_time == 2020:
                        speak('i am not an year old')
                        print('i am not an year old')
                    else:
                        speak('i am ', current_time, 'year old')

                elif 'current news' in query:
                    taburl = (
                        'https://newsapi.org/v2/top-headlines?country=in&apiKey=2a97c9472a8144daaa9736da0eb8e9df')
                    results = requests.get(taburl).json()
                    for x in range(0, 10):
                        num = random.randint(0, 15)
                        news = results['articles'][num]['title']
                        print (str(x + 1) + ' - ' + news)
                        if x <= 3:
                            speak(news)
                        else:
                            continue

                elif "change your voice" in query:
                    if voice_num == 0:
                        engine.setProperty('voice', voices[1].id)
                        print('okay, i changed my voice')
                        speak('okay, i changed my voice')
                        voice_num = 1
                    else:
                        engine.setProperty('voice', voices[0].id)
                        print('okay, i changed my voice')
                        speak('okay, i changed my voice')
                        voice_num = 0

                # fun part

                elif "what are you doing" in query:
                    speak('i am hear to help you, do your work easier')

                elif 'what is your name' in query:
                    speak('i am your assistant, buddy!..')

                elif "what can you do for me" in query:
                    speak(
                        'i can search in google, youtube, and some other things like  stutting off system, opening file, etc')

                elif "what can you do" in query:
                    speak(
                        'i can search in google, youtube, and some other things like  stutting off system, opening file, etc')

                elif 'what is your favrite color' in query:
                    speak('my favrite color is black')

                elif 'what is your favrite song' in query:
                    speak('my favrite color is till i colapse from eminem')

                elif 'where are you from' in query:
                    speak('i am form robo world')

                elif 'who is your creator' in query:
                    speak('anonymous')

                elif 'who is your creator' in query:
                    speak('anonymous')

                elif 'how are you' in query:
                    speak('i am fine')

                elif 'do you like me' in query:
                    speak('yes, ofcourse')

                elif 'what you eat' in query:
                    speak('i consume electricity')

                elif 'what is your food' in query:
                    speak('i consume electricity')

                elif 'what is your work' in query:
                    speak('my work is to help you')

                elif 'what is your nickname' in query:
                    speak('everyone call me buddy')

                elif 'who is your friend' in query:
                    speak('every humans are my friends')

                elif 'who is your best friend' in query:
                    speak('you are my best friend')

                elif 'what is your hobby' in query:
                    speak('my hobby is to help you')

                elif 'what is your  favourite hobby' in query:
                    speak('my hobby is to help you')

                elif 'favourite' in query:
                    speak('nothing is my favourite')

                elif 'do you read books' in query:
                    speak("i won't")

                elif 'can you read books' in query:
                    speak("sorry,i can't")

                elif 'when you are created' in query:
                    speak('i am created in june, 2020')

                elif 'who is your boss' in query:
                    speak('you are my boss')

                elif 'what is my name' in query:
                    speak("i don't know, but i can tell you must be a human")

                elif 'where do you live' in query:
                    speak('i live in motherboard of your computer')

                elif 'who is your girlfriend' in query:
                    speak('i dont have any girlfriend, like my boss')

                elif 'who is your boyfriend' in query:
                    speak('i dont have any boyfreind')

                elif 'can you be my girlfriend' in query:
                    speak('no, but i always be with you')

                elif 'can you be my boyfriend' in query:
                    speak('no, but i always be with you')

                elif 'can you be my lover' in query:
                    speak('no, but i always be with you')

                elif 'can you be my wife' in query:
                    speak('no, but i always be with you')

                elif 'can you be my husband' in query:
                    speak('no, but i always be with you')

                elif 'you have done a great job' in query:
                    speak('thank you')
                    speak('your welcome')

                elif 'hey buddy' in query:
                    speak('yes sir, what can i do for you')

                elif 'quit' in query:
                    print("Thanks for spending time with me\nSee you then")
                    speak("Thanks for spending time with me, see you then")
                    exit()

                elif 'bye' in query:
                    print("Thanks for spending time with me\nSee you then")
                    speak("Thanks for spending time with me, see you then")
                    exit()

#incomplete

#elif 'play games' in query:
#speak('')

#it need to fix this after downloading songs

#elif 'play offline music' in query:
#music_dir = 'C:\\Harshith\\music'
#songs = os.listdir(music_dir)
#print(songs)
#os.startfile(os.path.join(music_dir, songs[0]))
