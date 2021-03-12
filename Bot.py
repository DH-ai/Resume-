from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
from tkinter import *
import sys
from googlesearch import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices [ 1 ].id)


def Sp(audio):
    engine.say(audio)
    engine.runAndWait()


Sp("initializing")


def cancel():
    win.destroy()
    sys.exit()


def command1(event):
    file = open("pswd.txt",'w')
    file.write(str((entry1.get()) + (entry2.get())))
    file.close()
    fileP2 = open("pswd2.txt",'r')
    filep1 = open("pswd.txt","r")

    if filep1.read() == fileP2.read():
        win.destroy()
        filep1.close()
        fileP2.close()

        def TimeAndGreet():
            hour = int(datetime.datetime.now().hour)
            if hour >> 12 and hour << 18:
                Sp("Good Morning! SIR")

            elif hour >> 0 and hour << 5:
                Sp("Good afternoon! SIR")

            else:
                Sp("Good evening! Sir")
            Sp("I am lumna! how may i help you ")

        def LCo():
            r = sr.Recognizer()  # sr= speech recognition
            with sr.Microphone() as source:
                print("Listening...")
                r.energy_threshold = 300
                r.pause_threshold = 0.8
                audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio,language = 'en-in')
                print("User said:",query)
            except Exception:
                print("Say that again pls")
                return "None"
            return query

        if __name__ == "__main__":
            TimeAndGreet()
            while True:
                query = LCo().lower()
                if 'wikipedia' in query:
                    Sp("Searching Wikipedia.. ")
                    query = query.replace("wikipedia","")
                    result = wikipedia.summary(query,sentences = 5)
                    Sp("according to wikipedia ")
                    print(result)
                    Sp(result)
                elif 'open youtube' in query:
                    Sp("Opening")
                    webbrowser.open("www.youtube.com")
                elif 'open google' in query:
                    Sp("Opening")
                    webbrowser.open("www.google.com")
                elif 'play music' in query:
                    Sp("Playing")
                    music_dir = 'F:\\Music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs [ 0 ]))
                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H : %M  :%S")
                    Sp(f'sir, the time is {strTime}')
                elif "open gmail" in query:
                    Sp("Opening")
                    webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
                elif "code" in query:
                    Sp('opening')
                    os.startfile("F:\\Chachu's Song\\PYTHON WORKSPACE\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe")
                elif "open camera" in query:
                    cap = cv2.VideoCapture(0)
                    Sp("opening")
                    while True:
                        ret,frame = cap.read()
                        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
                        cv2.imshow('frame',gray)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                elif "bye" in query or "Q\quit" in query:
                    sys.exit()
                elif "hi lumna" in query:
                    Sp("HI! Nice to meet You ")
                elif "who created you" in query:
                    Sp("Dhruv chaturvedi")
                elif "i am bored" in query:
                    Sp("So! what can i do for you ")

                elif "thanks" in query or "thank you" in query:
                    Sp("it's my plessure ")
                elif "google" in query:
                    wn2 = Tk()
                    wn2.geometry("500x500+340+60")
                    wn2.title("Master's query")
                    wn2.resizable(0,0)
                    wn2.configure(background = "white")

                    frame1 = Frame(wn2)
                    frame1.pack(expand = True,fill = BOTH)
                    labelG = Label(frame1,text = "G",font = ("product sans",90),fg = "#6680FF")
                    labelG.pack(expand = True,fill = BOTH,side = LEFT)
                    labelO = Label(frame1,text = "o",font = ("product sans",90),fg = "#6680FF")
                    labelO.pack(expand = True,fill = BOTH,side = LEFT)
                    labelO1 = Label(frame1,text = "o",font = ("product sans",90),fg = "#FFAA00")
                    labelO1.pack(expand = True,fill = BOTH,side = LEFT)
                    labelG1 = Label(frame1,text = "g",font = ("product sans",90),fg = "#33AA65")
                    labelG1.pack(expand = True,fill = BOTH,side = LEFT)
                    labelL = Label(frame1,text = "l",font = ("product sans",90),fg = "#6680FF")
                    labelL.pack(expand = True,fill = BOTH,side = LEFT)
                    labelE = Label(frame1,text = "e",font = ("product sans",90),fg = "#FF5533")
                    labelE.pack(expand = True,fill = BOTH,side = LEFT)
                    labelDC = Label(frame1,text = "DC.Inc",font = ("product sans",9),anchor = NE)
                    labelDC.pack()

                    def En ( e ):
                        wn2.destroy()
                        query = str(q.get())
                        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                        Sp("searching")
                        for url in search(query,tld = "co.in",num = 1,stop = 1,pause = 2):
                            webbrowser.open("https://google.com/search?q=%s" % query)

                    q = StringVar()
                    frame = Frame(wn2)
                    frame.pack(expand = True,fill = "both")
                    entry = Entry(frame,textvariable = q,font = ("product sans",30))
                    entry.pack()
                    Sp("please type")
                    entry.bind("<Return>",En)

                    wn2.mainloop()
                elif "nice to meet you" in query:
                    Sp("me too")
                elif "your name" in query:
                    Sp("My name is  Lumna")
                elif "logout" in query:
                    Sp("logging ! out")
                    f = open("pswd.txt","w")
                    f.write(None)
                    f.close()
                    Sp("logout Done! Next Time! when you! open the bot !you need to login again  ")
                elif "my name" in query:
                    fileN = open("name.txt","r")
                    name = fileN.read()
                    Sp(f"your name is {name}")
                    fileN.close()
    elif entry1.get() == "" and entry2.get() == "":
        messagebox.showerror("Alert!","You didn't type the username and password")

    else:
        Sp(' Wrong Password GET OUT')
        messagebox.showerror("Error!","Wrong Password GET OUT")
        win.destroy()
        sys.exit()


