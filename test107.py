import pygame
pygame.init()
screenwidth,screenhieght=500,500
display=pygame.display.set_mode((screenwidth,screenhieght))
pygame.display.set_caption("adding image and background image")
backgroundimg=pygame.transform.scale(pygame.image.load("img2.png").convert(),(screenwidth,screenhieght))
img132=pygame.transform.scale(pygame.image.load("img12.png").convert_alpha(),200,200)
prnguinrect=img132.get_rect(center=(screenwidth//2,screenhieght // 2 -30))
text=pygame.font.Font(None,36).render("hello world",True,pygame.Color("black"))
text_rect=text.get_rect(center=(screenwidth//2,screenhieght // 2 +110))
def gameloop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(backgroundimg,(0,0))
        display_surface.blit(img132,prnguinrect)
        display_surface.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
pygame.quit()