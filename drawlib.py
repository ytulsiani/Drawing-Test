# Drawing Routines, like OpenGL

from matlib import *
shapeStarted = False
vertexArray = []
isOrtho = False
projArray = []
def gtOrtho(left, right, bottom, top, near, far):
    global projArray
    projArray = [left, right, bottom, top]
    global isOrtho
    isOrtho = True
def gtPerspective(fov, near, far):
    global projArray
    projArray = [fov, near, far]
    global isOrtho
    isOrtho = False

def gtBeginShape():
    global shapeStarted
    shapeStarted = True
    
def gtEndShape():
    global shapeStarted
    shapeStarted = False
    global vertexArray
    startVertex = []
    stopVertex = []
    firstPoint = True
    for i in vertexArray:
        if (firstPoint): #first point
            firstPoint = False
            startVertex = i
        else: #second point
            firstPoint = True
            stopVertex = i
            ctMatrix = gtGetMatrix()
            matrixStart = new_matrix_multiplier(ctMatrix, startVertex) #multiply with CTM. what does this equal
            matrixStop = new_matrix_multiplier(ctMatrix, stopVertex) #multiply with CTM, what does this equal
            matrixStart = doProjection(matrixStart)
            matrixStop = doProjection(matrixStop)
            line(matrixStart[0], matrixStart[1], matrixStop[0], matrixStop[1])
    vertexArray = []

def gtVertex(x, y, z):
    global vertexArray
    localVertex = [x, y, z, 1]
    vertexArray.append(localVertex)
    
def new_matrix_multiplier(before, changes):
    after = [0,0,0,0]
    for i in range(4):
            for k in range(4):
                after[i] += before[i][k] * changes[k]
    return after
def doProjection(matrix):
    global projArray
    global isOrtho
    if(isOrtho):
        left = projArray[0]
        right = projArray[1]
        bottom = projArray[2]
        top = projArray[3]
        matrix[0] = (width / (right - left)) * (matrix[0] - left)
        matrix[1] = (height / (bottom - top)) * (matrix[1] - top)        
    else:
        fov = projArray[0]
        near = projArray[1]
        far = projArray[2]
        fovRadians = radians(float(fov))
        xPrime = matrix[0] / abs(matrix[2])
        yPrime = matrix[1] / -(abs(matrix[2]))
        k  = tan(fovRadians / 2)
        matrix[0] = (xPrime + k) * (width  / (2*k) )
        matrix[1] = (yPrime + k) * (height / (2*k) )
    return matrix