
def multiply_matrices(A, B):    
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


def multiply_matrix_number(scalar, matrix):
    rows = len(matrix)
    columns = len(matrix[0])    
    for i in range(0,rows ):
        for j in range(0, columns):
            matrix[i][j] = matrix[i][j]*scalar
    return matrix


