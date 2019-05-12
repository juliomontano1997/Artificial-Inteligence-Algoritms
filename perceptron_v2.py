import random
class Neurona:
    def __init__(self): 
        self.pesos = []
        self.datos_entrenamiento = []
        self.umbral = 0.5
        self.tasa_de_aprendizaje = 0.1
    
    def generar_pesos(self, datos):
        self.pesos.clear()                        
        numero_de_datos = len(datos)                    
        while numero_de_datos>0:       
            self.pesos.append(random.random())  
            numero_de_datos -=1   
                  
    
    def calcular_net(self, datos, pesos):
        return sum(valor * peso for valor, peso in zip(datos, pesos))


    def escalon(self, resultado_net):
        if resultado_net>self.umbral:
            return 1
        else: 
            return 0
    def ajuste_pesos(self, vector_de_entrada, error):
        for indice, valor in enumerate(vector_de_entrada):
            self.pesos[indice] += self.tasa_de_aprendizaje * error * valor

    def entrenar(self, datos):
        self.datos_entrenamiento = datos
        self.generar_pesos(datos[0][0])
        
        while True:            
            contador_de_errores = 0            
            for vector_de_entrada, salida_deseada in self.datos_entrenamiento:                
                resultado = self.escalon(self.calcular_net(vector_de_entrada, self.pesos))
                error = salida_deseada - resultado                                                
                if error != 0:
                    contador_de_errores += 1
                    self.ajuste_pesos(vector_de_entrada,error)               
            if contador_de_errores == 0:
                break

    def evaluar(self, datos):
        net = self.calcular_net(datos, self.pesos)
        print(net)
        print(self.escalon(net))



perceptron = Neurona()
perceptron.entrenar([[[1, 0, 0], 0], [[1, 0, 1], 0], [[1, 1, 0], 0], [[1, 1, 1], 1]])
perceptron.evaluar([1,1,1])