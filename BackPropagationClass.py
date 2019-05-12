class Backpropagation:

    def __init__(self, dataSet, expectedOutputs, n_hiddenNodes, n_outputNodes):
        self.dataSet = dataSet
        self.expectedOutputs = expectedOutputs
        self.n_hiddenNodes = n_hiddenNodes
        self.n_outputNodes = n_outputNodes

    def multiply_matrices(self, A, B):    
        if len(A) != len(B):
            print("Las matrices no son compatibles")
            exit()        
        result = []
        for i in range(0,len(B[0])):
            sumatory = 0
            for j in range(0,len(A)):                        
                sumatory += A[j]*B[j][i]
            result.append(sumatory)
        return result

    def multiply_matrix_number(self, scalar, matrix):
        rows = len(matrix)
        columns = len(matrix[0])    
        for i in range(0,rows ):
            for j in range(0, columns):
                matrix[i][j] = matrix[i][j]*scalar
        return matrix

    def substractMatrix(self, matrixWeight, updatedMatrixWeights): #substract matrix values, they must be the same length.
        resultMatrix = []
        for i,weight in enumerate(matrix):
            values = []
            for j,value in enumerate(weight):
                values.append( matrixWeight[i][j]-matrixUpdated[i][j] )        
            resultMatrix.append( values )
        print(resultMatrix)

    def delta(self, predict, actual): #actual is our expected output
        return predict - actual

    def error(self, predict, actual):
        1/2*( (predict-actual)**2 )
