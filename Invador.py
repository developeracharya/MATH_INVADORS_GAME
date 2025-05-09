import pygame
import random
class Invador:
    invadors_list = []
    alive_invadors=[]
    dead_invadors = []
    
    VELOCITIES = [x for x in range(20, 50)]
    def __init__(self, screen, INVADOR_IMAGE, delta, mode):
        self.screen = screen
        self.INVADOR_IMAGE = INVADOR_IMAGE
        self.f_num = random.randint(0, 9)
        self.s_num = random.randint(0, 9)
        self.x_invador = random.randint(0, 760)
        self.y_invador = 100
        self.x_velocity = random.choice([-1, 1])* random.choice(self.VELOCITIES) * delta
        self.y_velocity = random.choice(self.VELOCITIES) * delta   
        self.mode = mode
        self.value_fun(self.mode)
        print("created")
    
    def drawText(self, txt,color,size= 24, position=(10,10)):
        text_surface = pygame.font.SysFont("Arial", size).render(txt, True, color) # True for antialiasing
        self.screen.blit(text_surface, position)  # Draw the text onto the screen
    
    def value_fun(self, mode):
        if(mode == "addition"):
            self.value = self.f_num + self.s_num
            return f"{self.f_num} + {self.s_num} = "
        if(mode == "subtraction"):
            self.value = self.f_num - self.s_num
            return f"{self.f_num} - {self.s_num} = "
        if(mode == "multiplication"):
            self.value = self.f_num * self.s_num
            return f"{self.f_num} x {self.s_num} = "
        if(mode == "division"):
            if self.s_num == 0:
                self.s_num = 1
            self.value = round(self.f_num / self.s_num, 2)
            return f"{self.f_num} / {self.s_num} = "
    
    def move_invador(self):
        if self.x_invador > 0 and self.x_invador < 760: 
            self.x_invador += self.x_velocity
            self.y_invador += self.y_velocity
            
        elif self.x_invador <= 10 or self.x_invador >= 760:
            self.x_velocity *= -1
            self.x_invador += self.x_velocity
            self.y_invador += self.y_velocity
            
        if self.y_invador > 400 or self.y_invador < 0:
            self.y_velocity *= -1
            self.x_invador += self.x_velocity
            self.y_invador += self.y_velocity
        self.screen.blit(self.INVADOR_IMAGE, (self.x_invador, self.y_invador))
        self.drawText(txt=f"{self.value}", color=(255, 0 ,0), position=(self.x_invador + 80, self.y_invador))
    
    @classmethod
    def increase_speed(cls):
        for invador in cls.alive_invadors:
            if invador.x_velocity < 0:
                invador.x_velocity -= 0.1
            else:
                invador.x_velocity += 0.1
            if invador.y_velocity < 0:
                invador.y_velocity -= 0.1
            else:
                invador.y_velocity += 0.1

    @classmethod
    def value_checker(cls, new_invador):
        for invador in cls.alive_invadors:
            if invador.value == new_invador.value: return True
            
    @classmethod
    def random_invador(cls):
        if cls.alive_invadors:
            return random.choice(cls.alive_invadors)
    def collision(self):
      ...
    
    @classmethod
    def move_invadors(cls):
        for invador in cls.alive_invadors:
            invador.move_invador()
print(Invador.VELOCITIES)