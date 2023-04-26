import tkinter as t
import random
buttonlist=[]
Colour=(['red','green','brown','orange','blue'])
global ctr
ctr=0
def PLAY():

    BUTTON_CLICK1.configure(bg=random.choice(Colour))
    BUTTON_CLICK2.configure(bg=random.choice(Colour))
    BUTTON_CLICK3.configure(bg=random.choice(Colour))
    BUTTON_CLICK4.configure(bg=random.choice(Colour))
    windows1.after(2000,click_event)
    windows1.mainloop()

def click_event():

    CHANGE()

def CHANGE():

    B1.configure(bg="SystemButtonFace", command=lambda:CHECK(buttonlist[0]))
    B2.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[1]))
    B3.configure(bg="SystemButtonFace", command=lambda:CHECK(buttonlist[2]))
    B4.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[3]))
    B5.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[4]))
    B6.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[5]))
    B7.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[6]))
    B8.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[7]))
    B9.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[8]))
    B10.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[9]))
    B11.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[10]))
    B12.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[11]))
    B13.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[12]))
    B14.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[13]))
    B15.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[14]))
    B16.configure(bg="SystemButtonFace", command=lambda: CHECK(buttonlist[15]))

def CHECK(x):
    global ctr

    if x==CHOICE[0]:
        CHOICE[0].configure(text="CORRECT")
        ctr+=1
    elif x == CHOICE[1]:
        CHOICE[1].configure(text="CORRECT")
        ctr+=1
    elif x == CHOICE[2]:
        CHOICE[2].configure(text="CORRECT")
        ctr += 1
    elif x == CHOICE[3]:
        CHOICE[3].configure(text="CORRECT")
        ctr+=1
    else:
        x.configure(text="WRONG")
        MESSAGE(100)

    MESSAGE(ctr)

def MESSAGE(w):
    print(w)
    if w==100:
        windows2 = t.Tk()
        windows2.title("MESSAGE")
        t.Label(windows2, text="YOU'VE LOST THE GAME", bg="RED", fg="ORANGE",font=("Arial Bold",30)).pack()

    if w==4:
        windows2=t.Tk()
        windows2.title("MESSAGE")
        t.Label(windows2,text="YOU'VE WON THE GAME",bg="RED",fg="ORANGE",font=("Arial Bold",30)).pack()

windows1=t.Tk()
windows1.title("GAME")
B1=t.Button(windows1)
B1.grid(row=0,column=0)
B1.configure(height=10,width=23)
B2=t.Button(windows1)
B2.grid(row=0,column=1)
B2.configure(height=10,width=23)
B3=t.Button(windows1)
B3.grid(row=0,column=2)
B3.configure(height=10,width=23)
B4=t.Button(windows1)
B4.grid(row=0,column=3)
B4.configure(height=10,width=23)
B5=t.Button(windows1)
B5.grid(row=1,column=0)
B5.configure(height=10,width=23)
B6=t.Button(windows1)
B6.grid(row=1,column=1)
B6.configure(height=10,width=23)
B7=t.Button(windows1)
B7.grid(row=1,column=2)
B7.configure(height=10,width=23)
B8=t.Button(windows1)
B8.grid(row=1,column=3)
B8.configure(height=10,width=23)
B9=t.Button(windows1)
B9.grid(row=2,column=0)
B9.configure(height=10,width=23)
B10=t.Button(windows1)
B10.grid(row=2,column=1)
B10.configure(height=10,width=23)
B11=t.Button(windows1)
B11.grid(row=2,column=2)
B11.configure(height=10,width=23)
B12=t.Button(windows1)
B12.grid(row=2,column=3)
B12.configure(height=10,width=23)
B13=t.Button(windows1)
B13.grid(row=3,column=0)
B13.configure(height=10,width=23)
B14=t.Button(windows1)
B14.grid(row=3,column=1)
B14.configure(height=10,width=23)
B15=t.Button(windows1)
B15.grid(row=3,column=2)
B15.configure(height=10,width=23)
B16=t.Button(windows1)
B16.grid(row=3,column=3)
B16.configure(height=10,width=23)
buttonlist.append(B1)
buttonlist.append(B2)
buttonlist.append(B3)
buttonlist.append(B4)
buttonlist.append(B5)
buttonlist.append(B6)
buttonlist.append(B7)
buttonlist.append(B8)
buttonlist.append(B9)
buttonlist.append(B10)
buttonlist.append(B11)
buttonlist.append(B12)
buttonlist.append(B13)
buttonlist.append(B14)
buttonlist.append(B15)
buttonlist.append(B16)
BUTTON_CLICK1=random.choice(buttonlist)
BUTTON_CLICK2=random.choice(buttonlist)
BUTTON_CLICK3=random.choice(buttonlist)
BUTTON_CLICK4=random.choice(buttonlist)
CHOICE=[BUTTON_CLICK1,BUTTON_CLICK2,BUTTON_CLICK3,BUTTON_CLICK4]
PLAY=t.Button(windows1,text="PLAY",fg="Red",bg="Orange",font=("Arial Bold",30),command=PLAY)
PLAY.grid(row=10,column=1)
EXIT=t.Button(windows1,text="EXIT",fg="Green",bg="Orange",font=("Arial Bold",30),command=exit)
EXIT.grid(row=10,column=2)
windows1.mainloop()