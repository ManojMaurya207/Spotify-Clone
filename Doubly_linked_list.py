class Song:
    def __init__(self, name, artist, address):
        self.next = None
        self.prev = None
        self.address=address
        self.name=name
        self.artist=artist


class Playlist:
    def __init__(self):
        self.start = None
        self.last = None
        self.curr_song = None

    def addSong(self, music):
        if self.start is None and self.last is None:
            self.start = music
            self.last = music
        else:
            self.last.next = music
            music.prev = self.last
            self.last = music
        self.curr_song = self.last

    def next(self):
        if self.curr_song.next==None:
          self.curr_song=self.start
          return self.curr_song
        else:
          self.curr_song=self.curr_song.next
          return self.curr_song
        
    def back(self):
        if self.curr_song.prev==None:
          self.curr_song=self.last
          return self.curr_song
        else:
          self.curr_song=self.curr_song.prev
          return self.curr_song
    
    def traverse(self):
        info=[]
        obj=[]
        ptr=self.start
        while (ptr!=None):
            det={'name':ptr.name,'artist':ptr.artist,'address':ptr.address}
            info.append(det)
            obj.append(ptr)
            ptr=ptr.next
        return info,obj

    def delete(self, song_obj):
        if song_obj == self.start:
            self.start = self.start.next if self.start.next else None
            if self.curr_song == song_obj:
                self.curr_song = self.start
        elif song_obj == self.last:
            self.last = self.last.prev
            self.last.next = None
            if self.curr_song == song_obj:
                self.curr_song = self.start
        else:
            song_obj.prev.next = song_obj.next
            song_obj.next.prev = song_obj.prev
            if self.curr_song == song_obj:
                self.curr_song = self.start

    def search(self, song_name):
        ptr=self.start
        while ptr != None:
            if ptr.name.lower()==song_name.lower():
                return ptr
            else:
                ptr=ptr.next
        return ptr







from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image
import io
import os

def extract_img_path(mp3_file):
    try:
        # Open the MP3 file using mutagen
        audio = MP3(mp3_file, ID3=ID3)

        for tag in audio.tags:
            if tag.startswith("APIC"):
                album_art = audio.tags[tag].data
                image_format = audio.tags[tag].mime.split("/")[1]
                image = Image.open(io.BytesIO(album_art))

                # Save album art as a PNG file
                output_file = os.path.join(".", "album_art.png")
                image.save(output_file, "PNG")

                return output_file[2:]

    except Exception as e:
        return None