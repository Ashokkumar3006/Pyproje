import tkinter as tk
import fnmatch
import os
from  pygame import mixer
ash=tk.Tk()
ash.title("Music Player")
ash.geometry("600x900")
ash.config(bg="black")

rootpath=r"C:\Users\Lenovo\Desktop\music"

pattern="*.mp3"

listBox=tk.Listbox(ash,fg="cyan",bg="black",width= 150,font=('roman',14))
listBox.pack(padx=15,pady=15)

label=tk.Label(ash,text=" ",bg="black",fg="red",font=('roman',18))
label.pack(pady=17)

top=tk.Frame(ash,bg="black")
top.pack(padx=10,pady=8,anchor="center")


#preview button
prevButton=tk.Button(ash,text="Prev")
prevButton.pack(pady=17,in_ = top,side="left")

#next button
nextButton=tk.Button(ash,text="Next")
nextButton.pack(pady=17,in_ = top,side="left")

#Pause button
PauseButton=tk.Button(ash,text="Pause")
PauseButton.pack(pady=17,in_ = top,side="left")

#play button
PlayButton=tk.Button(ash,text="Play")
PlayButton.pack(pady=17,in_ = top,side="left")


for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern): #matching files with pattern
        listBox.insert("end",filename)

ash.mainloop()
