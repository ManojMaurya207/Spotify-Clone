import pygame
import tkinter as tk
from tkinter import ttk
from customtkinter import *
from PIL import Image
from tkinter import filedialog
import os
from mutagen import File
from Doubly_linked_list import *


p1 = Playlist()
s1 = Song("Calm Down", "Manoj", r'Music\Rema, Selena Gomez - Calm Down (Official Music Video).mp3')
s2 = Song("Best day of my life", "Manoj", r"Music\American Authors - Best day of my life (lyrics).mp3")
s3 = Song("EXAM OVER", "Manoj", r"Music\EXAM OVER - VELOCITY EDIT  Exam CompleteStatus  Exam Status  #examover.mp3")
p1.addSong(s1)
p1.addSong(s2)
p1.addSong(s3)

def load():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(p1.curr_song.address)
    pygame.mixer.music.play()
    play_but.configure(image=pause_img)

#To play and pause music
play=False
def play_pause():
    global play,play_img,play_but,pause_img
    if play:
        pygame.mixer.music.unpause()
        play_but.configure(image=pause_img)
        play=False
    else:
        pygame.mixer.music.pause()
        play_but.configure(image=play_img)
        play=True



def next_song():
    global play
    pygame.mixer.music.stop()
    p1.next()
    play=False
    load()

def previous_song():
    global play
    pygame.mixer.music.stop()
    p1.back()
    play=False
    load()


def change_current(curr):
    global play
    play=False
    p1.curr_song=curr
    load()
    

def delete_song(obj):
    p1.delete(obj)
    playlist() 
#-----------------------------Window Working----------------------------------



set_appearance_mode('dark')
set_default_color_theme('dark-blue')
window=CTk()
window.title("Playlist")
main_f=CTkFrame(window,width=2000,height=1000,fg_color="#191414")
main_f.pack()
photo=CTkImage(Image.open("spotify.png"),size=(340,100))
l1=CTkLabel(main_f,image=photo,text=" ")
l1.place(x=18,y=30)



#Player 
player_f=CTkFrame(window,width=580,height=460,corner_radius=40,border_color="#1DB954",border_width=15,bg_color="#191414")
player_f.place(x=70,y=150)
photo=CTkImage(Image.open("prev.png"),size=(60,60))
prev_b=CTkButton(main_f,image=photo,corner_radius=10,hover_color='#585858',text=" ",bg_color="#191414",fg_color="#191414",width=10,command=previous_song)
prev_b.place(x=190,y=630)
play_img=CTkImage(Image.open("play.png"),size=(60,60))
pause_img=CTkImage(Image.open("pause.png"),size=(60,60))
play_but=CTkButton(main_f,image=play_img,corner_radius=10,hover_color='#585858',text=" ",bg_color="#191414",fg_color="#191414",width=10,command=play_pause)
play_but.place(x=300,y=630)
photo=CTkImage(Image.open("next.png"),size=(60,60))
next_b=CTkButton(main_f,image=photo,corner_radius=10,hover_color='#585858',text=" ",bg_color="#191414",fg_color="#191414",width=10,command=next_song)
next_b.place(x=410,y=630)



