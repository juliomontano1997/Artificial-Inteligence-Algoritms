import random
import math

class Backpropagation:
    def __init__(self, dataSet, expectedOutputs, n_hiddenNodes, n_outputNodes):
        self.dataSet = dataSet
        self.expectedOutputs = expectedOutputs
        self.n_hiddenNodes = n_hiddenNodes
        self.n_outputNodes = n_outputNodes
        self.learning_rate= 0.01
        self.Wh = []
        self.Wo = []
        self.I = []
        self.H = []
        self.O = []
        self.error_obtained = 1
        
    def multiply_matrices(self, A, B):    
        A_R = len(A)    
        A_C = len(A[0])
        B_R = len(B)
        B_C = len(B[0]) 
        if (A_C!= B_R):
            print("No se pueden multiplicar")
            exit()
        new_m = []
        for i in range(0, A_R):
            new_r = []
            for y in range(0, B_C):
                result = 0
                for j in range(0, A_C):
                    result += A[i][j]*B[j][y]
                new_r.append(result)            
            new_m.append(new_r)                
        return new_m

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
                values.append(matrixWeight[i][j]-updatedMatrixWeights[i][j])        
            resultMatrix.append( values )
        return resultMatrix

    def delta(self,net_results, actual): #actual is our expected output
        delt = 0
        for predict in net_results:
            delt += actual  - predict           
        return delt

    def error(self, net_results, actual):
        err = 0
        for predict in net_results: 
            err += 0.5*((predict-actual)**2 )     
        return err

    def generate_random_matrix(self, rows, colums):
        matrix = []
        for i in range(0, rows):
            row = []
            for j in range(0, colums):
                row.append(random.random())
            matrix.append(row)
        return matrix 
    
    def array_to_matrix(self, array):                      
        matrix = []
        for i in array:
            matrix.append([i])
        return matrix

    def matrix_to_array(self, matrix):
        array = []
        for i in matrix:
            array.append(i[0])
        return array

    def apply_sigmoide(self,matrix):          
        Q_R = len(matrix)                
        Q_F = len(matrix[0])
        for i in range(0, Q_R):
            for j in range(0, Q_F):
                matrix[i][j] = 1/ (1+ math.exp(-matrix[i][j]))       
        return matrix
    
    def apply_bias(self, matrix, bias):
        Q_R = len(matrix)                
        Q_F = len(matrix[0])
        for i in range(0, Q_R):
            for j in range(0, Q_F):
                matrix[i][j] = matrix[i][j] + bias        
        return matrix
                

    def train(self): 
        self.Wh = self.generate_random_matrix(len(self.dataSet[0]), self.n_hiddenNodes)
        self.Wo = self.generate_random_matrix(self.n_hiddenNodes, self.n_outputNodes)        
        self.bias_1 = 1
        self.bias_2 = 1        
        #iterations = 0
        while self.error_obtained > 0.001 :                                                  
            for index, I in enumerate(self.dataSet):                
                self.H = self.multiply_matrices([I], self.Wh)
                #self.H = self.apply_bias(self.H,self.bias_1) 
                #self.H = self.apply_sigmoide(self.H)               
                self.O = self.multiply_matrices(self.H, self.Wo) 
                #self.O = self.apply_bias(self.O,self.bias_2) 
                #self.O = self.apply_sigmoide(self.O)                                                                                   
                self.error_obtained = self.error(self.O[0], self.expectedOutputs[index])                
                delta = self.delta(self.O[0], self.expectedOutputs[index])                    
                h_matrix = self.array_to_matrix(self.H[0])
                wo_copy = self.Wo
                self.Wo = self.substractMatrix(self.Wo, self.multiply_matrix_number(self.learning_rate*delta, h_matrix))        
                i_matrix = self.array_to_matrix(I)                                    
                self.Wh = self.substractMatrix(self.Wh,self.multiply_matrices(self.multiply_matrix_number(self.learning_rate*delta,i_matrix),[self.matrix_to_array(wo_copy)])) 
            #iterations +=1

    def evaluate(self, entry):
        self.H = self.multiply_matrices([entry], self.Wh)
        self.H = self.apply_bias(self.H,self.bias_1) 
        self.H = self.apply_sigmoide(self.H)               
        self.O = self.multiply_matrices(self.H, self.Wo) 
        self.O = self.apply_bias(self.O,self.bias_2) 
        self.O = self.apply_sigmoide(self.O)     
        print(self.O)                


x = Backpropagation([[1,1],[0,1],[1,0],[0,0]], [1,0,0,0],6, 1)
x.train()
x.evaluate([1,1])
x.evaluate([0,1])
x.evaluate([1,0])
x.evaluate([0,0])
c = input("Press a key")

    


    
