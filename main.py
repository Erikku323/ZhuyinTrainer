from tkinter import *
import time

from cards import Cards






##########################################
#Functions
#######################################


def newCardEnter(event):
        if cardList.deck == 2:
            card = cardList.getNextCard()
            #card = cardList.getRandom()
            canvas.itemconfig(cardChinese, text=card[0],font=("Arial",40))
            canvas.itemconfig(zhuyinCard, text=card[1],font=("Arial",60,"bold"))
            canvas.itemconfig(userInputText, text="",font=("Arial",40,))
            print("The next card")
            print(cardList.getNext())


def newCard():
    if cardList.deck == 2:
        card = cardList.getNextCard()
         #card = cardList.getRandom()
        canvas.itemconfig(cardChinese,text=card[0],font=("Arial",40))
        canvas.itemconfig(zhuyinCard, text=card[1],font=("Arial",60,"bold"))
        canvas.itemconfig(userInputText, text="",font=("Arial",40,))
    if cardList.deck == 1:
        card = cardList.getNextZhuyin()
        canvas.itemconfig(cardChinese, text=card[0], font=("Arial", 40))
        canvas.itemconfig(zhuyinCard, text=card[1], font=("Arial", 60, "bold"))
        canvas.itemconfig(userInputText, text="", font=("Arial", 40,))

def onKeyPress(event):
   # print('You pressed %s\n' % (event.char, ) + "Key")
    keypressed = event.char
    if cardList.deck == 2:
        if zhuyinDict.__contains__(keypressed):
            key = zhuyinDict[keypressed]
            output = cardList.userInput(key)
            print(output)
            canvas.itemconfig(userInputText, text=output,font=("Arial",40,))
    if cardList.deck == 1:
        if zhuyinDict.__contains__(keypressed):
            key = zhuyinDict[keypressed]
            output = cardList.userInputZhuyin(key)
            canvas.itemconfig(userInputText, text=output, font=("Arial", 40,))
            if cardList.checkZhuyinCard() == True:
                newCard()



BACKGROUND_COLOR = "#B1DDC6"

zhuyinDict ={
    "1": "ㄅ",
    "q": "ㄆ",
    "a": "ㄇ",
    "z": "ㄈ",
    "2": "ㄉ",
    "w": "ㄊ",
    "s": "ㄋ",
    "x": "ㄌ",
    "e": "ㄍ",
    "d":"ㄎ",
    "c": "ㄏ",
    "r": "ㄐ",
    "f" :"ㄑ",
    "v" : "ㄒ",
    "5" : "ㄓ",
    "t":"ㄔ",
    "g":"ㄕ",
    "b":"ㄖ",
    "y":"ㄗ",
    "h":"ㄘ",
    "n": "ㄙ",
    "u": "ㄧ",
    "j": "ㄨ",
    "m":"ㄩ",
    "8":"ㄚ",
    "i":"ㄛ",
    "k":"ㄜ",
    ",":"ㄝ",
    "9":"ㄞ",
    "o":"ㄟ",
    "l": "ㄠ",
    ".":"ㄡ",
    "0":"ㄢ",
    "p":"ㄣ",
    ";":"ㄤ",
    "/":"ㄥ",
    "-":"ㄦ",
    " ":"ˉ",
    "6":"ˊ",
    "3":"ˇ",
    "4":"ˋ",
    "7":"˙"

}

cardList = Cards(zhuyinDict)



def closeStartWindow():
    cardList.deck = radio_state.get()
    print((cardList.deck))
    randomState = randomCheckState.get()
    if randomState == 1 :
        print("Shuffing Cards")
        cardList.random = True
        cardList.shuffleCards()
    startWindow.destroy()



startWindow = Tk()
startWindow.title("Welcome to Zhuyin Trainer")
startWindow.minsize(width=300,height=300)
welcomeLabel = Label(text="Welcome to Zhuyin Trainer!",pady=20)
welcomeLabel.pack()

randomCheckState = IntVar()
randomCheckbox = Checkbutton(text="Random",variable=randomCheckState)
randomCheckbox.pack()


#Radiobutton
def radio_used():
    print(radio_state.get())

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radio_state.set("1")
radiobutton1 = Radiobutton(text="Learn Zhuyin", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Practive Zhuyin", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()





choiceButton = Button(text="Start",command=closeStartWindow)
choiceButton.pack()


startWindow.mainloop()





#button = Button(image=my_image, highlightthickness=0)

window = Tk()
window.title("Zhuyin Trainer")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)


cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")

canvas.create_image(400,263,image=cardFront)

cardChinese = canvas.create_text(400,150,text="Title",font=("Arial",40))
zhuyinCard = canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))
userInputText = canvas.create_text(400,363,text="Word",font=("Arial",40,))

if cardList.deck == 1:
    card = cardList.setFirstZhuyin()
    canvas.itemconfig(cardChinese, text=card[0], font=("Arial", 40))
    canvas.itemconfig(zhuyinCard, text=card[1], font=("Arial", 60, "bold"))
    canvas.itemconfig(userInputText, text="", font=("Arial", 40,))
else:
    canvas.itemconfig(cardChinese,text="Welcome to Zhuyin Trainer",font=("Arial",20))
    canvas.itemconfig(zhuyinCard,text="What do you want to Practice?",font=("Arial",20))
    canvas.itemconfig(userInputText,text="Words of Single Zhuyin")

crossImage = PhotoImage(file="images/wrong.png")
checkImage = PhotoImage(file="images/right.png")







skipButton = Button(image=crossImage,highlightthickness=0,command=newCard)
skipButton.grid(row=1,column=0)
knowButton = Button(image= checkImage,command=newCard)
knowButton.grid(row=1,column=1)


canvas.grid(column=0,row=0,columnspan=2)


window.bind('<KeyPress>', onKeyPress)
window.bind("<Return>",newCardEnter)

window.mainloop()