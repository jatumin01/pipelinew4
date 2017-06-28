import maya.cmds as cmds
def GUI():    
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
    cmds.iconTextButton("button1", image='blank.png')
    cmds.iconTextButton("button2", image='blank.png')
    cmds.iconTextButton("button3", image='blank.png')
    cmds.button("tryAgian",l='Reset Match' , h = 50 ,p='menu')
    cmds.showWindow('cardGame')




