import pygame
pygame.mixer.init()
pygame.mixer.music.load('exe021.mp3')
#a faixa da música precisa estar na pasta onde o programa está salvo
pygame.mixer.music.play()
input()
pygame.event.wait()