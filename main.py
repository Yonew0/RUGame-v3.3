import pygame
import time
#from tkinter import messagebox as msg

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load("./icon.ico"))

font = pygame.font.Font(None, 24)
pygame.display.set_caption('Симулятор траханья X')

chlen_pos_tmp = [220, 130, 40, 120]
zalupa_pos_tmp = [220, 250, 40, 20]
pizda_pos_tmp = [0, 350, 500, 40]
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        chlen_pos_tmp[1] -= 10
        zalupa_pos_tmp[1] -= 10
    if key[pygame.K_s]:
        chlen_pos_tmp[1] += 10
        zalupa_pos_tmp[1] += 10
    if key[pygame.K_a]:
        chlen_pos_tmp[0] -= 10
        zalupa_pos_tmp[0] -= 10
    if key[pygame.K_d]:
        chlen_pos_tmp[0] += 10
        zalupa_pos_tmp[0] += 10
    if zalupa_pos_tmp[1] > 390:
        zalupa_pos_tmp[1] -= 100
        chlen_pos_tmp[1] -= 100
        score += 1

    chlen_pos = chlen_pos_tmp
    zalupa_pos = zalupa_pos_tmp
    pizda_pos = pizda_pos_tmp
    
    screen.fill((0, 0, 0))
    text1 = font.render(f"{score}", True, (0, 255, 0))

    if score >= 20:
       #msg.showinfo("Симулятор траханья Х", "Вся сперма закончилась!")
       text1 = font.render("Вся сперма закончилась. ", True, (0, 255, 0))
       screen.blit(text1, (10, 10))
    #
    #   text2 = font.render("Но игра бесконечная, трахайте сколько хотите. ", True, (0, 255, 0))
    #    screen.blit(text2, (10, 30))

    screen.blit(text1, (10, 10))
    pygame.draw.rect(screen, (155, 155, 155), chlen_pos)
    pygame.draw.rect(screen, (200, 0, 0), zalupa_pos)
    pygame.draw.rect(screen, (255, 150, 150), pizda_pos)

    

    clock.tick(15)
    pygame.display.update()