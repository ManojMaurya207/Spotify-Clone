import pygame
from customtkinter import *
from PIL import Image
from tkinter import filedialog
import eyed3
from Doubly_linked_list import *
import tkinter.messagebox as messagebox

p1 = Playlist()
s1 = Song("Calm Down", "Rema, Selena Gomez", r'Music\Rema, Selena Gomez - Calm Down (Official Music Video).mp3')
s2 = Song("Best day of my life", "Unknown", r"Music\American Authors - Best day of my life (lyrics) (1).mp3")
s3 = Song("O Mere Dil Ke Chain", "Kishore Kumar", r"Music/O Mere Dil Ke Chain (From _Mere Jeevan Saathi_).mp3")
p1.addSong(s1)
p1.addSong(s2)
p1.addSong(s3)



def search_display():
    name=sr_t.get()
    obj=p1.search(name)
    if obj==None:
        messagebox.showinfo("Song not Found", "try again")
    else:
        list_f1=CTkFrame(window,width=485,height=200,border_color="#1DB954",border_width=4,corner_radius=40,bg_color="#191414")
        list_f1.place(relx=0.64,rely=0.28,anchor=CENTER)
        new_b=CTkButton(list_f1,text=obj.name,height=55,width=390,command=lambda a=obj: change_current(a) ,border_width=2,corner_radius=20,border_color="black",text_color="white",fg_color="#191414",font=CTkFont("Helvetica",20))
        new_b.place(relx=0.54,rely=0.46,anchor=CENTER)
        icon=CTkImage(Image.open("musical_note.png"),size=(40,40))
        new_l=CTkLabel(new_b,image=icon,text='',height=40,width=40,text_color="black",fg_color="#191414")
        new_l.place(x=70,rely=0.5,anchor="e")

def Update_cover():
    global cover_img, cover_name, cover_artist
    cover_name.configure(text=p1.curr_song.name)
    cover_artist.configure(text=p1.curr_song.artist)
    try:
        photo_address = extract_img_path(p1.curr_song.address)
        cover_photo = Image.open(photo_address)
    except Exception :
        cover_photo = Image.open("Disk_cover.png") 
    cover_photo = CTkImage(cover_photo, size=(300, 300))
    cover_img.configure(image=cover_photo)


def load():
    global progressbar_1
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(p1.curr_song.address)
    pygame.mixer.music.play()
    play_but.configure(image=pause_img)
    Update_cover()
    progressbar_1.set(0)
    progressbar_1.start()
    playlist()

#To play and pause music
play=False
def play_pause():
    global play,play_img,play_but,pause_img
    if play:
        progressbar_1.start()
        pygame.mixer.music.unpause()
        play_but.configure(image=pause_img)
        play=False
    else:
        progressbar_1.stop()
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
l1.place(relx=0.115,rely=0.07,anchor=CENTER)
photo=CTkImage(Image.open("prev.png"),size=(60,60))
prev_b=CTkButton(main_f,image=photo,corner_radius=10,hover_color='#585858',text=" ",bg_color="#191414",fg_color="#191414",width=10,command=previous_song)
prev_b.place(relx=0.18,rely=0.84,anchor=CENTER)
window.bind('<Left>', lambda event=None: prev_b.invoke())
play_img=CTkImage(Image.open("play.png"),size=(60,60))
pause_img=CTkImage(Image.open("pause.png"),size=(60,60))
play_but=CTkButton(main_f,image=play_img,corner_radius=10,hover_color='#585858',text=" ",bg_color="#191414",fg_color="#191414",width=10,command=play_pause)
play_but.place(relx=0.24,rely=0.84,anchor=CENTER)
window.bind('<space>', lambda event=None: play_but.invoke())
photo=CTkImage(Image.open("next.png"),size=(60,60))
next_b=CTkButton(main_f,image=photo,corner_radius=10,hover_color='#585858',text=" ",bg_color="#191414",fg_color="#191414",width=10,command=next_song)
next_b.place(relx=0.3,rely=0.84,anchor=CENTER)
window.bind('<Right>', lambda event=None: next_b.invoke())

#Player Cover
player_f=CTkFrame(window,width=500,height=500,corner_radius=40,border_color="#1DB954",border_width=15,bg_color="#191414")
player_f.place(relx=0.24,rely=0.46,anchor=CENTER)
cover_photo=CTkImage(Image.open("Disk_cover.png"),size=(300,300))
cover_img=CTkLabel(player_f,image=cover_photo,text=" ")
cover_img.place(relx=0.5,rely=0.4,anchor=CENTER)
cover_name=CTkLabel(player_f,text="Unkown",font=("Franie Text Font",30)) 
cover_name.place(relx=0.05,rely=0.85,anchor="w")
cover_artist=CTkLabel(player_f,text="Unkown",font=("Franie Text Font",20))
cover_artist.place(relx=0.05,rely=0.92,anchor="w")
progressbar_1 = CTkProgressBar(player_f,bg_color="#1C1F26",fg_color="#656669",progress_color="white",height=6,mode="determinate",width=500-50,determinate_speed=0.005)
progressbar_1.place(relx=0.5,rely=0.78,anchor="center")
progressbar_1.set(0)




#Search song
sr_t=CTkEntry(main_f,corner_radius=20,width=350,height=50,text_color='white',font=("Franie Text Font",18))
sr_t.place(relx=0.66,rely=0.07,anchor=CENTER)
photo=CTkImage(Image.open("search.png"),size=(50,50))
b1=CTkButton(main_f,image=photo,corner_radius=10,width=50,height=60,hover_color='#585858',command=search_display,text=" ",bg_color="#191414",fg_color="#191414")
b1.place(x=1220,y=30)




#Playlist

def playlist():
    photo=CTkImage(Image.open("play_queue.png"),size=(60,60))
    b1=CTkButton(main_f,image=photo,corner_radius=10,command=lambda a=p1.start: change_current(a),hover_color='#585858',text=" ",bg_color="#191414",fg_color="#191414",width=10)
    b1.place(relx=0.5,rely=0.06,anchor=CENTER)
    list_f=CTkScrollableFrame(window,width=485,height=455,border_color="#1DB954",border_width=8,corner_radius=40,bg_color="#191414")
    list_f.place(relx=0.64,rely=0.46,anchor=CENTER)
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
        new_b.grid(row=r,column=0,padx=0,pady=y_pad+10)

        bt_delete=CTkButton(list_f,image=delete,height=55,width=50,text="",command=lambda a=obj[i]: delete_song(a),border_width=2,corner_radius=20,border_color="black",text_color="white",fg_color="#191414",font=CTkFont("Helvetica",20))
        bt_delete.grid(row=r,column=1,padx=5,pady=y_pad+10)
        new_l=CTkLabel(new_b,image=icon,text='',height=40,width=40,text_color="black",fg_color="#191414")
        new_l.place(x=70,rely=0.5,anchor="e")
        r+=1
playlist()

def add_song():
    global select_lb
    add_f=CTkFrame(window,width=550,height=550,border_color="#1DB954",border_width=8,corner_radius=40,bg_color="#191414")
    add_f.place(relx=0.64,rely=0.46,anchor=CENTER)
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
            audiofile = eyed3.load(file_path)
            songnm=audiofile.tag.title
            artistnm=audiofile.tag.artist
            if songnm==None or artistnm==None:
                nm_t.insert(END,"Unknown")
                ar_t.insert(END,"Unknown")
            else:
                nm_t.insert(END,songnm)
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
add_b.place(relx=0.64,rely=0.86,anchor=CENTER)



window.mainloop()