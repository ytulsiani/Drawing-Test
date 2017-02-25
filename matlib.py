# Matrix Stack Library -- Use your code from Project 1A

def gtInitialize():
    global initialMatrix
    initialMatrix = [ [1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1] ]
    global stack
    stack = []
    stack.append(initialMatrix)
    global ctMatrix
    ctMatrix = initialMatrix

def gtPushMatrix():
    global ctMatrix
    stack.append(ctMatrix)
    ctMatrix = stack[-1]

def gtPopMatrix():
    global ctMatrix
    if (len(stack) == 1 or len(stack) == 0):
        print("NOTHING CAN BE POPPED FROM THE STACK")
    else:
        stack.pop()
        ctMatrix = stack[-1]

def gtTranslate(x, y, z):
    transformationMatrix = [ [1,0,0,x], [0,1,0,y], [0,0,1,z], [0,0,0,1] ]
    global ctMatrix
    ctMatrix = matrix_multiplier(ctMatrix, transformationMatrix)
    stack[-1] = ctMatrix

def gtScale(x, y, z):
    transformationMatrix = [ [x,0,0,0], [0,y,0,0], [0,0,z,0], [0,0,0,1] ]
    global ctMatrix
    ctMatrix = matrix_multiplier(ctMatrix, transformationMatrix)
    stack[-1] = ctMatrix

def gtRotateX(theta):
    thetaRadians = radians(float(theta))
    transformationMatrix = [ [1,0,0,0], [0,cos(thetaRadians),-sin(thetaRadians),0], [0,sin(thetaRadians),cos(thetaRadians),0], [0,0,0,1] ]
    global ctMatrix
    ctMatrix = matrix_multiplier(ctMatrix, transformationMatrix)
    stack[-1] = ctMatrix

def gtRotateY(theta):
    thetaRadians = radians(float(theta))
    transformationMatrix = [ [cos(thetaRadians),0,sin(thetaRadians),0], [0,1,0,0], [-sin(thetaRadians),0,cos(thetaRadians),0], [0,0,0,1] ]
    global ctMatrix
    ctMatrix = matrix_multiplier(ctMatrix, transformationMatrix)
    stack[-1] = ctMatrix

def gtRotateZ(theta):
    thetaRadians = radians(float(theta))
    transformationMatrix = [ [cos(thetaRadians),-sin(thetaRadians),0,0], [sin(thetaRadians),cos(thetaRadians),0,0], [0,0,1,0], [0,0,0,1] ]
    global ctMatrix
    ctMatrix = matrix_multiplier(ctMatrix, transformationMatrix)
    stack[-1] = ctMatrix
    
def matrix_multiplier(before, changes):
    after = [ [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0] ]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                after[i][j] += before[i][k] * changes[k][j]
    return after
def gtGetMatrix():
    global ctMatrix
    return ctMatrix