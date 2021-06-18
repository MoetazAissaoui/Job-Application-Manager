from tkinter import *
from tkinter import messagebox
import os
import glob




def Administrator():
    msg=messagebox.showinfo("Administrator","Welcom Admin")
    """
    admin=Tk()
    admin.title("This is Admin panel")
    
    admin.mainloop()
    """

def Get_FromFile(textarea,src):
    tmp=open("tmp.txt","w+")
    tmp.write(textarea)
    tmp.seek(0)
    for i in tmp:
        if src in i:
            return i.split(":")[1].strip()
    #os.remove("tmp.txt")

def save_job(textarea):
    if Get_FromFile(textarea,"JOB_ID") == "":
        messagebox.showinfo("Warning","Job ID is empty !")
    else:
        if os.path.exists("Jobs/{}.txt".format(Get_FromFile(textarea,"JOB_ID"))):
            messagebox.showinfo("Warning","Job ID Already Exist")
        else:
            #job does not exist , we save it
            f=open("Jobs/{}.txt".format(Get_FromFile(textarea,"JOB_ID")),"w+")
            f.write(textarea)
            messagebox.showinfo("info","Job saved !")

def add_job_offer():
    main=Tk()
    text=Text(main)
    text.insert(INSERT,"JOB_ID : \n\nCompany Info  \n\nName : \nAdresse : \nPhone : \nEmail : \nField : \nCountry : \n\n\nRequested Profile  \n\nDegree : \nExperience : \nQualifications : \n")
    text.pack()
    B=Button(main,text="Submit",command=lambda:save_job(text.get("1.0",END)))
    B.pack(side=RIGHT)


def save (file,textarea,_const):
    f=open(file,"w")
    f.write(textarea)
    messagebox.showinfo("Info","Job Saved !")
    _const.destroy()

def saveupdatedjob(constructor,jobid):
    print("/Jobs/"+jobid+".txt")
    if os.path.exists("./Jobs/"+jobid+".txt"): #job fileexist !
        constructor.destroy()
        constructor=Tk()
        text=Text(constructor)
        text.pack()
        #opening job file
        f=open("./Jobs/"+jobid+".txt","r")
        text.insert(INSERT,f.read())
        f.close()


        b=Button(constructor,text="Apply changes",command=lambda:save("./Jobs/"+jobid+".txt",text.get("1.0",END),constructor) )
        b.pack(side=RIGHT)
        
    else: #job file exist
        messagebox.showinfo("Warning","Job Does Not Exist !")


def update_job():
    main=Tk()
    main.geometry("400x200")
    L=Label(main,text="Job ID :")
    L.pack(side=LEFT)
    E=Entry(main)
    E.pack(side=LEFT)
    B=Button(main,text="Update",command=lambda:saveupdatedjob(main,E.get()))
    B.pack(side=LEFT)

    main.mainloop()


def delete(jobid):

    if os.path.exists("./Jobs/"+jobid+".txt"): #job fileexist !
        os.remove("./Jobs/"+jobid+".txt")
        messagebox.showinfo("info","Job Removed From Records !")
    else: #job file exist
        messagebox.showinfo("Warning","There is no job with this ID")



def delete_job():

    main=Tk()
    main.geometry("400x200")
    L=Label(main,text="Job ID :")
    L.pack(side=LEFT)
    E=Entry(main)
    E.pack(side=LEFT)
    B=Button(main,text="Delete",command=lambda:delete(E.get()))
    B.pack(side=LEFT)

    main.mainloop()




def show_all_applicants():
    main=Tk()
    main.geometry("500x650")
    lis=glob.glob("./JobApplicants/*.txt")
    if len(lis) == 0:
        msg=messagebox.showinfo("Warning","There is no job applicants")
    else:
        L=Label(main,text="All Job Applicants :")
        L.pack(side=LEFT)
        text=Text(main)
        text.pack(side=RIGHT)

    

    for i in lis:
        f=open(i,"r")
        text.insert(INSERT,f.read())
        text.insert(INSERT,"======================= \n\n")



def list_applicant(_const,jobid):
    if not os.path.exists("./Jobs/"+jobid+".txt"):
        msg=messagebox.showinfo("Warning","Wrong/Inexistant Job ID")
    else:
        lis=glob.glob("./JobApplicants/*.txt")
        if len(lis) == 0:
            msg=messagebox.showinfo("Warning","There is no job applicants")
        else:
            print(lis)
            text=Text(_const)
            text.pack(side=RIGHT)
            text.insert(INSERT,"Listing Applicants that applied for Job N: "+jobid+"\n\n")
            for i in lis :
                
                print(i)
                f=open(i,"r")
                f=f.read()
                if "JOB_ID : "+jobid in f:
                    text.insert(INSERT,f+"\n\n")


def show_same_applicants():
    main=Tk()
    main.geometry("500x650")

    L=Label(main,text="Job ID :")
    L.pack(side=LEFT)

    E=Entry(main)
    E.pack(side=LEFT)

    B=Button(main,text="submit",command=lambda:list_applicant(main,E.get()))
    B.pack(side=LEFT)



def list_JobSeekers():

    main=Tk()
    main.geometry("400x200")
    B=Button(main,text="All Applied Job Seekers",command=show_all_applicants)
    B.pack(side=LEFT)

    B2=Button(main,text="Same Job Applicants",command=show_same_applicants)
    B2.pack(side=LEFT)
    main.mainloop()



def adminspace():
    #tkinter constructor
    main=Tk()

    main.geometry("400x200")
    main.title("Administration Company")

    L1=Label(main,text="Administrator")
    L1.pack()

    B1=Button(main,text="Add new Job Offer",command=add_job_offer)
    B1.pack()

    B2=Button(main,text="Show & Update a job offer",command=update_job)
    B2.pack()

    B3=Button(main,text="Delete Job Offer",command=delete_job)
    B3.pack()

    B4=Button(main,text="Brows Job seekers",command=list_JobSeekers)
    B4.pack()

    main.mainloop()
