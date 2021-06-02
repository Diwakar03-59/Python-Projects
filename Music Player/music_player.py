# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 08:49:52 2020

@author: DEEPAKKU
"""
from tkinter import *
import pygame
import os


class MusicPlayer:
    def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Chalu H")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()
    
    def stopsong(self):
        # Displaying Status
        self.status.set("-Band H")
        # Stopped Song
        pygame.mixer.music.stop()
    
    def pausesong(self):
        # Displaying Status
        self.status.set("-Ruk Gya")
        # Paused Song
        pygame.mixer.music.pause()
    
    def unpausesong(self):
        # It will Display the  Status
        self.status.set("-Chalu H")
        # Playing back Song
        pygame.mixer.music.unpause()
    
    def __init__(self,root):
        self.root = root
        self.root.title("Pythoon ka Gaana Player")
        # Window Geometry
        self.root.geometry("1000x200+200+200")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()
    
        # Creating the Track Frames for Song label & status label
        trackframe = LabelFrame(self.root,text="Baj Rahe Geet ka naam",font=("times new roman",15,"bold"),bg="yellow",fg="black",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=600,height=100)
        # Inserting Song Track Label
        songtrack = Label(trackframe,textvariable=self.track,width=29,font=("times new roman",20,"bold"),bg="black",fg="yellow").grid(row=0,column=0,padx=5,pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",18,"bold"),bg="black",fg="yellow").grid(row=0,column=1,padx=5,pady=5)
    
        # Creating Button Frame
        buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="black",fg="yellow",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)
        # Inserting Play Button
        playbtn = Button(buttonframe,text="SHURU KARE",command=self.playsong,width=12,height=1,font=("times new roman",16,"bold"),fg="black",bg="yellow").grid(row=0,column=0,padx=5,pady=5)
        # Inserting Pause Button
        playbtn = Button(buttonframe,text="RUK JAE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="black",bg="yellow").grid(row=0,column=1,padx=5,pady=5)
        # Inserting Unpause Button
        playbtn = Button(buttonframe,text="CHALU RAKHE",command=self.unpausesong,width=13,height=1,font=("times new roman",16,"bold"),fg="black",bg="yellow").grid(row=0,column=2,padx=4,pady=5)
        # Inserting Stop Button
        playbtn = Button(buttonframe,text="BAND KARE",command=self.stopsong,width=10,height=1,font=("times new roman",16,"bold"),fg="black",bg="yellow").grid(row=0,column=3,padx=5,pady=5)
    
        # Creating Playlist Frame
        songsframe = LabelFrame(self.root,text="Geeton ki Suchi",font=("times new roman",15,"bold"),bg="black",fg="yellow",bd=5,relief=GROOVE)
        songsframe.place(x=600,y=0,width=400,height=200)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="yellow",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="black",fg="yellow",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("C:/Users/DEEPAKKUMAR/Music/Playlists")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
          self.playlist.insert(END,track)
      
   
root = Tk()
MusicPlayer(root)
root.mainloop()
      
      
      


    