archivos = ["Gilberto1.txt","Gilberto2.txt","Gilberto3.txt","Gilberto4.txt","Gilberto5.txt", 
    "Gilberto6.txt","Gilberto7.txt", "Gilberto8.txt","Gilberto9.txt","Gilberto10.txt",
    "JE1.txt","JE2.txt","JE3.txt","JE4.txt", "JE5.txt",
    "JE6.txt", "JE7.txt","JE8.txt", "JE9.txt","JE10.txt",
    "firma1.txt","firma2.txt", "firma3.txt","firma4.txt", "firma5.txt",
    "firma6.txt", "firma7.txt","firma8.txt", "firma9.txt","firma10.txt",
    "Marco1.txt","Marco2.txt", "Marco3.txt","Marco4.txt", "Marco5.txt",
    "Marco6.txt", "Marco7.txt","Marco8.txt", "Marco9.txt","Marco10.txt"
]

esperado = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4]   

def get_bits(nombre):    
    archivo  = open("bitmaps/"+nombre,mode="r")
    datos =  archivo.read()
    datos = datos.replace("\n","")

    archivo.close()
    return list(datos)

