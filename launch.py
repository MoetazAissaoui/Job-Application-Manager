from tkinter import *
from tkinter import messagebox
import admin
import jobseeker



"""
Author : Moetaz Aissaoui
Python3.* , Tkinter GUI
All data will be stored in TXT files
"""

def Preveillage(Auth,password):
    
    if(password == "admin"):
        msg=messagebox.showinfo("INFO","Welcome Administartor")
        admin.adminspace()
    else:
        if password == "jobseeker":
            msg=messagebox.showinfo("INFO","Welcome Job Seeker")
            Auth.destroy()
            jobseeker.JOBS()
        else:
            print("you are unauthorized")
            msg=messagebox.showinfo("Warning","You are not authorized , please contact administator")


def Authentication(_const):
    _const.destroy()
    Auth=Tk()
    Auth.geometry("400x200")
    Auth.title("Authentication Page")
    L2=Label(Auth,text="Password")
    L2.pack(side=LEFT)
    E2=Entry(Auth,justify="center")
    E2.pack(side=LEFT)
    B2=Button(Auth,text="Login",command=lambda:Preveillage(Auth,E2.get()))
    B2.pack(side=LEFT)
    Auth.mainloop()



main=Tk()

main.geometry("400x200")
main.title("Recrutement Company")

L1=Label(main,text="Welcom to our Company")
L1.pack()

B1=Button(main,text="Login",command=lambda:Authentication(main))
B1.pack()


main.mainloop()
