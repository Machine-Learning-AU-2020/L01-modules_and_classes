import numpy as np

def printThis(x):
    print(x)

def importDefaults():
    import numpy as np
    import os

def L1(x):
    return np.sum(np.absolute(x))

def L2(x):
    val = np.square(x)
    valSum = np.sum(val)
    return np.sqrt(valSum)

def L2Dot(x):
    return np.sqrt(np.sum(np.dot(x, x)))

def RMSE(xPred, yTrue):
    dif = xPred - yTrue
    difSquared = np.square(dif)
    difSquaredSum = np.sum(difSquared)
    val = np.divide(difSquaredSum, len(xPred))
    rmseVal = np.sqrt(val)
    
    return rmseVal

def MAE(xPred, yTrue):
    dif = xPred - yTrue
    difSquared = np.absolute(dif)
    difSquaredSum = np.sum(difSquared)
    maeVal = np.divide(difSquaredSum, len(xPred))
    
    return maeVal

