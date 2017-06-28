import random
class CardGame(object):
    def __init__(self,Hero,Monster,Boss):
        super(CardGame,self).__init__()
        self.hero = Hero
        self.monster = Monster
        self.boss = Boss
        self.cardHero = [0,0,0]
         
    
    def randomCard(self,x):
        x.selectCard = random.randint(0,3)
    
    def randomCardHero(self):
        for x in range(3):
            self.cardHero[x] = random.randint(0,3)
        print 'Draw Card : ' + str(self.cardHero)
        
    def chooseCard(self):
        print 'You Have Card ' + str(self.cardHero)
        self.hero.selectCard = input('Hero SelectCard')
        if self.hero.selectCard == self.cardHero[0]:
            self.cardHero[0]=random.randint(0,3)
        elif self.hero.selectCard == self.cardHero[1]:
            self.cardHero[1]=random.randint(0,3)
        elif self.hero.selectCard == self.cardHero[2]:
            self.cardHero[2]=random.randint(0,3)           
          
    def action(self):
        self.state = 1
        self.fineMonster = 1
        self.randomCardHero()
        self.monsterType = self.monster 
        while self.state != 3 :
            self.turn = 1
            while self.hero.hp >0 and self.monsterType.hp >0 :
                print '--------- Turn ' + str(self.turn) +' -------------'
                self.count = 0
                for x in self.cardHero :
                    if x == 0 :
                        cmds.iconTextButton("button%s"%(self.count), image='aHero.png')
                    elif x == 1 :
                        cmds.iconTextButton("button%s"%(self.count), image='dHero.png')
                    elif x == 2 :
                        cmds.iconTextButton("button%s"%(self.count), image='bHero.png')
                    else :
                        cmds.iconTextButton("button%s"%(self.count), image='heal.png')
                    self.count+=1
                
                self.randomCard(self.monsterType)       
                self.chooseCard()
                print 'Hero SelectCard == ' + str(self.hero.selectCard) + '\nMonster SelectCard == ' + str(self.monsterType.selectCard)
                if self.hero.selectCard == 0 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= self.monsterType.atk
                    self.monsterType.hp -= self.hero.atk
                    print 'Hero Attack : ' +str(self.hero.atk)
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 1 :
                    self.monsterType.hp -= (self.hero.atk - self.monsterType.deff)
                    print 'Hero Attack : ' +str(self.hero.atk)
                    print self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff)
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 2 :
                    self.monsterType.hp -= self.hero.atk
                    print 'Hero Attack : ' + str(self.hero.atk)
                    print self.monsterType.name + ' Break  : Break Fail '
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp -= (self.hero.atk-self.monsterType.hel)
                    print 'Hero Attack : ' +str(self.hero.atk)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= ( self.monsterType.atk - self.hero.deff )
                    print 'Hero Deffend : ' +str(self.hero.deff)
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)            
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 1 :
                    print 'Hero Deffend : ' +str(self.hero.deff)
                    print self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff)   
                    print 'Nothing'
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= self.monsterType.brk
                    print 'Hero Deffend : Deffend Fail'
                    print self.monsterType.name + ' Break : ' +str(self.monsterType.brk)  
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp += self.monsterType.hel
                    print 'Hero Deffend : ' +str(self.hero.deff)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)  
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= self.monsterType.atk
                    print 'Hero Break : Break Fail' 
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk) 
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 1 :
                    self.monsterType.hp -= self.hero.brk
                    print 'Hero Break : ' +str(self.hero.brk)
                    print self.monsterType.name + ' Deffend : Deffend Fail'
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= self.monsterType.brk
                    self.monsterType.hp -= self.hero.brk
                    print 'Hero Break : ' +str(self.hero.brk)
                    print self.monsterType.name + ' Break : ' +str(self.monsterType.brk)
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp -= (self.hero.brk-self.monsterType.hel)
                    print 'Hero Break : ' +str(self.hero.brk)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= (self.monsterType.atk-self.hero.hel)
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 1 :
                    self.hero.hp += self.hero.hel
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Deffend '
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= (self.monsterType.brk-self.hero.hel)
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Break : ' +str(self.monsterType.brk)
                elif self.hero.selectCard == 3 and self.monster.selectCard == 3 :
                    self.monsterType.hp += self.monsterType.hel
                    self.hero.hp += self.hero.hel
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                    
                if self.hero.hp > 300 :
                    self.hero.hp = 300
                if self.monster.hp > 150 :
                    self.monsterType.hp = 150
                if self.boss.hp > 300 :
                    self.boss.hp = 300
                print self.hero.name + ' HP : ' + str(self.hero.hp)
                print self.monsterType.name + '  HP : ' + str(self.monsterType.hp)
                self.turn+=1
                
                                
            if self.state == 1 :
                if self.hero.hp <= 0 :
                    print '-------- Monster Win -----------'
                    break
                else :
                    self.state+=1
                    print '-------- Hero Win --------------'
                    print '-------- Next State (Boss) ----------'
                    self.monsterType = self.boss
                    continue
                    
            elif self.state == 2 :
                if self.hero.hp <= 0 :
                    print '-------- Boss Win -----------'
                else :
                    print '-------- Hero Win --------------'
                
                print '--------- End Game ----------'
                break
            
    def GUI(self):

        if cmds.window('cardGame' , q=True, ex=True):
                cmds.deleteUI('a' , window=True)
        cmds.window('cardGame' , t='Card Game')
        cmds.columnLayout('menu' ,adjustableColumn = True,w=20,)
        cmds.text("MHp", label = "Monster HP 150/150", height = 30, backgroundColor = [0.2, 0.2, 0.2],p='menu')
        cmds.gridLayout( 'Monster',numberOfRowsColumns=(1,2), cellWidthHeight=(200,100),p='menu' )
        cmds.iconTextButton( image='O.png',p='Monster')
        cmds.iconTextButton( image='O.png',p='Monster')
        cmds.text("event", label = "Start Game", height = 50, backgroundColor = [0.2, 0.2, 0.2],p='menu')
        cmds.gridLayout( 'Hero',numberOfRowsColumns=(1,2), cellWidthHeight=(200,100),p='menu' )
        cmds.iconTextButton('Hero Card',image='X.png',p='Hero')
        cmds.iconTextButton( image='X.png',p='Hero')
        cmds.text("HHp", label = "Hero HP 150/150", height = 30, backgroundColor = [0.2, 0.2, 0.2],p='menu')
        cmds.gridLayout( 'name',numberOfRowsColumns=(1,3), cellWidthHeight=(200,200),p='menu' )
        cmds.iconTextButton("button0", image='blank.png',c=buttonCard0)
        cmds.iconTextButton("button1", image='blank.png',c=buttonCard1)
        cmds.iconTextButton("button2", image='blank.png',c=buttonCard2)
        cmds.button("tryAgian",l='Reset Match' , h = 50 ,p='menu')
        cmds.showWindow('cardGame')

    def buttonCard0(self):
        if self.cardHero[x]
    def buttonCard1(self):
        self.chooseCard()
    def buttonCard2(self):
        self.chooseCard()