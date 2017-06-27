import maya.cmds as cmds
class tictactoe(object):
    def __init__(self):
        self.ix = 1
        self.tictactoe = ['0','1','2','3','4','5','6','7','8','9']
    def tictactoeWindow(self):    
        if cmds.window('tictactoeWindow' , q=True, ex=True):
                cmds.deleteUI('tictactoeWindow' , window=True)
        cmds.window('tictactoeWindow' , t='TIC TAC TOE GAME')
        cmds.gridLayout( numberOfColumns=3, cellWidthHeight=(200,200) )
        cmds.button('button1',l='1',c=choosenum1)
        cmds.button('button2',l='2',c=choosenum2)
        cmds.button('button3',l='3',c=choosenum3)
        cmds.button('button4',l='4',c=choosenum4)
        cmds.button('button5',l='5',c=choosenum5)
        cmds.button('button6',l='6',c=choosenum6)
        cmds.button('button7',l='7',c=choosenum7)
        cmds.button('button8',l='8',c=choosenum8)
        cmds.button('button9',l='9',c=choosenum9)
        cmds.showWindow('tictactoeWindow')
                
    def choosenum1(self,*agrs):
        self.UI(1)

    def choosenum2(self,*agrs):
        self.UI(2)

    def choosenum3(self,*agrs):
        self.UI(3)

    def choosenum4(self,*agrs):
        self.UI(5)

    def choosenum5(self,*agrs):
        self.UI(6)

    def choosenum6(self,*agrs):
        self.UI(7)

    def choosenum7(self,*agrs):
        self.UI(8)

    def choosenum8(self,*agrs):
        self.UI(9)
    def choosenum9(self,*agrs):
        self.UI(10)
        
    def play_tictactoe(self,position,player):    
        self.mask =''
        if player%2 == 1:
            self.mask = 'X'
        else :
            self.mask = 'O' 
        if position == 1 and self.tictactoe[1] == '1':
            self.tictactoe[position] =self. mask
        elif position == 2 and self.tictactoe[2] == '2':
            self.tictactoe[position] = self.mask
        elif position == 3 and self.tictactoe[3] == '3':
            self.tictactoe[position] = self.mask
        elif position == 4 and self.tictactoe[4] == '4':
            self.tictactoe[position] = self.mask
        elif position == 5 and self.tictactoe[5] == '5':
            self.tictactoe[position] = self.mask
        elif position == 6 and self.tictactoe[6] == '6':
            self.tictactoe[position] = self.mask
        elif position == 7 and self.tictactoe[7] == '7':
            self.tictactoe[position] = self.mask
        elif position == 8 and self.tictactoe[8] == '8':
            self.tictactoe[position] = self.mask
        elif position == 9 and self.tictactoe[9] == '9':
            self.tictactoe[position] = self.mask
        else :
            self.c = ' Error input pls try agian'
            return self.c
        print self.show_state() 
        self.i = self.checkwin()
        if self.i == 1 :
            self.i = 'Tic tac toe is Over \n Winner is player ' + mask
        elif self.i == 0 :
            self.i = 'Tic tac Toe in Progress' 
        else :
            self.i = 'Tic Tac Toe is Draw' 
        return self.i
            
    def show_state(self):
        self.asset = '\nPlayer 1 is [X] Player 2 is [O]\n'
        self.asset += self.tictactoe[1] + ' | ' + self.tictactoe[2] + ' | ' + self.tictactoe[3]
        self.asset += '\n'+ self.tictactoe[4] + ' | ' + self.tictactoe[5] + ' | ' + self.tictactoe[6] 
        self.asset += '\n' + self.tictactoe[7] + ' | ' + self.tictactoe[8] + ' | ' + self.tictactoe[9]
        return asset 
    
    def checkwin(self):
        if self.tictactoe[1] == self.tictactoe[2] and self.tictactoe[2] == self.tictactoe[3]:
            return 1
        elif self.tictactoe[4] == self.tictactoe[5] and self.tictactoe[5] == self.tictactoe[6]:
            return 1
        elif self.tictactoe[7] == self.tictactoe[8] and self.tictactoe[8] == self.tictactoe[9]:
            return 1
        elif self.tictactoe[1] == self.tictactoe[4] and self.tictactoe[4] == self.tictactoe[7]:
            return 1
        elif self.tictactoe[2] == self.tictactoe[5] and self.tictactoe[5] == self.tictactoe[8]:
            return 1
        elif self.tictactoe[3] == self.tictactoe[6] and self.tictactoe[6] == self.tictactoe[9]:
            return 1
        elif self.tictactoe[7] == self.tictactoe[5] and self.tictactoe[5] == self.tictactoe[3]:
            return 1
        elif self.tictactoe[1] == self.tictactoe[5] and self.tictactoe[5] == self.tictactoe[9]:
            return 1
        elif self.tictactoe[1] != '1' and self.tictactoe[2] != '2' and self.tictactoe[3] != '3' and self.tictactoe[4] != '4' and self.tictactoe[5] != '5' and self.tictactoe[6] != '6' and self.tictactoe[7] != '7' and self.tictactoe[8] != '8' and self.tictactoe[9] != '9' :
            return -1
        else :
            return 0
            
        
    def UI(self,num):
        self.pos = num
        self.x = play_tictactoe(self.pos,self.ix)
        if self.x == ' Error input pls try agian':
            print self.x
        elif x =='Tic tac toe is Over \n Winner is player X' or  x =='Tic tac toe is Over \n Winner is player O' :
            print self.x
        elif x == 'Tic Tac Toe is Draw' :
            print self.x
        print self.x
        self.ix+=1

a = tictactoe()
a.tictactoeWindow()
