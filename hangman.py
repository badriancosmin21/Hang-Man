
import random
import tkinter as tk
from tkinter import StringVar
from PIL import Image, ImageTk

win = tk.Tk()

f = open("words.txt", "r")
class Ch:
    chances = 0
filecontent = f.read()
lines = filecontent.splitlines()
iLine = random.randrange(0, len(lines))
word = lines[iLine]
guessWord = '_' * len(word)
guess = list(guessWord)

guesslbl = StringVar()
letter = StringVar()
statuslbl = StringVar()

xPos = int(win.winfo_screenwidth() / 2 - win.winfo_reqwidth())
yPos = int(win.winfo_screenheight() / 2 - win.winfo_reqheight())
win.geometry("+{}+{}".format(xPos, yPos))
win.geometry("490x620")

image0 = Image.open("C:/Users/zbirl/Desktop/PYTHON/Hang Man/images/0.jpg")
image0 = image0.resize((400, 300), Image.ANTIALIAS)
pic0 = ImageTk.PhotoImage(image0)

image1 = Image.open("C:/Users/zbirl/Desktop/PYTHON/Hang Man/images/1.jpg")
image1 = image1.resize((400, 300), Image.ANTIALIAS)
pic1 = ImageTk.PhotoImage(image1)

image2 = Image.open("C:/Users/zbirl/Desktop/PYTHON/Hang Man/images/2.jpg")
image2 = image2.resize((400, 300), Image.ANTIALIAS)
pic2 = ImageTk.PhotoImage(image2)

image3 = Image.open("C:/Users/zbirl/Desktop/PYTHON/Hang Man/images/3.jpg")
image3 = image3.resize((400, 300), Image.ANTIALIAS)
pic3 = ImageTk.PhotoImage(image3)

image4 = Image.open("C:/Users/zbirl/Desktop/PYTHON/Hang Man/images/4.jpg")
image4 = image4.resize((400, 300), Image.ANTIALIAS)
pic4 = ImageTk.PhotoImage(image4)

image5 = Image.open("C:/Users/zbirl/Desktop/PYTHON/Hang Man/images/5.jpg")
image5 = image5.resize((400, 300), Image.ANTIALIAS)
pic5 = ImageTk.PhotoImage(image5)

image6 = Image.open("C:/Users/zbirl/Desktop/PYTHON/Hang Man/images/6.jpg")
image6 = image6.resize((400, 300), Image.ANTIALIAS)
pic6 = ImageTk.PhotoImage(image6)


picture = tk.Label(win, image=pic0)
picture.pack()

labelguess = tk.Label(win, textvariable=guesslbl, font=("Courier", 24, "bold"))
labelguess.pack()
entryletter = tk.Entry(win, width=5, font=("Courier", 24, "bold"), justify = tk.CENTER, textvariable=letter)
win.bind('<Return>',lambda event: check(labelguess, entryletter))
entryletter.pack()


tk.Button(win, text="SUBMIT", font=("Courier", 30, "bold"), command=lambda: check(labelguess, entryletter)).pack()
guesslbl.set(guess)
labelstatus = tk.Label(win, textvariable=statuslbl, font=("Courier", 18))
labelstatus.pack()


def printHangMan(picture):
    if Ch.chances == 1:
        picture.configure(image=pic1)
    elif Ch.chances == 2:
        picture.configure(image=pic2)
    elif Ch.chances == 3:
        picture.configure(image=pic3)
    elif Ch.chances == 4:
        picture.configure(image=pic4)
    elif Ch.chances == 5:
        picture.configure(image=pic5)
    elif Ch.chances == 6:
        picture.configure(image=pic6)


def check(labelguess, entryletter):
    if len(entryletter.get()) >= 2 or entryletter.get().isdigit() or entryletter.get() == "":
        statuslbl.set("Please input only one LETTER")
        return
    lett = entryletter.get()
    letter.set("")
    print(entryletter.get())
    while True:
        k = 1
        for i in range(0, len(guess)):
            if lett == word[i].lower():
                if guess[i] == lett:
                    statuslbl.set("LETTER ALREADY USED!")
                    return
                guess[i] = lett
                k = 0
        
        guesslbl.set(guess)
        if k == 1:
            Ch.chances += 1
        printHangMan(picture)
        if '_' not in guess:
            statuslbl.set("YOU WON!")
        if Ch.chances == 6:
            statuslbl.set("YOU LOST!")
        return

win.mainloop()
