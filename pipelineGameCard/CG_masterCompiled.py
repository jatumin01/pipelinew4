import sys
if not "C:/Users/eur/Documents/Git/pipelinew4" in sys.path:
    sys.path.append("C:/Users/eur/Documents/Git/pipelinew4")

import pipelineGameCard.CG_ClassCharacter
import pipelineGameCard.CG_heroClass
import pipelineGameCard.CG_monsterClass
import pipelineGameCard.CG_cardGame
import pipelineGameCard.CG_GUI

x= Hero('Hero')
y= Monster('Monster')
z= Monster('Boss')
c= CardGame(x,y,z)
c.action()



