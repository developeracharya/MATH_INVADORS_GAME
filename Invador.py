import pygame
import random
class Invador:
    invadors_list = []
    VELOCITIES = [x for x in range(5, 11)]
    def __init__(self, screen, INVADOR_IMAGE, delta):
        self.screen = screen
        self.INVADOR_IMAGE = INVADOR_IMAGE
        self.f_num = random.randint(0, 9)
        self.s_num = random.randint(0, 9)
        self.x_invador = random.randint(-50, 760)
        self.y_invador = 100
        self.x_velocity = random.choice([-1, 1])* random.choice(self.VELOCITIES) * delta
        self.y_velocity = random.choice(self.VELOCITIES) * delta   
        __class__.invadors_list.append(self)    
        print("created")
         
    def value(self, mode):
        # if(mode == "addition"):
            self.value = self.f_num + self.s_num
        # if(mode == "subtraction"):
        #     self.value = self.f_num - self.s_num
        # if(mode == "multiplication"):
        #     self.value = self.f_num * self.s_num
        # if(mode == "division"):
        #     self.value = self.f_num / self.s_num
    
    def move_invador(self):
        self.x_invador += self.x_velocity
        self.y_invador += self.y_velocity
        self.screen.blit(self.INVADOR_IMAGE, (self.x_invador, self.y_invador))
    
    @classmethod
    def move_invadors(cls):
        for invador in cls.invadors_list:
            invador.move_invador()
print(Invador.VELOCITIES)