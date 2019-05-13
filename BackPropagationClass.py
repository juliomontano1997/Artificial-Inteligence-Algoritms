import random

class Backpropagation:
    def __init__(self, dataSet, expectedOutputs, n_hiddenNodes, n_outputNodes):
        self.dataSet = dataSet
        self.expectedOutputs = expectedOutputs
        self.n_hiddenNodes = n_hiddenNodes
        self.n_outputNodes = n_outputNodes
        self.a = 0.25
        self.hidden_weights = []
        self.outputs_weights = []
        self.entry_data = []
        self.hidden_data = []
        self.output_data = []
        self.error_obtained = 0
        
    def multiply_matrices(self, A, B):    
        '''if len(A) != len(B):
            print("Las matrices no son compatibles")
            exit()        '''
        
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
        for i,weight in enumerate(matrixWeight):
            values = []
            for j,value in enumerate(weight):
                values.append( matrixWeight[i][j]-updatedMatrixWeights[i][j] )        
            resultMatrix.append( values )
        print(resultMatrix)

    def delta(self, predict, actual): #actual is our expected output
        return predict - actual

    def error(self, predict, actual):
        return 1/2*( (predict-actual)**2 )

    def generate_random_matrix(self, rows, colums):
        matrix = []
        for i in range(0, rows):
            row = []
            for j in range(0, colums):
                row.append(random.random())
            matrix.append(row)
        return matrix 
    
    def generate_array(self, elements):
        new_array = []
        for i in range(0, elements):
            new_array.append(0)
        return new_array
    
    def train(self):
        self.hidden_weights = [[0.11, 0.12], [0.21, 0.08]]#self.generate_random_matrix(len(self.dataSet[0]), self.n_hiddenNodes)
        self.outputs_weights = [[0.14],[0.15]]#self.generate_random_matrix(self.n_hiddenNodes, self.n_outputNodes)                
        
        self.hidden_data = self.generate_array(self.n_hiddenNodes)
        self.output_data = self.generate_array(self.n_outputNodes)

        for index, value in enumerate(self.dataSet):            
            self.hidden_data = self.multiply_matrices(value, self.hidden_weights)
            self.output_data = self.multiply_matrices(self.hidden_data, self.outputs_weights)
            self.error_obtained =  self.error(self.output_data[0], self.expectedOutputs[index])                        
            print(self.error_obtained)

x = Backpropagation([[2,3]], [1],2, 1)
x.train()
        

    


    