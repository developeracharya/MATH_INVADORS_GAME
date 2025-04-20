import random
class Invador:
    invadors_list = []
    def __init__(self):
        f_num = random.randint(0, 9)
        s_num = random.randint(0, 9)
        __class__.invadors_list.append(self)    
         
    def value(self, mode):
        if(mode == "addition"):
            self.value = self.f_num + self.s_num
        if(mode == "subtraction"):
            self.value = self.f_num - self.s_num
        if(mode == "multiplication"):
            self.value = self.f_num * self.s_num
        if(mode == "division"):
            self.value = self.f_num / self.s_num