#Playlist
def playlist():
    photo=CTkImage(Image.open("play_queue.png"),size=(60,60))
    b1=CTkButton(main_f,image=photo,corner_radius=10,command=lambda a=p1.start: change_current(a),hover_color='#585858',text=" ",bg_color="#191414",fg_color="#191414",width=10)
    b1.place(x=760,y=23)
    # search for songs   
    sr_t=CTkEntry(main_f,corner_radius=20,width=270,height=40,text_color='white',font=("Franie Text Font",18))
    sr_t.place(x=950,y=40)
    photo=CTkImage(Image.open("search.png"),size=(50,50))
    b1=CTkButton(main_f,image=photo,corner_radius=10,hover_color='#585858',text=" ",bg_color="#191414",fg_color="#191414",width=10)
    b1.place(x=1220,y=30)
    list_f=CTkScrollableFrame(window,width=500,height=455,border_color="#1DB954",border_width=8,corner_radius=40,bg_color="#191414")
    list_f.place(x=750,y=100)
    l1=CTkLabel(list_f,text='Your Playlist',font=("Franie Text Font",30),width=20,height=15,text_color="#ffffff")
    l1.grid(row=0,column=0,padx=1)
    result,obj=p1.traverse()
    r=1
    y_pad=0
    icon=CTkImage(Image.open("musical_note.png"),size=(40,40))
    delete=CTkImage(Image.open("delete.png"),size=(40,40))
    for i in range(len(result)):
        song_nm=result[i]['name']
        song_at=result[i]['artist']
        song_add=result[i]['address']
        new_b=CTkButton(list_f,text=song_nm,height=55,width=390,command=lambda a=obj[i]: change_current(a),border_width=2,corner_radius=20,border_color="black",text_color="white",fg_color="#191414",font=CTkFont("Helvetica",20))
        new_b.grid(row=r,column=0,padx=5,pady=y_pad+10)

        bt_delete=CTkButton(list_f,image=delete,height=55,width=50,text="",command=lambda a=obj[i]: delete_song(a),border_width=2,corner_radius=20,border_color="black",text_color="white",fg_color="#191414",font=CTkFont("Helvetica",20))
        bt_delete.grid(row=r,column=1,padx=5,pady=y_pad+10)
        new_l=CTkLabel(new_b,image=icon,text='',height=40,width=40,text_color="black",fg_color="#191414")
        new_l.place(x=70,rely=0.5,anchor="e")
        r+=1
playlist()

def add_song():
    global select_lb
    add_f=CTkFrame(window,width=565,height=550,border_color="#1DB954",border_width=8,corner_radius=40,bg_color="#191414")
    add_f.place(x=750,y=100)
    b1=CTkLabel(main_f,text=" ",bg_color="#191414",fg_color="#191414",width=70,height=100)
    b1.place(x=770,y=23)
    nm_lb=CTkLabel(add_f,text="Name",text_color='white',font=("Franie Text Font",25),width=100,height=30)
    nm_lb.place(x=30,y=40)
    nm_t=CTkEntry(add_f,corner_radius=20,width=270,height=40,text_color='white',font=("Franie Text Font",18))
    nm_t.place(x=200,y=38)
    ar_lb=CTkLabel(add_f,text="Artist",text_color='white',font=("Franie Text Font",25),width=100,height=30)
    ar_lb.place(x=30,y=140)
    ar_t=CTkEntry(add_f,corner_radius=20,width=270,height=40,text_color='white',font=("Franie Text Font",18))
    ar_t.place(x=200,y=138)
    fl_nm=CTkLabel(add_f,text="Select File",text_color='white',font=("Franie Text Font",25),width=100,height=30)
    fl_nm.place(x=30,y=240)

    def select_file():
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            audio = File(file_path)
            songnm=audio.get('title', 'Unknown')
            artistnm=audio.get('artist', 'Unknown')
            nm_t.insert(END,songnm[:30])
            ar_t.insert(END,artistnm)
            
            select_lb.configure(text_color='green',text='File Selected')
    f_bt=CTkButton(add_f,command=select_file,corner_radius=20,text="Browse File",fg_color="#1DB954",hover_color="#585858",width=200,height=40,text_color='black',font=("Franie Text Font",22))
    f_bt.place(x=200,y=238)
    select_lb=CTkLabel(add_f,text="No File Selected",height=35,width=160,corner_radius=20,text_color="red",font=CTkFont("Helvetica",20))
    select_lb.place(x=200,y=280)
    
    def add_sn():
        name=nm_t.get()
        artist=ar_t.get()
        text=select_lb.cget("text")
        if len(name)!=0 and len(artist)!=0 and text=='File Selected':
            song=Song(name,artist,file_path)
            p1.addSong(song)
            playlist()
        else:
            print('Fail to add song')
    add_bt=CTkButton(add_f,command=add_sn,corner_radius=20,text="Add",fg_color="#1DB954",hover_color="#585858",width=100,height=34,text_color='black',font=("Franie Text Font",22))
    add_bt.place(relx=0.5,rely=0.8,anchor=CENTER)

add_b=CTkButton(window,command=add_song,width=100,height=50,font=("Franie Text Font",30),hover_color="#585858",bg_color="#191414",text="Add Song",text_color='black',corner_radius=50,fg_color="#1DB954")
add_b.place(x=950,y=670)




# print(pygame.mixer.Sound(p1.curr_song.address).get_length())

window.mainloop()