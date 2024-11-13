

class Detector:
    def __init__(self,especie,variedad) :
        self.especie=especie
        self.variedad=variedad
        
    

    def generador_de_codigo1(self): ##Generador de codgio genetico
        
        list_codigo = [] ##hacer lista
        for i in range (0,6): #hacer una lista de 6 string de 6 letras
         max_letras=6
         while True: ##Se hace con while true para hacerlo de 6 letras
          codigo = input ("ingrese 6 bases ")
          codigo_min = codigo.lower() ##pasaje a minuscula
          if len(codigo_min) == max_letras : ##valida para que tenga las letras pertinentes
               list_codigo.append(codigo )
          
               break
          
          print("cadena incorrecto continue")
           
        return list_codigo
    codigo_genetico = generador_de_codigo1


especie1 = Detector("Vitis_Vinifera","Malbec")

codigo_genetico = especie1.generador_de_codigo1()


for i in range(6):
   print(codigo_genetico[i])
   

             
             
                

          
                     


        



















