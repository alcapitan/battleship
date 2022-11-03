import pygame
import back
from sys import exit
from time import sleep
from random import randint
pygame.init()

def someoneWon(ships):
    """
    Stop the game if someone has won.
	"""
    if 0 in ships:
        player = ships.index(0)
        player+=1
        if player==1:
            return 2
        elif player==2:
            return 1
    else:
        return None

def boatHere(table, player, position):
    """
         table is table of the play
         player is 1 or 2 according to user identifiant (who call this function)
         position is a tuple. First is x (left - right), and second is y (top - bottom)
         Remember in Python, lists start from 0. So remember to move 1 from the position !
    """
    x = position[0]
    y = position[1]
    if (table[y][x] != player) and (table[y][x] != 0):
        return "opposite"
    elif table[y][x] == player:
        return "same"
    elif table[y][x] == 0:
        return "empty"
    else:
        print(error("Retire boat"))
        return

def surface():
    ecran=pygame.display.set_mode()
    (x,y)=ecran.get_size()
    pygame.display.set_caption("Bataille navale")
    ecran=pygame.display.set_mode((x,y), pygame.FULLSCREEN)

    return (ecran,(x,y))

def plateau(ecran,pos,grille,joueur):
    noir=(0,0,0)
    posX=pos[0]
    posY=pos[1]
    coefMarge=150/1080
    coefSepHoriz=1/10

    imageBateau=pygame.image.load("bateau.png")
    dimensionImage=(int(coefSepHoriz*posX),int(((posY-(coefMarge*posY))/10)))

    imageBateau=pygame.transform.scale(imageBateau,dimensionImage)


    for i in range(1,10):
        pygame.draw.line(ecran,noir,(i*coefSepHoriz*posX,coefMarge*posY),(i*coefSepHoriz*posX,posY))
        pygame.display.flip()
    for i in range(10):
        pygame.draw.line(ecran,noir,(0,(coefMarge*posY)+(i*((posY-(coefMarge*posY))/10))),(posX,(coefMarge*posY)+(i*((posY-(coefMarge*posY)))/10)))
        pygame.display.flip()
    for i in range(10):
        for j in range(10):
            if grille[i][j]==1 and joueur==1:
                ecran.blit(imageBateau,(j*coefSepHoriz*posX,(coefMarge*posY)+i*((posY-(coefMarge*posY))/10)))
                pygame.display.flip()
            elif grille[i][j]==2 and joueur==2:
                ecran.blit(imageBateau,(j * coefSepHoriz * posX, (coefMarge * posY) + i * ((posY - (coefMarge * posY)) / 10)))
                pygame.display.flip()

                
    return (ecran)
def main():
    #initialisation des variables de bases

#-------------------couleurs---------------------

    noir=(0,0,0)
    blanc=(255,255,255)

#-------------------Variables:-----------------------------
    enCours=True
    ecran,resolEcran=surface()
    tourJoueur=True
    tourJoueur2=False
    grille = back.prepareGrid(10, 10)

    joueur1=1
    joueur2=2

    bateaux = [10 for joueur in range(2)]

    coefMarge = 150 / 1080
#------------------côté pygame------------------------------
    
    arial_font = pygame.font.SysFont("arial", 50)
    texteJ1=arial_font.render("À vous de jouer.",True,noir)
    texteJ2=arial_font.render("L'adversaire joue.",True,noir)
    texteTouche2=arial_font.render("L'adversaire a touché un de vos bateaux.",True,noir)
    texteTouche=arial_font.render("Vous avez touché un bateau de l'adversaire.",True,noir)
    texteFail=arial_font.render("Vous avez touché un de vos propres bateaux.",True,noir)
    texteFail2=arial_font.render("L'adversaire a touché un de ses propres bateaux.",True,noir)
    texteRien=arial_font.render("Vous n'avez pas touché de bateaux.",True,noir)
    texteRien2=arial_font.render("L'adversaire n'a pas touché de bateaux.",True,noir)
    while enCours:
        ecran.fill(blanc)
        ecran.blit(texteJ1, [50, 45])
        ecran = plateau(ecran, resolEcran, grille, joueur1)
        pygame.display.flip()
