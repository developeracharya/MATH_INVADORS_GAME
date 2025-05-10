import pygame
from Invador import Invador 
class Bullet():
    BULLETS = []
    def __init__(self, screen, X_BULLET, Y_BULLET, BULLET_SPEED, BULLET_IMAGE, delta):
        self.screen = screen
        self.BULLET_IMAGE = BULLET_IMAGE
        self.X_BULLET = X_BULLET + 75
        self.Y_BULLET = Y_BULLET
        self.BULLET_SPEED = BULLET_SPEED * delta
        self.collision = False
        __class__.BULLETS.append(self)
    
    def move_bullet(self):
        self.Y_BULLET -= self.BULLET_SPEED
        self.screen.blit(self.BULLET_IMAGE, (self.X_BULLET, self.Y_BULLET))
        
    def collision_detector(self, invadors):
        for invador in invadors:
            if invador.x_invador - 50 < self.X_BULLET < invador.x_invador + 50 and invador.y_invador < self.Y_BULLET < invador.y_invador + 100:
                self.collision = True
                return invador
                
                
    @classmethod
    def move_bullets(cls):
        # print("BULLETS list")
        for bullet in cls.BULLETS:
            if Invador.alive_invadors:
               colloided_invador = bullet.collision_detector(Invador.alive_invadors)
               if bullet.collision:
                    cls.BULLETS = []
               if colloided_invador:
                    bullet.move_bullet()
                    return colloided_invador
            if bullet.Y_BULLET < -50:
                cls.BULLETS.remove(bullet)
            bullet.move_bullet()
            
            