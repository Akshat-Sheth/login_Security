from tkinter import *
from datetime import datetime

def quit():
    exit_btn.configure(exit())

usr=input(str('set a username'))

now=datetime.now()
time=int(now.strftime("%S"))

pwd=input(str("set the password"))

now2=datetime.now()
time2=int(now2.strftime("%S"))




def login():
    diff=time2-time
    diff2=time_0-time0
    password = password_text.get()
    username = usr_name_text.get()

    if(str(username)==usr and str(password)==pwd):
        if(diff2==diff or diff2==diff-1 or diff2==diff+1):
            login_btn.configure(text="login is sucessful")
        else:
            login_btn.configure(text="login failed")



def enter_0():
    global time0
    if(len(usr_name_text.get())<1):
        enter0_btn.configure(text="do it again")
        usr_name_text.focus_set()
    else:
        enter0_btn.configure(text="done")
        password_text.focus_set()
        now0=datetime.now()
        time0 = int(now0.strftime("%S"))



def enter():
    global time_0
    if(len(password_text.get())<1):
        enter_btn.configure(text="do it again")
        password_text.focus_set()
    else:
        enter_btn.configure(text="done")
        now00 = datetime.now()
        time_0 = int(now00.strftime("%S"))


window=Tk()
window.geometry("300x100")
window.title("welcome to the login session")

label_1=Label(window,text="USERNAME:",font=("Arial Bold",15))
label_1.grid(column=0,row=0)
usr_name_text=Entry(window,width=20)
usr_name_text.grid(column=1,row=0)

label_2=Label(window,text="PASSWORD:",font=("Arial Bold",15))
label_2.grid(column=0,row=1)
password_text=Entry(window,width=20)
password_text.grid(column=1,row=1)
usr_name_text.focus_set()


login_btn=Button(window,text="login",command=login)
login_btn.grid(column=1,row=3)
exit_btn=Button(window,text="exit",command=exit)
exit_btn.grid(column=0,row=3)

enter0_btn=Button(window,text="enter",command=enter_0)
enter0_btn.grid(column=2,row=0)
enter_btn=Button(window,text="enter",command=enter)
enter_btn.grid(column=2,row=1)

window.mainloop()