def command10():
    file = open("pswd.txt",'w')
    file.write(str((entry1.get()) + (entry2.get())))
    file.close()
    fileP2 = open("pswd2.txt",'r')
    filep1 = open("pswd.txt","r")

    if filep1.read() == fileP2.read():
        win.destroy()
        fileP2.close()
        filep1.close()

        def TimeAndGreet ():
            hour = int(datetime.datetime.now().hour)
            if hour >> 12 and hour << 18:
                Sp("Good Morning! SIR")


            elif hour >> 0 and hour << 5:
                Sp("Good afternoon! SIR")

            else:
                Sp("Good evening! Sir")
            Sp("I am lumna! how may i help you ")

        def LCo ():
            r = sr.Recognizer()  # sr= speech recognition
            with sr.Microphone() as source:
                print("Listening...")
                r.energy_threshold = 300
                r.pause_threshold = 0.8
                audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio,language = 'en-in')
                print("User said:",query)
            except Exception:
                print("Say that again pls")
                return "None"
            return query

        if __name__ == "__main__":
            TimeAndGreet()
            while True:
                query = LCo().lower()
                if 'wikipedia' in query:
                    Sp("Searching Wikipedia.. ")
                    query = query.replace("wikipedia","")
                    result = wikipedia.summary(query,sentences = 5)
                    Sp("according to wikipedia ")
                    print(result)
                    Sp(result)
                elif 'open youtube' in query:
                    Sp("Opening")
                    webbrowser.open("www.youtube.com")
                elif 'open google' in query:
                    Sp("Opening")
                    webbrowser.open("www.google.com")
                elif 'play music' in query:
                    Sp("Playing")
                    music_dir = 'F:\\Music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs [ 0 ]))
                elif "what is my name " in query:
                    Sp("dhruv")
                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H : %M  :%S")
                    Sp(f'sir, the time is {strTime}')
                elif "open gmail" in query:
                    Sp("Opening")
                    webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
                elif "code" in query:
                    Sp('opening')
                    os.startfile("F:\\Chachu's Song\\PYTHON WORKSPACE\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe")
                elif "open camera" in query:
                    cap = cv2.VideoCapture(0)
                    Sp("opening")
                    while True:
                        ret,frame = cap.read()
                        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
                        cv2.imshow('frame',gray)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                elif "bye" in query or "quit" in query:
                    sys.exit()
                elif "hi lumna" in query:
                    Sp("HI! Nice to meet You  ")
                elif "who created you" in query:
                    Sp("dhruv chaturvedi")
                elif "i am bored" in query:
                    Sp("So! what can i do for you ")
                elif "thanks" in query or "thank you" in query:
                    Sp("it's my plessure ")
                elif "google" in query:
                    wn2 = Tk()
                    wn2.geometry("500x500+340+60")
                    wn2.title("Master's query")
                    wn2.resizable(0,0)
                    wn2.configure(background = "white")

                    frame1 = Frame(wn2)
                    frame1.pack(expand = True,fill = BOTH)
                    labelG = Label(frame1,text = "G",font = ("product sans",90),fg = "#6680FF")
                    labelG.pack(expand = True,fill = BOTH,side = LEFT)
                    labelO = Label(frame1,text = "o",font = ("product sans",90),fg = "#6680FF")
                    labelO.pack(expand = True,fill = BOTH,side = LEFT)
                    labelO1 = Label(frame1,text = "o",font = ("product sans",90),fg = "#FFAA00")
                    labelO1.pack(expand = True,fill = BOTH,side = LEFT)
                    labelG1 = Label(frame1,text = "g",font = ("product sans",90),fg = "#33AA65")
                    labelG1.pack(expand = True,fill = BOTH,side = LEFT)
                    labelL = Label(frame1,text = "l",font = ("product sans",90),fg = "#6680FF")
                    labelL.pack(expand = True,fill = BOTH,side = LEFT)
                    labelE = Label(frame1,text = "e",font = ("product sans",90),fg = "#FF5533")
                    labelE.pack(expand = True,fill = BOTH,side = LEFT)
                    labelDC = Label(frame1,text = "DC.Inc",font = ("product sans",9),anchor = NE)
                    labelDC.pack()

                    def En ( e ):
                        wn2.destroy()
                        query = str(q.get())
                        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                        Sp("searching")
                        for url in search(query,tld = "co.in",num = 1,stop = 1,pause = 2):
                            webbrowser.open("https://google.com/search?q=%s" % query)

                    q = StringVar()
                    frame = Frame(wn2)
                    frame.pack(expand = True,fill = "both")
                    entry = Entry(frame,textvariable = q,font = ("product sans",30))
                    entry.pack()
                    Sp("please type ")
                    entry.bind("<Return>",En)

                    wn2.mainloop()
                elif "nice to meet you" in query:
                    Sp("me too")
                elif "your name" in query:
                    Sp("My name is  Lumna")
                elif "logout" in query:
                    Sp("logging ! out")
                    f = open("pswd.txt","w")
                    f.write(None)
                    f.close()
                    Sp("logout Done! Next Time! when you! open the bot !you need to login again  ")

                elif "my name" in query:
                    fileN = open("name.txt","r")
                    name = fileN.read()
                    Sp(f"your name is {name}")
                    fileN.close()

    elif entry1.get() == "" and entry2.get() == "":
        messagebox.showerror("Alert!","You didn't type the username and password")
    else:
        Sp('Wrong Password GET OUT')
        messagebox.showerror("Error!","Wrong Password GET OUT")
        win.destroy()
        sys.exit()


