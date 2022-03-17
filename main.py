from argparse import FileType
import tkinter as tk
from tkinter import *
import pytube
import os

def Downloader():
    global link_e
    global filename_e
    link = link_e.get()
    file = filename_e.get()
    
    url = pytube.YouTube(link)
    video = url.streams.get_highest_resolution()
    video.download(filename = ("{}.mp4").format(file), output_path = (os.path.join("yt downloads")))
    Label(win, text = ' VIDEO DOWNLOADED').place(x= 180 , y = 210)

def Downloader_mp3():
    global link_e
    global filename_e
    link = link_e.get()
    file = filename_e.get()
        
    url = pytube.YouTube(link)
    video = url.streams.get_highest_resolution()
    video.download(filename = ("{}.mp3").format(file), output_path = (os.path.join("yt downloads")))
    Label(win, text = ' VIDEO DOWNLOADED').place(x= 180 , y = 210)
    
win = Tk()
win.title("YT downloader")
win.geometry('600x400')

global link_e
global filename_e

Link_l = Label(win, text = 'Link:').grid(row=0, column=0)
link_e = Entry(win, width = 70)
link_e.grid(row=0, column=1)


filename_l = Label(win, text = 'Filename:').grid(row=2, column=0)
filename_e = Entry(win, width = 70)
filename_e.grid(row=2, column=1)


Button(win, text = 'DOWNLOAD .mp4', command = Downloader).grid(row=3, column=0)
Button(win, text = 'DOWNLOAD .mp3', command = Downloader_mp3).grid(row=3, column=1)
win.mainloop()