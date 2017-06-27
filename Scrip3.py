#=========================(Window Zone)========================
import maya.cmds as cmds

#set Window and defult of button
cmds.window(title="Tictactoe", widthHeight=(250,250))
cmds.gridLayout(numberOfRowsColumns=[3,3],cellWidthHeight=(85, 85) )
cmds.button(label='(add 1)')
cmds.button(label='(add 2)')
cmds.button(label='(add 3)')
cmds.button(label='(add 4)')
cmds.button(label='(add 5)')
cmds.button(label='(add 6)')
cmds.button(label='(add 7)')
cmds.button(label='(add 8)')
cmds.button(label='(add 9)')

#==============================================================

tictactoe = ['0','1','2','3','4','5','6','7','8','9']
def play_tictactoe(position,player):    
    mask =''
    if player%2 == 1:
        mask = 'X'
    else :
        mask = 'O' 
    if position == 1 and tictactoe[1] == '1':
        tictactoe[position] = mask
    elif position == 2 and tictactoe[2] == '2':
        tictactoe[position] = mask
    elif position == 3 and tictactoe[3] == '3':
        tictactoe[position] = mask
    elif position == 4 and tictactoe[4] == '4':
        tictactoe[position] = mask
    elif position == 5 and tictactoe[5] == '5':
        tictactoe[position] = mask
    elif position == 6 and tictactoe[6] == '6':
        tictactoe[position] = mask
    elif position == 7 and tictactoe[7] == '7':
        tictactoe[position] = mask
    elif position == 8 and tictactoe[8] == '8':
        tictactoe[position] = mask
    elif position == 9 and tictactoe[9] == '9':
        tictactoe[position] = mask
    else :
        c = ' Error input pls try agian'
        return c
    print show_state() 
    i = checkwin()
    if i == 1 :
        i = 'Tic tac toe is Over \n Winner is player ' + mask
    elif i == 0 :
        i = 'Tic tac Toe in Progress' 
    else :
        i = 'Tic Tac Toe is Draw' 
    return i
        
def show_state():
    asset = '\nPlayer 1 is [X] Player 2 is [O]\n'
    asset += tictactoe[1] + ' | ' + tictactoe[2] + ' | ' + tictactoe[3]
    asset += '\n'+ tictactoe[4] + ' | ' + tictactoe[5] + ' | ' + tictactoe[6] 
    asset += '\n' + tictactoe[7] + ' | ' + tictactoe[8] + ' | ' + tictactoe[9]
    return asset 

def checkwin():
    if tictactoe[1] == tictactoe[2] and tictactoe[2] == tictactoe[3]:
        return 1
    elif tictactoe[4] == tictactoe[5] and tictactoe[5] == tictactoe[6]:
        return 1
    elif tictactoe[7] == tictactoe[8] and tictactoe[8] == tictactoe[9]:
        return 1
    elif tictactoe[1] == tictactoe[4] and tictactoe[4] == tictactoe[7]:
        return 1
    elif tictactoe[2] == tictactoe[5] and tictactoe[5] == tictactoe[8]:
        return 1
    elif tictactoe[3] == tictactoe[6] and tictactoe[6] == tictactoe[9]:
        return 1
    elif tictactoe[7] == tictactoe[5] and tictactoe[5] == tictactoe[3]:
        return 1
    elif tictactoe[1] == tictactoe[5] and tictactoe[5] == tictactoe[9]:
        return 1
    elif tictactoe[1] != '1' and tictactoe[2] != '2' and tictactoe[3] != '3' and tictactoe[4] != '4' and tictactoe[5] != '5' and tictactoe[6] != '6' and tictactoe[7] != '7' and tictactoe[8] != '8' and tictactoe[9] != '9' :
        return -1
    else :
        return 0
        
    
def UI():
    ix = 1
    while True:
        pos = input('Enter Position')
        x = play_tictactoe(pos,ix)
        if x == ' Error input pls try agian':
            print x
            continue
        elif x =='Tic tac toe is Over \n Winner is player X' or  x =='Tic tac toe is Over \n Winner is player O' :
            print x
            break 
        elif x == 'Tic Tac Toe is Draw' :
            print x
            break
        print x
        ix+=1
    
UI()

#=========================(Window Zone)========================
cmds.showWindow()
#==============================================================