win = Tk()
win.geometry('600x600+340+60')
win.title('Login AI')
win.resizable(0,0)
win.configure(background = '#202021')
photo1 = PhotoImage(file = 'ai.gif')

photo = Label(win,image = photo1,height = 100,width = 100)
photo.pack(expand = True,fill = 'both')
lbl1 = Label(win,text = "USER NAME",font = ('Courier',10),fg = "white",bg = '#202021')
lbl1.pack()
entry1 = Entry(win)
entry1.pack()
lbl2 = Label(win,text = "password",font = ('Courier',10),fg = "white",bg = '#202021')
lbl2.pack()
entry2 = Entry(win,show = "*")
entry2.pack()
entry2.bind('<Return>',command1)
frame = Frame(win)
frame.pack()
button1 = Button(frame,text = "Login",fg = "white",bg = '#202021',activebackground = '#9b870c',relief = GROOVE,
                 command = command10)
button1.pack(side = LEFT)
button2 = Button(frame,text = "Cancel",fg = "white",bg = '#202021',activebackground = '#9b870c',relief = GROOVE,
                 command = cancel)
button2.pack(side = LEFT)

info = StringVar()
info1 = StringVar()
info2 = StringVar()


def print_():
    fileN = open("name.txt","w")
    fileN.write(str(info.get()))
    fileN.close()
    fileP1 = open("pswd2.txt","w")
    fileP1.write(str(info1.get()) + str(info2.get()))
    fileP1.close()
    win.destroy()

    def TimeAndGreet ():
        hour = int(datetime.datetime.now().hour)
        if hour >> 12 and hour << 18:
            Sp("Good Morning! SIR")

        elif hour >> 0 and hour << 5:
            Sp("Good afternoon! SIR")

        else:
            Sp("Good evening! Sir")
        Sp("I am lumna! how may i help you ")

    def LCo ():
        r = sr.Recognizer()  # sr= speech recognition
        with sr.Microphone() as source:
            print("Listening...")
            r.energy_threshold = 300
            r.pause_threshold = 0.8
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language = 'en-in')
            print("User said:",query)
        except Exception:
            print("Say that again pls")
            return "None"
        return query

    if __name__ == "__main__":
        TimeAndGreet()
        while True:
            query = LCo().lower()
            if 'wikipedia' in query:
                Sp("Searching Wikipedia.. ")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query,sentences = 5)
                Sp("according to wikipedia ")
                print(result)
                Sp(result)
            elif 'open youtube' in query:
                Sp("Opening")
                webbrowser.open("www.youtube.com")
            elif 'open google' in query:
                Sp("Opening")
                webbrowser.open("www.google.com")
            elif 'play music' in query:
                Sp("Playing")
                music_dir = 'F:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs [ 0 ]))
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H : %M  :%S")
                Sp(f'sir, the time is {strTime}')
            elif "open gmail" in query:
                Sp("Opening")
                webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            elif "code" in query:
                Sp('opening')
                codepath = (
                    "F:\\Chachu's Song\\PYTHON WORKSPACE\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe")
                os.startfile(codepath)
            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                Sp("opening")
                while True:
                    ret,frame = cap.read()
                    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
                    cv2.imshow('frame',gray)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "bye" in query or "quit" in query:
                sys.exit()
            elif "hi lumna" in query:
                Sp("HI! Nice to meet You ")
            elif "who created you" in query:
                Sp("Dhruv chaturvedi")
            elif "i am bored" in query:
                Sp("So! what can i do for you ")

            elif "thanks" in query or "thank you" in query:
                Sp("it's my pleasure ")
            elif "google" in query:
                wn2 = Tk()
                wn2.geometry("500x500+340+60")
                wn2.title("Master's query")
                wn2.resizable(0,0)
                wn2.configure(background = "white")

                frame1 = Frame(wn2)
                frame1.pack(expand = True,fill = BOTH)
                labelG = Label(frame1,text = "G",font = ("product sans",90),fg = "#6680FF")
                labelG.pack(expand = True,fill = BOTH,side = LEFT)
                labelO = Label(frame1,text = "o",font = ("product sans",90),fg = "#6680FF")
                labelO.pack(expand = True,fill = BOTH,side = LEFT)
                labelO1 = Label(frame1,text = "o",font = ("product sans",90),fg = "#FFAA00")
                labelO1.pack(expand = True,fill = BOTH,side = LEFT)
                labelG1 = Label(frame1,text = "g",font = ("product sans",90),fg = "#33AA65")
                labelG1.pack(expand = True,fill = BOTH,side = LEFT)
                labelL = Label(frame1,text = "l",font = ("product sans",90),fg = "#6680FF")
                labelL.pack(expand = True,fill = BOTH,side = LEFT)
                labelE = Label(frame1,text = "e",font = ("product sans",90),fg = "#FF5533")
                labelE.pack(expand = True,fill = BOTH,side = LEFT)
                labelDC = Label(frame1,text = "DC.Inc",font = ("product sans",9),anchor = NE)
                labelDC.pack()

                def En ( e ):
                    wn2.destroy()
                    query = str(q.get())
                    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                    Sp("searching")
                    for url in search(query,tld = "co.in",num = 1,stop = 1,pause = 2):
                        webbrowser.open("https://google.com/search?q=%s" % query)

                q = StringVar()
                frame = Frame(wn2)
                frame.pack(expand = True,fill = "both")
                entry = Entry(frame,textvariable = q,font = ("product sans",30))
                entry.pack()
                Sp("please type")
                entry.bind("<Return>",En)

                wn2.mainloop()
            elif "nice to meet you" in query:
                Sp("me too")
            elif "your name" in query:
                Sp("My name is  Lumna")
            elif "logout" in query:
                Sp("logging ! out")
                f = open("pswd.txt","w")
                f.write("")
                f.close()
                Sp("logout Done! Next Time! when you! open the bot !you need to login again  ")
            elif "my name" in query:
                fileN = open("name.txt","r")
                name = fileN.read()
                Sp(f"your name is {name}")
                fileN.close()

