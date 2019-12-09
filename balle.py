import pygame 
import random 


class Balle:
    
    def __init__(self, x, y, taille, direction):
        
        self.x = x 
        self.y = y 
        self.taille = taille 
        self.direction = direction
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
        self.vitesse_aleatoire_y = random.randint(1, 4)
        
    def mouvement(self, vitesse_x, vitesse_y):
        
        self.rect.x = (self.rect.x + self.direction * vitesse_x)
        self.rect.y += self.vitesse_aleatoire_y * vitesse_y 
        
    def afficher(self, surface):
        
        pygame.draw.rect(surface, (230, 230, 230), self.rect)        