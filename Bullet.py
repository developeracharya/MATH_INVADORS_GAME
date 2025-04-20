import pygame
class Bullet:
    bullets = []
    def __init__(self, screen, X_BULLET, Y_BULLET, BULLET_SPEED, BULLET_IMAGE, delta):
        self.screen = screen
        self.BULLET_IMAGE = BULLET_IMAGE
        self.X_BULLET = X_BULLET + 75
        self.Y_BULLET = Y_BULLET
        self.BULLET_SPEED = BULLET_SPEED * delta
        self.collision = False
        __class__.bullets.append(self)
    
    def move_bullet(self):
        self.Y_BULLET -= self.BULLET_SPEED
        self.screen.blit(self.BULLET_IMAGE, (self.X_BULLET, self.Y_BULLET))
    
    @classmethod
    def move_bullets(cls):
        print("bullets list")
        for bullet in cls.bullets:
            bullet.move_bullet()