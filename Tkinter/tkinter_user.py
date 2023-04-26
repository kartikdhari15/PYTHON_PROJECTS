import os
import tkinter as t
def login():

    if(E1.get()=="15" and E2.get()=="abc"):
        t.Label(windows,text="ACCESS GRANTED",fg="Green",font=("Arial Bold",20)).pack()
        windows.after(2000,windows.destroy)
        import tkinter_game
        os.system("tkinter_game.py")
    else:
        t.Label(windows,text="ACCESS DENIED",fg="Red",font=("Arial Bold",20)).pack()
        windows.after(2000,windows.destroy)
    windows.mainloop()

windows=t.Tk()
windows.title("LOGIN")
INTRO=t.Label(windows,text="LOGIN TO ACCESS THE GAME",fg="Purple",bg="Orange",font=("Arial Bold",25),height=13,width=26).pack()
USER=t.Label(windows,text="USERNAME:",font=("Arial Bold",15)).pack(side="top")
x=t.StringVar()
E1=t.Entry(windows,textvariable=x)
E1.pack()
PASS_KEY=t.Label(windows,text="PASSWORD:",font=("Arial Bold",15)).pack(side="top")
y=t.StringVar()
E2=t.Entry(windows,show="*",textvariable=y)
E2.pack()
LOGIN=t.Button(windows,text="LOGIN",fg="Purple",font=("Arial Bold",15),relief="groove",command=login).pack()
windows.mainloop()