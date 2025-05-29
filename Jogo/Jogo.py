import pygame
from pygame import display, mixer, event, draw, font, image, Rect
from pygame.locals import QUIT, KEYUP, K_SPACE
from pygame.time import Clock
from pygame.transform import scale
from random import randint

pygame.init()
mixer.init()
pygame.mixer.music.load("chopin.mp3")
pygame.mixer.music.play(-1)
estado = 0
info = display.Info()
largura = info.current_w
altura = info.current_h
centro_da_tela = largura/2
tela = display.set_mode((altura, largura), pygame.FULLSCREEN)
display.set_caption("Praticando matemática")




#ret = pygame.Rect(centro_da_tela,centro_da_tela,(100,100))
#draw.rect(tela, (255,255,255), ret)


display.flip()



while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_novo_jogo.collidepoint(evento.pos):
                estado = 1
            elif rect_fechar.collidepoint(evento.pos):
                pygame.quit()
                exit()
    match estado:
        case 0:
            cor_titulo = (250,0,50)
            tela.fill((0, 255, 255))

            fonte_titulo = font.SysFont("Comic Sans", 60)
            fonte_texto = font.SysFont("Garamond", 30)

            texto = fonte_titulo.render("Praticando Matemática!", True, cor_titulo)
            tela.blit(texto, ((largura/16),(altura/16)))

            rect_novo_jogo = Rect(((largura/8)-30), ((altura/4)-15), 350, 50)
            draw.rect(tela, (0, 200, 200), rect_novo_jogo, 0, 50)
            texto = fonte_texto.render("Novo jogo!", True, (0, 0, 0))
            tela.blit(texto, ((largura*2/16),(altura/4)))

            rect = Rect(((largura/8)-30),((altura/2)-15), 350, 50)
            draw.rect(tela, (0, 200, 200), rect, 0, 50)
            texto = fonte_texto.render("Carregar jogo salvo", True, (0,0,0))
            tela.blit(texto, ((largura*2/16),(altura/2)))

            rect_fechar = Rect(((largura/8)-30),((altura*3/4)-15), 350, 50)
            draw.rect(tela, (0, 200, 200), rect_fechar, 0, 50)
            texto = fonte_texto.render("Fechar o jogo", True, (0,0,0))
            tela.blit(texto,((largura/8),(altura*3/4)))

            imagem = image.load("Menino com lápis gigante alegre.jpg")
            tela.blit(imagem,((largura*3/4),(altura/2)))
        case 1:
            tela.fill((0, 255, 255))


            
            pass
            
            
            


    display.update()

