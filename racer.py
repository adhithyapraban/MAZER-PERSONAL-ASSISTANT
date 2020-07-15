from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3, datetime, sys, wikipedia, wolframalpha, os, smtplib, random, webbrowser, pygame, subprocess

client = wolframalpha.Client('K6QKEK-86G67XRWU8')

folder = 'C:\\Users\\skt\\Music\\YouTube\\'

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(audio):
    print('Karen:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning adhithya!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon adhithya!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening adhithya!')

class Widget:
    def __init__(self):
       root = Tk()
       root.title('KAREN(MK-1)')
       root.config(background='Red')
       root.geometry('350x600')
       root.resizable(0, 0)
       img = ImageTk.PhotoImage(Image.open(r"C:\Users\Regupathi\Downloads\karen image 2.png"))
       panel = Label(root, image = img)
       panel.pack(side = "bottom", fill = "both", expand = "no")

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Start Listening\' to Give commands')

       userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='dodgerBlue', fg='white')
       left2.config(font=("Comic Sans MS", 10, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="KAREN", font=('Black ops one', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='Red',fg='white')
       left1.config(font=("Comic Sans MS", 10, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepskyBlue', fg='black', command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepskyBlue', fg='black', command=root.destroy).pack(fill='x', expand='no')

       
       speak('Hello, I am Karen! What should I do for You?')
       self.compText.set('Hello, I am Karen! What should I do for You?')

       root.bind("<Return>", self.clicked) # handle the enter key event of your keyboard
       root.mainloop()
    
    def clicked(self):
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'open ccleaner' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\CCleaner\CCleaner.exe')

        elif 'open google chrome' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif 'open powerpoint' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007.lnk.EXE')

        elif 'open youtube' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open whatsapp' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('https://web.whatsapp.com')

        elif 'open schoology' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('https://app.schoology.com/course/2458701086/materials')

        elif 'open gmail' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()

            if 'me' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Username')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    self.compText.set('Email sent!')
                    speak('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')



        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye adhithya, have a good day.')
            speak('Bye adhithya, have a good day.')
           
        elif 'hello' in query:
            self.compText.set('Hello adhithya')
            speak('Hello adhithya')


        elif 'bye' in query:
            self.compText.set('Bye ' + 'adhithya' + ', have a good day.')
            speak('Bye ' + 'adhithya' + ', have a good day.')
                                    
        elif 'play music' in query:
            music_folder = 'C:/'
            music = ['Edison', 'bensound-actionable', 'bensound-buddy', 'Micro', 'Lucid_Dreamer']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            
            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')
            
        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    self.compText.set(results)
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    self.compText.set(results)
                    speak(results)
        
            except:
                speak('I don\'t know Sir! Google is smarter than me!')
                self.compText.set('I don\'t know Sir! Google is smarter than me!')
                webbrowser.open('www.google.com')
                
if __name__ == '__main__':
    greetMe()
    widget = Widget()