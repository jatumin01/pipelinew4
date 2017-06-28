import pipelineGameCard.CG_ClassCharacter
class Hero(Character):
    
   def __init__(self,name):
       super(Hero,self).__init__(name)
       self.hp = 300
       self.atk = 50
       self.deff = 30
       self.brk = 70
       self.hel = 30

       

