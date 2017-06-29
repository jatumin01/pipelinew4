#########################
#                       #
#    follow  in path    #
#                       #
#                       #
#########################
import sys
if not "C:/Users/eur/Documents/Git/pipelinew4" in sys.path:
    sys.path.append("C:/Users/eur/Documents/Git/pipelinew4")

import pipelineGameCard.CG_masterCompiled
reload(pipelineGameCard.CG_masterCompiled)