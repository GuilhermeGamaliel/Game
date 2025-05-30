import pygame
from pygame import display, mixer, event, draw, font, image, Rect
from pygame.locals import QUIT
from pygame.time import Clock
from pygame.transform import scale
from random import randint
#import playground

# O código que eu vou colocar abaixo era para funcionar como módulo do arquivo playground
# Mas como é 1:30 da manhã e eu não sei porque não tá funcionando eu vou colocar aqui mesmo
# é uma boa ideia tirar depois

#parte que preenche as listas
def preenchedor(nums1, nums2, teto, qnt_perguntas):
    for i in range(0, qnt_perguntas):
        nums1.append(randint(0,teto))
        nums2.append(randint(0,teto))

# A função somador tem a importante tarefa de construir a lista soma_nat
# A lista soma_nat funciona como um gabarito para as questões de soma
def somador(nums1, nums2, soma_nat, qnt_perguntas):
    preenchedor(nums1, nums2, teto, qnt_perguntas)
    for i in range(0, qnt_perguntas):
        soma_nat[i] = nums1[i] + nums2[i]

pygame.init()

# Música de fundo :)
mixer.init()
pygame.mixer.music.load("chopin.mp3")
#pygame.mixer.music.play(-1) 
# A última linha tá dentro de um comentário, porque a música tava chata e eu mandei parar de tocar XD

# Estado é a variável que carrega consigo a tela na qual estamos
estado = 0

fases = 15 
secoes = 4

# Variaveis que carregam as proporções da tela
# A ideia é que o jogo seja responsivo
info = display.Info()
largura = info.current_w
altura = info.current_h

tela = display.set_mode((altura, largura), pygame.FULLSCREEN)
display.set_caption("Praticando matemática")

# variaveis da pagina das fases
blocos_horizontal = 5
blocos_vertical = 3
blocos_total = blocos_horizontal * blocos_vertical

display.flip()

while True:
    for evento in event.get():
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

            #Imagem do protagonista do jogo
            imagem = image.load("Menino com lápis gigante alegre.jpg")
            #pygame.transform.scale(imagem,)
            tela.blit(imagem,((largura*3/4),(altura/2)))
            
        case 1:
            #Essa é a tela que tem as fases do jogo
            tela.fill((0, 255, 255))

            texto = fonte_titulo.render("Primeira parte do jogo(Adição)",True,(0,0,0))
            tela.blit(texto, ((largura/32),(altura/32)))

            tamanho_ret, pos_ret_x = largura/8, largura/8
            pos_ret_y = altura/8

            # O trambolho abaixo tá colocando as fases na tela
            
            blocos = []
            
            for i in range(1, blocos_vertical+1):
                for j in range(1, blocos_horizontal+1):
                    # Desenha a fase/bloco na tela
                    rect = Rect(j*(pos_ret_x+tamanho_ret/8), i*(pos_ret_y + tamanho_ret/2), tamanho_ret, tamanho_ret)
                    draw.rect(tela, (0, 200, 200), rect, 0, 25)
                    fase_id = i*j

                    # Enumera as fases
                    texto = fonte_texto.render(str(i*j),True,(0,0,0))
                    tela.blit(texto,(j*(pos_ret_x+tamanho_ret/8), i*(pos_ret_y + tamanho_ret/2)))

            for evento in event.get():
                mouse_pos = evento.pos
                rect = Rect((pos_ret_x+tamanho_ret/8),(pos_ret_y + tamanho_ret/2), tamanho_ret, tamanho_ret)
                if rect.collidepoint(mouse_pos):
                    estado = 2
        case 2:
            tela.fill((0,250,250))

            
            nums1,nums2,teto,num_perguntas = [],[],9,15
            preenchedor(nums1,nums2,teto,num_perguntas)
            for i in range(0,num_perguntas):
                texto = fonte_titulo.render(f"{nums1[i]} + {nums2[i]}", True, (0,0,0))
                user_text = fonte_titulo.render(" ", True, (0,0,0))
                tela.blit(texto,(largura/2,altura/2))
                tela.blit(user_text,(largura/2,altura*3/4))
                for evento in event.get():
                    if evento.type == pygame.KEYDOWN:
                        user_text += evento.unicode
                

            
            

                
    display.update()