def func():
    global info
    photo.destroy()
    button1.destroy()
    button2.destroy()
    frame.destroy()
    entry1.destroy()
    entry2.destroy()
    lbl2.destroy()
    lbl1.destroy()
    but.destroy()
    win.geometry("400x400+300+60")
    win.title('New User ')

    fram1 = Frame(win,bg = '#202021')
    fram1.pack(expand = TRUE,fill = "both")

    frame2 = Frame(win,bg = '#202021')
    frame2.pack(expand = TRUE,fill = "both")

    fram33 = Frame(win,bg = '#202021')
    fram33.pack(expand = TRUE,fill = "both")

    labN = Label(fram1,text = '   Name    ',font = ('Courier',10),bg = '#202021',fg = "white",anchor = E)
    labN.pack(expand = True,fill = "both",side = "left")
    Entry_N = Entry(fram1,font = ("sans mono",10,),fg = "black",textvariable = info)
    Entry_N.pack(expand = TRUE,side = "left")

    labU = Label(frame2,text = 'User name  ',font = ('Courier',10),bg = '#202021',fg = "white",anchor = E)
    labU.pack(expand = True,fill = "both",side = "left")
    Entry_U = Entry(frame2,font = ("sans mono",10,),fg = "black",textvariable = info1)
    Entry_U.pack(expand = TRUE,side = "left")

    labP = Label(fram33,text = 'Password   ',font = ('Courier',10),bg = '#202021',fg = "white",anchor = E)
    labP.pack(expand = True,fill = "both",side = "left")
    Entry_P = Entry(fram33,font = ("sans mono",10,),fg = "black",textvariable = info2)
    Entry_P.pack(expand = TRUE,side = "left")

    buttonL = Button(
        win,
        text = "Log in",
        relief = GROOVE,
        border = 3,
        bg = '#202021',
        fg = "white",
        activebackground = "light blue",
        command = print_
    )
    buttonL.pack(side = "bottom")

    lab.destroy()


