matrixUpdated = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]
matrix = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

def substractMatrix(matrixWeight, updatedMatrixWeights): #substract matrix values, they must be the same length.
    resultMatrix = []

    for i,weight in enumerate(matrix):
        values = []
        for j,value in enumerate(weight):
            values.append( matrixWeight[i][j]-matrixUpdated[i][j] )
        
        resultMatrix.append( values )

    print(resultMatrix)

substractMatrix(matrix, matrixUpdated)

def delta(predict, actual): #actual is our expected output
    return predict - actual

def error(predict, actual):
    1/2*(predict-actual)**2
