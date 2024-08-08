import pygame
import time
from gtts import gTTS
from mutagen.mp3 import MP3
import time


text1 = input(str("Enter text: \n"))
print('\n------------Entered text--------------\n')
print(text1)
myobj = gTTS(text=text1, lang='en', slow =False)
myobj.save("voice.mp3")
print('\n------------Playing--------------\n')
song = MP3("voice.mp3")
pygame.mixer.init()
pygame.mixer.music.load('voice.mp3')
pygame.mixer.music.play()
time.sleep(song.info.length)
pygame.quit()
