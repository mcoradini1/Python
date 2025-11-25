#fazer um programa que que le um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('chronotrigger.mp3')
pygame.mixer.music.play()
pygame.event.wait()
