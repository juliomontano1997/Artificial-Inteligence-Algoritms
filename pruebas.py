import random
import math
archivos = ["Gilberto1.txt","Gilberto2.txt","Gilberto3.txt","Gilberto4.txt","Gilberto5.txt", 
            "Gilberto6.txt","Gilberto7.txt", "Gilberto8.txt",

            "JE1.txt","JE2.txt","JE3.txt","JE4.txt", "JE5.txt",
            "JE6.txt", "JE7.txt","JE8.txt",
            "firma1.txt","firma2.txt", "firma3.txt","firma4.txt", "firma5.txt",
            "firma6.txt", "firma7.txt","firma8.txt", 
            "Marco1.txt","Marco2.txt", "Marco3.txt","Marco4.txt", "Marco5.txt",
            "Marco6.txt", "Marco7.txt","Marco8.txt"]

esperado = [1,1,1,1,1,1,1,1,
            2,2,2,2,2,2,2,2,
            3,3,3,3,3,3,3,3,
            4,4,4,4,4,4,4,4]

pruebas = ["Gilberto9.txt","Gilberto10.txt", "JE9.txt","JE10.txt", "firma9.txt","firma10.txt","Marco9.txt","Marco10.txt"]

def get_list_bits(nombre):    
    archivo  = open("bitmaps/"+nombre,mode="r")
    datos =  archivo.read()
    datos = datos.replace("\n","")

    archivo.close()
    return list(datos)

class Backpropagation:
    def __init__(self, n_entries, n_hiddenNodes, n_outputNodes):
                         
        self.learning_rate= 0.05
        self.Wh = self.generate_random_matrix(n_entries, n_hiddenNodes)
        self.Wo = self.generate_random_matrix(n_hiddenNodes, n_outputNodes)      
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
                    result += (A[i][j])*(B[j][y])
                new_r.append(result)            
            new_m.append(new_r)                
        return new_m

    def multiply_matrix_number(self, scalar, matrix):
        rows = len(matrix)
        columns = len(matrix[0])    
        for i in range(0,rows ):
            for j in range(0, columns):
                matrix[i][j] = (matrix[i][j])*scalar
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
            delt += predict  - actual
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

    def convert_to_int(self,array):
        newa =[]
        for i in array:
            newa.append(int(i))
        return newa

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
                

    def train(self,dataSet,expectedOutputs): 
        self.dataSet = dataSet
        self.expectedOutputs = expectedOutputs         
        iterations = 0
        #while self.error_obtained < -0.01 or self.error_obtained>0.01 :   
        while iterations<10:                                
            for index, I in enumerate(self.dataSet):
                #print(index)
                I = get_list_bits(I)  
                I = self.convert_to_int(I)                                                                   
                # forward propagation 
                self.H = self.multiply_matrices([I], self.Wh)       
                self.H = self.apply_bias(self.H,1) 
                self.H = self.apply_sigmoide(self.H)                      
                self.O = self.multiply_matrices(self.H, self.Wo)  
                self.O = self.apply_bias(self.O,1) 
                self.O = self.apply_sigmoide(self.O)                                    
                self.error_obtained = self.error(self.O[0], self.expectedOutputs[index]/4)                                
                #back propagation      
                #print(self.O)
                #print(self.error_obtained)
                delta = self.delta(self.O[0], self.expectedOutputs[index]/4)                
                h_matrix = self.array_to_matrix(self.H[0])
                wo_copy = self.Wo
                self.Wo = self.substractMatrix(self.Wo, self.multiply_matrix_number(self.learning_rate*delta, h_matrix))                
                i_matrix = self.array_to_matrix(I)                                    
                self.Wh = self.substractMatrix(self.Wh,self.multiply_matrices(self.multiply_matrix_number(self.learning_rate*delta,i_matrix),[self.matrix_to_array(wo_copy)]))                                               
            iterations+=1
            print(iterations)

        
    def evaluate(self, I):
        I = get_list_bits(I)  
        I = self.convert_to_int(I)   
        self.H = self.multiply_matrices([I], self.Wh)        
        self.O = self.multiply_matrices(self.H, self.Wo)         
        print(self.O)                

x = Backpropagation(6000,3, 1)
x.train(archivos,esperado)

for i in pruebas:
    x.evaluate(i)
c = input("Press a key")

    


    


    
