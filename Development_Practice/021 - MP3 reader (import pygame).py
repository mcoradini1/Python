#A PROGRAM TO READ AN MP3 ARCHIVE
import pygame
pygame.init()
pygame.mixer.music.load('chronotrigger.mp3')
pygame.mixer.music.play()
pygame.event.wait()
