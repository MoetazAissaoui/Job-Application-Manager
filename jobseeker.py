from tkinter import *
from tkinter import messagebox
from os import remove
import os
import glob

def list_jobs(field):

    if field == "":
        msg=messagebox.showinfo("Warning","Error Field is empty !")
        return 0

    #jobs list
    lis=glob.glob("./Jobs/*.txt")
    data = []
    njobs=0
    jobs=""
    
    for i in lis:
        f=open(i,"r")
        for k in f:
            data.append(k.split(" : ")[len(k.split(" : "))-1].strip())
        f.seek(0)
        if field.upper() in map(lambda x:x.upper(),data):
            njobs+=1
            jobs+=f.read()+"\n\n"
    

    if njobs == 0:
        msg=messagebox.showinfo("Warning","There is no Jobs for this Field!")
    else:
        #Creating widget structre
        msg=messagebox.showinfo("Info","There is {} Jobs in this Field!".format(njobs))
        job=Tk()
        text=Text(job)
        text.insert(INSERT,jobs)
        text.pack()
    
def job_offers():
    #tkinter constuctor
    job=Tk()
    job.geometry("400x200")
    job.title("Job Offers")

    L1=Label(job,text="Search")
    L1.pack(side=LEFT)

    E1=Entry(job)
    E1.pack(side=LEFT)

    B1=Button(job,text="Submit Query",command=lambda:list_jobs(E1.get().strip()))
    B1.pack(side=LEFT)




    #start sequence    
    job.mainloop()


def show_jobs():
    lis=glob.glob("./Jobs/*.txt")

    if len(lis) == 0:
        msg=messagebox.showinfo("Warning","There is No Jobs Available")
    else:
        show=Tk()
        text=Text(show)
        njobs=0

        for i in lis:
            f=open(i,'r')
            text.insert(INSERT,f.read()+"\n\n")
            njobs+=1
        text.pack()
        msg=messagebox.showinfo("Info","There is {} jobs available .".format(njobs) )


def Get_FromFile(textarea,src):
    tmp=open("tmp.txt","w+")
    tmp.write(textarea)
    tmp.seek(0)
    for i in tmp:
        if src in i:
            return i.split(":")[1].strip()
    remove("tmp.txt")

def exist_job(job):
    listjobs=glob.glob("./Jobs/*.txt")
    
    exist=False
    for i in listjobs:
        #opening file
        f=open(i,"r")
        if Get_FromFile(f.read(),"JOB_ID") == job:
            exist=True
    return exist

def save_applicant(env,textarea):


    if exist_job(Get_FromFile(textarea,"JOB_ID")) == True and os.path.exists("./JobSeekers/"+Get_FromFile(textarea,"ID Card")+".txt") == True:
        f=open("./JobApplicants/{}_{}_JOB{}.txt".format(Get_FromFile(textarea,"ID Card"),Get_FromFile(textarea,"Name"),Get_FromFile(textarea,"JOB_ID")),"w+")
        f.write(textarea)
        env.destroy()
        msg=messagebox.showinfo("Info","Application saved !")
    else:
        msg=messagebox.showinfo("Warning","Invalid Job ID/ID Card")

def apply_job():
    show=Tk()
    text=Text(show)
    text.insert(INSERT,"JOB_ID : \n\nPersonal Info  \n\nID Card : \nName : \nAdresse : \nPhone : \n\nProfessional info  \n\nExperience : \nSkills : \n")
    text.pack()
    B=Button(show,text="Apply",command=lambda:save_applicant(show,text.get("1.0",END)))
    B.pack(side=RIGHT)


def list_apply_job():
    #tkinter constuctor
    job=Tk()
    job.geometry("400x200")
    job.title("Show & Apply for a job")

    B1=Button(job,text="Show Available Jobs",command=show_jobs)
    B1.pack(side=LEFT)

    B2=Button(job,text="Apply for a job",command=apply_job)
    B2.pack(side=LEFT)



def apply_changes(id,textarea):
    f=open("JobSeekers/"+id+".txt","w")
    f.write(textarea)
    msg=messagebox.showinfo("Info",id+" Updated")


def update_seeker(constructor,id):
    B=Button(constructor,text="Apply Changes",command=lambda:apply_changes(id,text.get("1.0",END)))
    B.pack()
    try:

        f=open("JobSeekers/"+id+".txt","r")
        print("existing")
        text=Text(constructor)
        text.insert(INSERT,f.read())
        text.pack()

    except IOError: #if the file does not exist
        msg=messagebox.showinfo("Warning","User does not exist please Add it")
        text=Text(constructor)
        text.insert(INSERT,"Name : \nLastName : \nPhone : \nAge : ")
        text.pack()
            
    

def update_jobseeker():
    update=Tk()
    update.geometry("550x200")

    L1=Label(update,text="ID Card")
    L1.pack(side=LEFT)

    E1=Entry(update)
    E1.pack(side=LEFT)

    B1=Button(update,text="Submit Query",command=lambda:update_seeker(update,E1.get()))
    B1.pack(side=LEFT)

    update.mainloop()
    
    
    
def JOBS():
    #tkinter constructor
    main=Tk()

    main.geometry("400x200")
    main.title("Recrutement Company")

    L1=Label(main,text="Job Seeker Panel")
    L1.pack()

    B1=Button(main,text="Search a job",command=job_offers)
    B1.pack()

    B2=Button(main,text="Show & Apply for a job",command=list_apply_job)
    B2.pack()

    B3=Button(main,text="Update Your Information",command=update_jobseeker)
    B3.pack()

    main.mainloop()