#----------------Tour joueur 1----------------------
        while tourJoueur:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    tourJoueur=False
                    enCours=False
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    joueur1PosX, joueur1PosY = pygame.mouse.get_pos()
                    if joueur1PosY>(coefMarge*resolEcran[1]):
                        joueur1PosX=joueur1PosX // (resolEcran[0]/10)
                        test=joueur1PosY-(coefMarge*resolEcran[1])
                        joueur1PosY=(test//((resolEcran[1]-(coefMarge*resolEcran[1]))/10))
                        joueur1PosY=int(joueur1PosY)
                        joueur1PosX=int(joueur1PosX)
                        outcome = boatHere(grille,joueur1,(joueur1PosX,joueur1PosY))
                        if outcome == "opposite":
                            bateaux[1] -= 1
                            grille[joueur1PosY][joueur1PosX]=0
                            ecran.fill(blanc)
                            ecran = plateau(ecran, resolEcran, grille, joueur1)
                            ecran.blit(texteTouche, (50,45))
                            pygame.display.flip()
                        elif outcome=="same":
                            bateaux[0] -= 1
                            grille[joueur1PosY][joueur1PosX] = 0
                            ecran.fill(blanc)
                            ecran= plateau(ecran, resolEcran, grille, joueur1)
                            ecran.blit(texteFail, (50,45))
                            pygame.display.flip()
                        else:
                            ecran.fill(blanc)
                            ecran = plateau(ecran, resolEcran, grille, joueur1)
                            ecran.blit(texteRien,(50,45))
                            pygame.display.flip()


                        gagnant = someoneWon(bateaux)
                        if gagnant != None:
                            tourJoueur = False
                        else:
                            tourJoueur = False
                            tourJoueur2 = True

        sleep(3)
        """ecran.fill(blanc)
        ecran.blit(texteJ2, [resolEcran[1] / 2, 50])
        ecran = plateau(ecran, resolEcran, grille, 2)
        pygame.display.flip()"""
#----------------Tour joueur 2--------------------
        while tourJoueur2:
            """for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    tourJoueur=False
                    enCours=False
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    joueur2PosX,joueur2PosY = pygame.mouse.get_pos()
                    print(joueur2PosX,joueur2PosY)
                    if joueur2PosY>(coefMarge*resolEcran[1]):
                        joueur2PosX = joueur2PosX // (resolEcran[0] / 10)
                        test = joueur2PosY - (coefMarge * resolEcran[1])
                        joueur2PosY = (test // ((resolEcran[1] - (coefMarge * resolEcran[1])) / 10))
                        joueur2PosY = int(joueur2PosY)
                        joueur2PosX = int(joueur2PosX)
                        outcome = boatHere(grille,joueur2,(joueur2PosX,joueur2PosY))"""
            joueur2PosX = randint(0,9)
            joueur2PosY = randint(0,9)
            outcome = boatHere(grille,joueur2,(joueur2PosX,joueur2PosY))
            if outcome == "opposite":
                bateaux[0] -= 1
                grille[joueur2PosY][joueur2PosX]=0
                ecran.fill(blanc)
                ecran.blit(texteTouche2, (50,45))
                ecran = plateau(ecran, resolEcran, grille, joueur1)
                pygame.display.flip()
            elif outcome=="same":
                bateaux[1] -= 1
                grille[joueur2PosY][joueur2PosX] = 0
                ecran.fill(blanc)
                ecran.blit(texteFail2,(50,45))
                ecran = plateau(ecran, resolEcran, grille, joueur1)
                pygame.display.flip()
            else:
                ecran.fill(blanc)
                ecran.blit(texteRien2, (50,45))
                ecran = plateau(ecran, resolEcran, grille, joueur1)
                pygame.display.flip()
            gagnant=someoneWon(bateaux)
            if gagnant!=None:
                tourJoueur2=False
            else:
                tourJoueur2 = False
                tourJoueur = True
        sleep(2)
        if gagnant!=None:
            texteGagnant=arial_font.render((f"Le gagnant est le joueur {gagnant}"),True,noir)
            ecran.fill(blanc)
            ecran.blit(texteGagnant,(resolEcran[1]/2,resolEcran[1]/2))
            pygame.display.flip()
            sleep(3)
            enCours=False
main()
