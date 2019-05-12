import random
import math
class BackPropagation():
    def __init__(self, datos_entrada, tamaño_capa_oculta, numero_neuronas_salidas):  
        self.datos_entrada = datos_entrada
        self.datos_generados_capa_oculta = []
        self.datos_generados_capa_salida=[]
        self.tasa_aprendizaje = 0.25        
        self.capa_oculta = []
        self.capa_salida = []
        self.numero_neuronas_capa_oculta = tamaño_capa_oculta
        self.numero_neuronas_capa_salida = numero_neuronas_salidas
    
    def multiplicar_matrices(self, A,B): 
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

    def pesos_entrada_oculta(self):
        self.capa_oculta.clear()
        numero_neuronas =  len(self.datos_entrada[0][0])             
        while numero_neuronas>0:        
            numero_ocultas= self.numero_neuronas_capa_oculta
            pesos = []   
            while numero_ocultas>0:
                pesos.append(random.random())
                numero_ocultas-=1            
            self.capa_oculta.append(pesos)
            numero_neuronas-=1
        imprimir_matriz(self.capa_oculta)
        
    def pesos_oculta_salida(self):        
        self.capa_salida.clear()
        numero_neuronas = self.numero_neuronas_capa_oculta
        while numero_neuronas > 0:
            pesos = []
            neuronas_capa_salida = self.numero_neuronas_capa_salida
            while neuronas_capa_salida > 0:
                pesos.append(random.random())
                neuronas_capa_salida -=1
            numero_neuronas-=1
            self.capa_salida.append(pesos)            
        imprimir_matriz(self.capa_salida)  
  
    def net_capa_oculta(self, entradas):
        self.datos_generados_capa_oculta.clear()
        resultado = self.multiplicar_matrices(entradas,  self.capa_oculta)                 
        for i in resultado:
            self.datos_generados_capa_oculta.append(1/(1+math.exp(-i)))                        
    
    def net_capa_salida(self):
        resultados = self.multiplicar_matrices(self.datos_generados_capa_oculta, self.capa_salida)        
        for i in resultados:
            self.datos_generados_capa_salida.append(1/(1+math.exp(-i)))                        
        print(self.datos_generados_capa_salida)
    
    def calcular_error(self, esperado, salida):
        return esperado-salida
    
    def calcular_nuevos_pesos_salida(self):
        for i in self.capa_salida: 
            m =  1+i
            print(m)

    def entrenar(self):
        print ("....  Entrenando ....")
        #self.pesos_entrada_oculta()
        #self.pesos_oculta_salida()   
        imprimir_matriz(self.capa_oculta)
        self.net_capa_oculta([0,1])        
        if (self.calcular_error(1,self.net_capa_salida())):                    
            self.calcular_nuevos_pesos_salida()                     
def imprimir_matriz(matriz):
    print("-"*60)
    print("[")
    for i in matriz:
        print(i)            
    print("]")
    print("-"*60)
datos = ([[[0, 0], 0], [[0, 1], 1], [[1, 0], 1], [[1, 1], 0]])

red = BackPropagation(datos, 2, 1)
red.entrenar()


