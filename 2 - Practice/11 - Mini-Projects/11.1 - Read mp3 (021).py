# ==========================================================================================================
# CHALLENGE 21: READ AND PLAY AN MP3 ARCHIVE
# ==========================================================================================================

"""
Challenge: 11.1 - Read mp3 (021)
Category: 11 - Mini-Projects
Concepts Used:
    - import pygame
    - init()
    - mixer.music.load()
    - pygame.mixer.music.play()
    - pygame.event.wait()


Tags: init(), mixer.music.load(), pygame.mixer.music.play(), pygame.event.wait()
Status: ✔️ Completed
"""

import pygame
pygame.init()
pygame.mixer.music.load('chronotrigger.mp3')
pygame.mixer.music.play()
pygame.event.wait()
