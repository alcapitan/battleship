import pygame
import sys

pygame.init()
def surface():
    ecran=pygame.display.set_mode()
    (x,y)=ecran.get_size()
    pygame.display.set_caption("Touché Coulé")
    ecran=pygame.display.set_mode((x,y))

    return (ecran,(x,y))

def plateau(ecran,pos):
    noir=(0,0,0)
    posX=pos[0]
    posY=pos[1]
    coefMarge=200/1920
    coefSepHoriz=1/10



    for i in range(1,10):
        pygame.draw.line(ecran,noir,(i*coefSepHoriz*posX,coefMarge*posY),(i*coefSepHoriz*posX,posY))
        pygame.display.flip()
    for i in range(10):
        pygame.draw.line(ecran,noir,(0,(coefMarge*posY)+(i*((posY-(coefMarge*posY))/10))),(posX,(coefMarge*posY)+(i*((posY-(coefMarge*posY)))/10)))
        pygame.display.flip()
    return ecran
def main():
    #initialisation des variables de bases

#-------------------couleurs---------------------

    noir=(0,0,0)
    blanc=(255,255,255)

#-------------------Variables:-----------------------------
    enCours=True
    ecran,test=surface()
    tourJoueur=True
    tourRobot=False


#------------------côté pygame------------------------------

    arial_font = pygame.font.SysFont("arial", 50)
    texteJ1=arial_font.render("C'est le tour du joueur 1",True,noir)
    texteJ2=arial_font.render("C'est le tour du joueur 2",True,noir)

    while enCours:
        ecran.fill(blanc)
        ecran=plateau(ecran,test)
        ecran.blit(texteJ1,[test[1]/2,50])
        pygame.display.flip()
        while tourJoueur:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    tourJoueur=False
                    enCours=False
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    joueur1PosX, joueur1PosY = pygame.mouse.get_pos()
                    print(joueur1PosX,joueur1PosY)
                    ecran.fill(blanc)
                    ecran.blit(texteJ1, [test[1]/2, 50])
                    ecran = plateau(ecran,test)
                    pygame.display.flip()

                    
main()
        
        