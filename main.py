import pygame 
import sys
import random
import math 
from joueur import Joueur
from balle import Balle

class Jeu:
    
    def __init__(self):
        
        self.ecran = pygame.display.set_mode((900, 500))
        pygame.display.set_caption('Jeu Pong')
        self.jeu_encours = True 
        self.joueur_1_x, self.joueur_1_y = 20, 250
        self.joueur_2_x, self.joueur_2_y = 860, 250
        self.joueur_taille = [20, 80]
        self.vitesse_y_1, self.vitesse_y_2 = 0, 0
        self.joueur_1 = Joueur(self.joueur_1_x, self.joueur_1_y, self.joueur_taille)
        self.joueur_2 = Joueur(self.joueur_2_x, self.joueur_2_y, self.joueur_taille)
        self.rect = pygame.Rect(0, 0, 900, 500)
        self.balle_direction = [-1, 1]
        self.balle = Balle(450, 250, [10, 10], random.choice(self.balle_direction))
        self.balle_tire = False 
        self.balle_vitesse_x, self.balle_vitesse_y = 15, 2
        self.score_1, self.score_2 = 0, 0

    def boucle_principale(self):
        
        while self.jeu_encours:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.vitesse_y_1 = -10 
                    if event.key == pygame.K_DOWN:
                        self.vitesse_y_1 = 10 
                        
                    if event.key == pygame.K_w:
                        self.vitesse_y_2 = -10 
                    if event.key == pygame.K_s:
                        self.vitesse_y_2 = 10 
                    if event.key == pygame.K_SPACE:
                        self.balle_tire = True 
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.vitesse_y_1 = 0
                    if event.key == pygame.K_DOWN:
                        self.vitesse_y_1 = 0
                        
                    if event.key == pygame.K_w:
                        self.vitesse_y_2 = 0
                    if event.key == pygame.K_s:
                        self.vitesse_y_2 = 0
                        
            self.joueur_1.mouvement(self.vitesse_y_1)
            self.joueur_2.mouvement(self.vitesse_y_2)
            self.joueur_1.rect.clamp_ip(self.rect)
            self.joueur_2.rect.clamp_ip(self.rect)
            if self.balle_tire:
                self.balle.mouvement(self.balle_vitesse_x, self.balle_vitesse_y)
                
            if self.joueur_1.rect.colliderect(self.balle.rect) or self.joueur_2.rect.colliderect(self.balle.rect):
                self.balle_vitesse_x = self.changement_direction_balle(self.balle_vitesse_x, 0)  
                self.balle_vitesse_y = self.changement_direction_balle(self.balle_vitesse_y, 60)
                self.balle.vitesse_aleatoire_y = random.randint(1, 7)
            if self.balle.rect.top <= 0 or self.balle.rect.bottom >= 500:
                self.balle_vitesse_y = self.changement_direction_balle(self.balle_vitesse_y, 0)
                
            if self.balle.rect.right >= 915:
                self.balle.rect.x, self.balle.rect.y = 450, 250 
                self.score_1 += 1
                self.balle_tire = False
            if self.balle.rect.left <= -15:
                self.balle.rect.x, self.balle.rect.y = 450, 250 
                self.score_2 += 1 
                self.balle_tire = False
            self.balle.rect.clamp_ip(self.rect)
            self.ecran.fill((50, 50, 50))
            self.creer_message('grande', f"Jeu Pong", [300, 50, 20, 20], (255, 255, 255))
            self.creer_message('grande', f" { self.score_1 }", [300, 200, 50, 50], (255, 255, 255))
            self.creer_message('grande', f" { self.score_2 }", [485, 200, 50, 50], (255, 255, 255))
            if self.balle_tire is False:
                self.creer_message('petite', f" Appuyer Sur Espace Pour Commencer Le Jeu", [30, 100, 300, 50], (255, 255, 255))
                
            self.balle.afficher(self.ecran)
            self.joueur_1.afficher(self.ecran)
            self.joueur_2.afficher(self.ecran)
            pygame.display.flip()
            
    def changement_direction_balle(self, vitesse, angle):
        
        vitesse = - (vitesse * math.cos(angle))
        
        return vitesse
    
    def creer_message(self, font, message, message_rectangle, couleur):
        
        if font == 'petite':
            font = pygame.font.Font('/Users/karimsadiki/Desktop/Pong Game/ATARCC__.TTF', 20)
            
        if font == 'moyenne':
            font = pygame.font.Font('/Users/karimsadiki/Desktop/Pong Game/ATARCC__.TTF', 30)
            
        if font == 'grande':
            
            font = pygame.font.Font('/Users/karimsadiki/Desktop/Pong Game/ATARCC__.TTF', 40)
            
        message = font.render(message, True, couleur)
        self.ecran.blit(message, message_rectangle)            
            
            
if __name__ == '__main__':
    
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()