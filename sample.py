import glob
import pygame
import RPi.GPIO as GPIO
from time import sleep

pygame.init()
pygame.mixer.init()

MUSIC_ENDED = pygame.USEREVENT
pygame.mixer.music.set_endevent(MUSIC_ENDED)

files = glob.glob("/media/usb/*")
passlist = []

for file in files:
    if file.endswith('.mp3'):
        passlist.append(file)
        
print(passlist)
        
def run ():
    song_index = 0
    global passlist
    
    pygame.mixer.music.load(passlist[song_index])
    pygame.mixer.music.play()
    
    while True:
        for event in pygame.event.get():
            if event.type == MUSIC_ENDED:
                song_index += 1
                pygame.mixer.music.load(passlist[song_index])
                pygame.mixer.music.play()
                
run()





        
    