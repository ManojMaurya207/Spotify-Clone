import os
import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize pygame
pygame.init()

# Create a function to play music
def play_music():
    global playlist, current_index
    if len(playlist) > 0:
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()
        status_label.config(text="Now Playing: " + os.path.basename(playlist[current_index]))

# Create a function to stop music
def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Music Stopped")

# Create a function to select a music directory
def choose_directory():
    global playlist, current_index
    directory = filedialog.askdirectory()
    if directory:
        playlist = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith((".mp3", ".wav"))]
        current_index = 0
        play_music()

# Create a function to play the next song in the playlist
def next_song():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    play_music()

# Create a function to play the previous song in the playlist
def prev_song():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    play_music()

# Create the main window
root = tk.Tk()
root.title("Music Player")

# Create and place widgets
choose_button = tk.Button(root, text="Choose Music Directory", command=choose_directory)
choose_button.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack()

next_button = tk.Button(root, text="Next", command=next_song)
next_button.pack()

prev_button = tk.Button(root, text="Previous", command=prev_song)
prev_button.pack()

status_label = tk.Label(root, text="Select a music directory")
status_label.pack(pady=10)

# Initialize playlist and current index
playlist = []
current_index = 0

# Run the Tkinter main loop
root.mainloop()










# directory = r"C:\Users\manoj\OneDrive\Desktop\MANOJ\SEM 3\Data Structures\Spotify Presentation\Music"
# if directory:
#     playlist = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith((".mp3", ".wav"))]
#     current_index = 0  # Clear the listbox
#     for song in playlist:
#         audiofile = eyed3.load(song)
#         songnm=audiofile.tag.title
#         artistnm=audiofile.tag.artist
#         if songnm==None or artistnm==None:
#             songnm="Unknown"
#             songnm="Unknown"
#         s1 = Song(songnm,songnm, song)
#         p1.addSong(s1)



# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3
# from PIL import Image
# import io
# import os

# def extract_img_path(mp3_file):
#     try:
#         # Open the MP3 file using mutagen
#         audio = MP3(mp3_file, ID3=ID3)

#         for tag in audio.tags:
#             if tag.startswith("APIC"):
#                 album_art = audio.tags[tag].data
#                 image_format = audio.tags[tag].mime.split("/")[1]
#                 image = Image.open(io.BytesIO(album_art))

#                 # Save album art as a PNG file
#                 output_file = os.path.join(".", "album_art.png")
#                 image.save(output_file, "PNG")

#                 return output_file[2:]

#     except Exception as e:
#         return None