lab = Label(win,text = "Luna a DC.Inc product",font = ("sans mono",10,),fg = "white",bg = '#202021',anchor = SE)
lab.pack(side = RIGHT)

but = Button(win,text = "Log Out",anchor = SW,relief = GROOVE,border = 0,bg = '#202021',fg = "white",
             activebackground = "light blue",command = func)
but.pack(side = LEFT)

file1 = open("pswd.txt","r")
file2 = open("pswd2.txt","r")
if file2.read() == file1.read():
    win.destroy()
    file2.close()
    file1.close()


    def TimeAndGreet ():
        hour = int(datetime.datetime.now().hour)
        if hour >> 12 and hour << 18:
            Sp("Good Morning! SIR")

        elif hour >> 0 and hour << 5:
            Sp("Good afternoon! SIR")

        else:
            Sp("Good evening! Sir")
        Sp("I am lumna! how may i help you ")


    def LCo ():
        r = sr.Recognizer()  # sr= speech recognition
        with sr.Microphone() as source:
            print("Listening...")
            r.energy_threshold = 270
            r.pause_threshold = 0.8
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language = 'en-in')
            print("User said:",query)
        except Exception:
            print("Say that again pls")
            return "None"
        return query


    if __name__ == "__main__":
        TimeAndGreet()
        while True:
            query = LCo().lower()
            if 'wikipedia' in query:
                Sp("Searching Wikipedia.. ")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query,sentences = 5)
                Sp("according to wikipedia ")
                print(result)
                Sp(result)
            elif 'open youtube' in query:
                Sp("Opening")
                webbrowser.open("www.youtube.com")
            elif 'open google' in query:
                Sp("Opening")
                webbrowser.open("www.google.com")
            elif 'play music' in query:
                Sp("Playing")
                music_dir = 'F:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
                sys.exit()
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H : %M  :%S")
                Sp(f'sir, the time is {strTime}')
            elif "open gmail" in query:
                Sp("Opening")
                webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            elif "code" in query:
                Sp('opening')
                os.startfile("F:\\Chachu's Song\\PYTHON WORKSPACE\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe")
            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                Sp("opening")
                while True:
                    ret,frame = cap.read()
                    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
                    cv2.imshow('frame',gray)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "bye" in query or "quit" in query:
                sys.exit()
            elif "hi luna" in query:
                Sp("HI! Nice to meet You ")
            elif "who created you" in query:
                Sp("Dhruv chaturvedi")
            elif "i am bored" in query:
                Sp("So! what can i do for you ")

            elif "thanks" in query or "thank you" in query:
                Sp("it's my pleasure ")
            elif "google" in query:
                wn2 = Tk()
                wn2.geometry("500x500+340+60")
                wn2.title("Master's query")
                wn2.resizable(0,0)
                wn2.configure(background = "white")

                frame1 = Frame(wn2)
                frame1.pack(expand = True,fill = BOTH)
                labelG = Label(frame1,text = "G",font = ("product sans",90),fg = "#6680FF")
                labelG.pack(expand = True,fill = BOTH,side = LEFT)
                labelO = Label(frame1,text = "o",font = ("product sans",90),fg = "#6680FF")
                labelO.pack(expand = True,fill = BOTH,side = LEFT)
                labelO1 = Label(frame1,text = "o",font = ("product sans",90),fg = "#FFAA00")
                labelO1.pack(expand = True,fill = BOTH,side = LEFT)
                labelG1 = Label(frame1,text = "g",font = ("product sans",90),fg = "#33AA65")
                labelG1.pack(expand = True,fill = BOTH,side = LEFT)
                labelL = Label(frame1,text = "l",font = ("product sans",90),fg = "#6680FF")
                labelL.pack(expand = True,fill = BOTH,side = LEFT)
                labelE = Label(frame1,text = "e",font = ("product sans",90),fg = "#FF5533")
                labelE.pack(expand = True,fill = BOTH,side = LEFT)
                labelDC = Label(frame1,text = "DC.Inc",font = ("product sans",9),anchor = NE)
                labelDC.pack()


                def En(e):
                    wn2.destroy()
                    query = str(q.get())
                    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                    Sp("searching")
                    for url in search(query,tld = "co.in",num = 1,stop = 1,pause = 2):
                        webbrowser.open("https://google.com/search?q=%s" % query)


                q = StringVar()
                frame = Frame(wn2)
                frame.pack(expand = True,fill = "both")
                entry = Entry(frame,textvariable = q,font = ("product sans",30))
                entry.pack()
                Sp("please type")
                entry.bind("<Return>",En)

                wn2.mainloop()
            elif "nice to meet you" in query:
                Sp("me too")
            elif "your name" in query:
                Sp("My name is  Lumna")
            elif "logout" in query:
                Sp("logging ! out")
                f = open("pswd.txt","w")
                f.write("")
                f.close()
                Sp("logout Done! Next Time! when you! open the bot !you need to login again  ")
            elif "my name" in query:
                fileN = open("name.txt","r")
                name = fileN.read()
                Sp(f"your name is {name}")
                fileN.close()




else:
    win.mainloop()
    file1.close()