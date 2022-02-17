"""
Author: github.com/Ariocodes
This is a mini code showing how Pseudorandom generates random numbers.
"""
import tkinter as tk, pygame, os
from tkinter import *
pygame.init()
pygame.mixer.init()
from pygame.mixer import music

number=1

# Functions
def play():
    global number
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume.get())
    number = 1

def pause():
    pygame.mixer.music.pause()
    print(music.get_pos())
    
def volume_change(a):
    b = volume.get()
    pygame.mixer.music.set_volume(b)

def unpause():
    pygame.mixer.music.unpause()

def pause_unpause():
    global number
    if number % 2:
        pauseUnpauseBtn.config(text="\u25b6")
        pause()
    else:
        pauseUnpauseBtn.config(text="||")
        unpause()
    number +=1


# Screen
root = tk.Tk()
icon = PhotoImage(file = "sai.png")
root.geometry("600x400")
root.title("TOP Player \u03c8")
root.iconphoto(False, icon)
root.config(bg= "#79c5e0")
root.pack_propagate(0)
root.resizable(0, 0)

bg = PhotoImage(file = "bg1.png")
background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

var = tk.StringVar()
musicTitle = tk.Label(root, textvariable=var, background="#79c5e0")
playlist = tk.Listbox(width=21, height=11, activestyle="none", 
                        background="#79c5e0", relief=FLAT)
os.chdir("songs/")
musicList = os.listdir()
print(musicList)
i = 0
for item in musicList:
    if item.endswith(".mp3"):
        playlist.insert(i, item)
        i += 1

# Widgets
pauseUnpauseBtn = tk.Button(root, width=10, height=2, background="#79c5e0",
                        activeforeground="#79c5e0", activebackground="#79c5e0", text="||", command=pause_unpause)

playBtn = tk.Button(root, width=10, height=2, background="#79c5e0", 
                    activeforeground="#79c5e0", activebackground="#79c5e0", 
                    text="\u03c8", command=play)  # \|/

volume = tk.Scale(root, from_=0, to_=1, length=400, resolution=0.01, border=0, 
                    relief=FLAT, background="#79c5e0", activebackground="#79c5e0", 
                    command=volume_change, orient=VERTICAL)
volume.set(1)



# Pack
print('\u03c8')
playlist.place(x=-1, y=0-1)
volume.place(x=556, y=-1)
musicTitle.place(x=250, y=350)
playBtn.place(x=450, y=20)
pauseUnpauseBtn.place(x=450, y= 65)

# Mainloop
tk.mainloop()
