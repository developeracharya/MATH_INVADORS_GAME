import pygame
from Invador import Invador

class Button(Invador):
    buttons_list = []
    def __init__(self, index : any, screen: object, BUTTON_TEXT : str, BUTTON_WIDTH: int, BUTTON_HEIGHT : int, BUTTON_LOCATION : tuple, BUTTON_COLOR : str or tuple, TXT_COLOR : str or tuple, **kargs):
        '''Button(screen)'''
        self.screen = screen
        self.id = index
        self.BUTTON_WIDTH = BUTTON_WIDTH
        self.BUTTON_HEIGHT = BUTTON_HEIGHT
        self.BUTTON_TEXT = BUTTON_TEXT
        self.TXT_COLOR = TXT_COLOR
        self.BUTTON_COLOR = BUTTON_COLOR
        self.LOCATION_X, self.LOCATION_Y = BUTTON_LOCATION
        for name , value in kargs.items():
            setattr(self, name, value)
        self.create_button()
        __class__.buttons_list.append(self)
    #self, txt,color,size= 24, position=(10,10)
    #   Button("speaker",screen, "", SPEAKER_WIDTH, SPEAKER_HEIGHT, (SPEAKER_X, SPEAKER_Y), (0, 0, 0), (0, 0, 0), speaker=True, on=True, speaker_pic = (SPEAKER_ON_IMAGE, SPEAKER_OFF_IMAGE))
    
    def create_button(self):
        if self.id == "speaker":
            if self.on == True:
                self.current_pic = self.speaker_pic[0]
            else:
                 self.current_pic = self.speaker_pic[1]
            self.screen.blit(self.current_pic, (self.LOCATION_X, self.LOCATION_Y))
        else:
            pygame.draw.rect(self.screen,  self.BUTTON_COLOR, (self.LOCATION_X, self.LOCATION_Y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
            super().drawText(self.BUTTON_TEXT, self.TXT_COLOR, 18, (self.LOCATION_X + self.BUTTON_WIDTH//4, (self.LOCATION_Y+ self.BUTTON_HEIGHT//4)))

    @classmethod 
    def button_click(cls, CLICK_LOCATION):
        for button in cls.buttons_list:
            if (button.LOCATION_X <= CLICK_LOCATION[0] <= (button.LOCATION_X + button.BUTTON_WIDTH)) and (button.LOCATION_Y <= CLICK_LOCATION[1] <= (button.LOCATION_Y + button.BUTTON_HEIGHT)):
                # print(button.id,CLICK_LOCATION, button.LOCATION_X, button.LOCATION_Y)
                # print()
                return button.id
            
                ...