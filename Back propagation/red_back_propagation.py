import random
import math
import copy


archivos = ["Gilberto1.txt","Gilberto2.txt","Gilberto3.txt","Gilberto4.txt","Gilberto5.txt", "Gilberto6.txt","Gilberto7.txt",
            "JE1.txt","JE2.txt","JE3.txt","JE4.txt", "JE5.txt","JE6.txt", "JE7.txt", 
            "firma1.txt","firma2.txt", "firma3.txt","firma4.txt", "firma5.txt", "firma6.txt", "firma7.txt",
            "Marco1.txt","Marco2.txt", "Marco3.txt","Marco4.txt", "Marco5.txt", "Marco6.txt", "Marco7.txt"]

esperado =[ [1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],
            [0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0],
            [0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0],
            [0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]


datos_evaluacion = ["Gilberto8.txt","Gilberto9.txt","Gilberto10.txt",
                    "JE8.txt","JE9.txt","JE10.txt",
                    "firma8.txt","firma9.txt", "firma10.txt",
                    "Marco8.txt","Marco9.txt", "Marco10.txt"]



# Funcion que recive dos matrices para ser multiplicadas   m*n n*y 
# m_a = matriz para operar 
# m_b matriz para operar 
# retorna una matriz
def multiplicar_matriz(m_a, m_b):    
    filas1 = len(m_a)    
    columnas1 = len(m_a[0])    
    columnas2 = len(m_b[0])        
    resultado_final = []
    for i in range(0, filas1):
        resultado_parcial= []
        for y in range(0, columnas2):
            sumatoria = 0
            for j in range(0, columnas1):
                    sumatoria += m_a[i][j]*m_b[j][y]
            resultado_parcial.append(sumatoria)            
        resultado_final.append(resultado_parcial)    
    return resultado_final

# Obtiene los patrones desde los txt 
# nombres = lista de strings
# Retorna una matriz con 1s y 0s 
def  get_patrones(nombres):
    patrones = []
    for nombre in nombres:   
        archivo  = open("bitmaps/"+nombre,mode="r")
        datos =  archivo.read()
        datos = datos.replace("\n","")
        archivo.close()
        patron = [ ]
        for i in datos:
            patron.append(float(i))
        patrones.append(patron)
    return patrones

# Obtiene los pesos 
# n_izquierda  = numero de neuronas al lado izquierdo. 
# n_derecha = numero de neuronas al lado derecho. 
# Retorna una matriz 
def generar_pesos(n_izquierda,n_derecha):
    pesos_generados = []
    for i in range(n_izquierda):
        valores = []
        for j in range(n_derecha):
            valores.append(random.uniform(-1,1)) 
        pesos_generados.append(valores)
    return pesos_generados

# Aplica la funcion sigmoidal a cada uno de los elementos de la net
# net_result = matriz 
# Retorna una matriz
def sigmoide(net_result):    
    sigmoide_result = []
    for y in net_result:
        sigmoide_result.append(1/ (1+ math.exp(-y)))
    return sigmoide_result 

# Calcula el error en la salida 
# deseados = lista de elementos deseados
# obtenidos = lista de elementos obtenidos 
# Retorna una lista 
def error_salida_sigmoide(deseados, obtenidos):    
    errores = []
    for d,y in zip(deseados, obtenidos):        
        errores.append((d-y)*(y*(1-y)))    
    return errores        


class Retropropagacion():
    def __init__(self, n_entradas,n_ocultas , n_salidas, t_a):
        self.wh = generar_pesos(n_entradas,n_ocultas)
        self.wo = generar_pesos(n_ocultas, n_salidas)
        self.aprendizaje = t_a
        self.h = []
        self.o = []
    
    # Calcula la net y le aplica sigmoidal 
    def net_sigmoide(self, patron):        
        self.h = sigmoide(multiplicar_matriz([patron], self.wh)[0])        
        self.o = sigmoide(multiplicar_matriz([self.h], self.wo)[0])        

    # Calcula el delta de la capa de salida
    def delta_salida(self, errores, salidas):
        resultados = []
        for error, salida in zip(errores, salidas):
            resultados.append(salida*(1-salida)*error)
        return resultados

    # Calcula el delta de la capa oculta 
    def delta_oculta(self,h, w2, delt_sal):
        resultado  = []
        for j, hj in enumerate(h):         
            sumatoria = 0               
            for k, delta in enumerate(delt_sal):
                sumatoria+= w2[j][k]*delta            
            resultado.append(hj*(1-hj)*sumatoria)                                        
        return resultado
    
    # Permite actualizar los pesos
    # pesos = matriz
    # I = lista
    # deltas = lista    
    def actualizar_pesos(self,pesos,I,deltas):        
        for i,values in enumerate(pesos):            
            for j, num in enumerate(values) :                
                pesos[i][j] = num + self.aprendizaje*I[i]*deltas[j]
        return pesos
    
    # Algoritmo principal 
    def entrenar_con_sigmoide(self, patrones, salidas_esperadas, iteraciones=10):
        while iteraciones>0:
            for patron, deseado in  zip(patrones, salidas_esperadas):
                self.net_sigmoide(patron)
                errores_salida = error_salida_sigmoide(deseado, self.o) 
                deltas_salida = self.delta_salida(errores_salida, self.o)                
                wo_copy = copy.deepcopy(self.wo)
                self.wo = self.actualizar_pesos(self.wo,self.h, deltas_salida)
                deltas_oculta = self.delta_oculta(self.h, wo_copy, deltas_salida)                
                self.wh = self.actualizar_pesos(self.wh, patron,deltas_oculta)      
            iteraciones -=1    
  
    # Calcula la salida para los patrones dados
    def evaluar_sigmoidal(self,patrones, sal ):
        print("\n Evaluación sigmoidal\n") 
        for d,i in enumerate(patrones):
            self.net_sigmoide(i)            
            for m in self.o:
                print(round(m, 1), end="  ")            
            print("--->  ",sal[d])
            print("\n")   
                                                                                                    
# Para  prueba con  XOR
"""
prueba = Retropropagacion(2,5, 1, 0.25)
prueba.entrenar_con_sigmoide([  [0,1],[  1,0],  [1,1],   [0,0]]  , [[1], [1], [0], [0]], 10000)
prueba.evaluar([[0,1],[1,0],[0,0],[1,1]],[[1], [1], [0],[0]])
"""

patrones = get_patrones(archivos)

# Para  prueba con  Imagenes
patrones_prueba = get_patrones(datos_evaluacion)
salidas_prueba = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
prueba1 = Retropropagacion(6000,30, 4, 0.25)
prueba1.evaluar_sigmoidal(patrones_prueba, salidas_prueba)
prueba1.entrenar_con_sigmoide(patrones, esperado, iteraciones=1)
prueba1.evaluar_sigmoidal(patrones_prueba, salidas_prueba)
i = input("press a key")



