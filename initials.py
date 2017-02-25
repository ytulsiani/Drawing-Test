# In the routine below, you should draw your initials in perspective

from matlib import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective (40, -100, 100)
    #gtOrtho (-100, 100, -100, 100, -50, 50)
    gtPushMatrix()
    #gtTranslate(0, 0, -4)
    gtRotateY(5)
    initials()
    gtPopMatrix()
def initials():
    gtBeginShape()
    #Y
    
    gtVertex (-30, 30,  100.0)
    gtVertex (-20, 0,  -200.0)

    gtVertex (10, 50, 100.0)
    gtVertex (-20, 0, -200.0)

    gtVertex (-20, 0,  -200.0)
    gtVertex (-20, -30,  -100.0)
    #T
    gtVertex (-20, 0, -200.0)
    gtVertex (20, -10, -200.0)
    
    gtVertex (0, -5, -200.0)
    gtVertex (-20, -50, -100.0)
    gtEndShape()