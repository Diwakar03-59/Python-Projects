from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x200')
root.resizable(0,0)
root.title("Uthoob BolTe")


track=LabelFrame(text="Youtube Material Downloader",font=("algerian",15,"bold"),bg="yellow",fg="black",bd=5,relief=GROOVE)
track.place(x=0,y=0,width=500,height=60)


##enter link
link = StringVar()

task=LabelFrame(text="Enter the Link here",font=("algerian",15,),bg="orange",fg="black",bd=10,relief=GROOVE)
task.place(x=0,y=60,width=500,height=90)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Button(root,text = 'DOWNLOADED', font = 'algerian 15 bold' ,bg = 'orange', padx = 2).place(x=180,y=150)
    
    


Button(root,text = 'DOWNLOAD', font = 'algerian 15 bold' ,bg = 'orange', padx = 2,command = Downloader).place(x=180,y=150)


root.mainloop()
