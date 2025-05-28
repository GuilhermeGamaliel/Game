import pygame
from pygame import display, mixer, event
from pygame.locals import QUIT, KEYUP, K_SPACE
from pygame import font
from pygame.time import Clock
from pygame.transform import scale
from pygame.image import load
from random import randint

pygame.init()
mixer.init()
pygame.mixer.music.load("chopin.mp3")
pygame.mixer.music.play(-1)
estado = 0
info = display.Info()
largura = info.current_w
altura = info.current_h
tela = display.set_mode((altura, largura), pygame.FULLSCREEN)
display.set_caption("Praticando matemática")

fonte = pygame.font.SysFont("Garamond", 30)
texto = fonte.render("Novo jogo!", True, (255, 255, 255))


tela.fill((0, 255, 255))
pygame.display.flip()


while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    match estado:
        case 0:
            pass
            
            


    display.update()

