# [1,2,3, n]  [[0,2,3,4,5..n], n]
def multiplicar_matrices(A,B): 
    if(len(A)!= len(B)):
        print("Las matrices no se pueden multiplicar")                
        exit()
    resultado = []
    for i in range(0,len(B[0])):
        suma = 0
        for j in range(0,len(A)):                        
            suma += A[j]*B[j][i]
        resultado.append(suma)
    return resultado

print(multiplicar_matrices([0,1],[[0.1, 0.5], [-0.7,0.3]]))

            