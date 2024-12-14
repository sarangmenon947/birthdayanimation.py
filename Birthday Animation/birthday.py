import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greetings By Sarang")

img = pygame.image.load("Birthday Animation\welcome.png")
image = pygame.transform.scale(img, (WIDTH, HEIGHT))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    
    font = pygame.font.SysFont("Lato", 50)
    text = font.render("Happy Birthday!", True, "blue")
    text2 = font.render("To You", True, "green")
    screen.fill("orange")
    screen.blit(image, (0, 0))
    screen.blit(text, (200, 250))
    screen.blit(text2, (240, 300))

    pygame.display.update()
    time.sleep(2)

    img2 = pygame.image.load("Birthday Animation\giftbox.png")
    image2 = pygame.transform.scale(img2, (WIDTH, HEIGHT))
    font2 = pygame.font.SysFont("Lato", 20)
    text3 = font.render("May God Bless You", True, "red")
    screen.fill("pink")
    screen.blit(image2, (0, 0))
    screen.blit(text3, (200, 250))

    pygame.display.update()
    time.sleep(2)

    img3 = pygame.image.load("Birthday Animation/birthdaycake.png")
    image3 = pygame.transform.scale(img3, (WIDTH, HEIGHT))
    font3 = pygame.font.SysFont("Lato", 20)
    text4 = font.render("From Sarang", True, "green")
    screen.fill("pink")
    screen.blit(image3, (0, 0))
    screen.blit(text4, (200, 230))

    pygame.display.update()
    time.sleep(2)
