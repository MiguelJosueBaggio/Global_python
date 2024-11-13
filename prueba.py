class Detector: 
    def __init__(self,especie,variedad,codigo_genetico) :
        self.__especie= especie
        self.__variedad= variedad
        self.codigo_genetico =codigo_genetico
        
    def mostrar_lista(self): ##muestra la lita del codigo genetico
       for i in range(6):
        print(codigo_genetico[i])
   
    def get_especie (self): ##Getters para obtener especie y variedad
        return self.__especie
    def get_variedad (self):
        return self.__variedad

    def set_especie (self,especie): ## setter para modificar especie y variedad
        self.__especie = especie 

    def set_variedad (self, variedad):
        self.__variedad = variedad



    def detectar_mutantes_horizontales (self, codigo_genetico): ##detectar mutantes horizontales
        mutantes = False ## variable local para iniciar que la prescencia de mutantes es falsa
        numero_mutantes = 0 ## contador de numero de mutantes
        for codigo in codigo_genetico: ##Recorre la lista del codigo genetico
            codigo_lista =[]
            codigo_lista = list(codigo) ## transformamos en lista cada codigo que es un String

            
            if ((codigo_lista[0] == codigo_lista[1]) and (codigo_lista[1] == codigo_lista[2] ) and (codigo[2] == codigo[3])) or ((codigo_lista[1] == codigo_lista[2]) and (codigo_lista[2] == codigo_lista[3]) and (codigo_lista[3] == codigo_lista[4])) or ((codigo_lista[2] == codigo_lista[3]) and (codigo_lista[3] == codigo_lista[4]) and (codigo_lista[4] == codigo_lista[5])): ## da la condicion de que aparezcan 4 veces repetidas en la fila
              mutantes = True ## si se cumple la condicion
              numero_mutantes = numero_mutantes + 1
   
        print (f"La presencia de mutantes horizontales es:{mutantes} y el nmuero de mutantes es {numero_mutantes } ") 


    def detector_mutantes_verticales (self,codigo_genetico):
        mutantes_ver = False
        numero_mutantes = 0
        for codigo in codigo_genetico: ##Recorre la lista del codigo genetico
            codigo_lista =[]
            codigo_lista = list(codigo) ## transformamos en lista cada codigo que es un String
        for i in range (0,6):
            if (codigo_genetico[0][i]==codigo_genetico[1][i]==codigo_genetico[2][i]==codigo_genetico[3][i]) or (codigo_genetico[1][i]==codigo_genetico[2][i]==codigo_genetico[3][i]==codigo_genetico[4][i]) or (codigo_genetico[2][i]==codigo_genetico[3][i]==codigo_genetico[4][i]==codigo_genetico[5][i]) :
               mutantes_ver = True ## si se cumple la condicion
               numero_mutantes = numero_mutantes + 1

        print (f"La presencia de mutantes verticales es:{mutantes_ver} y el nmuero de mutantes es {numero_mutantes } ")

    def detector_mutantes_diagonales (self,codigo_genetico):
        mutantes_diag = False
        numero_mutantes = 0
        for codigo in codigo_genetico: ##Recorre la lista del codigo genetico
            codigo_lista =[]
            codigo_lista = list(codigo) ## transformamos en lista cada codigo que es un String
        
        if (codigo_genetico[0][0]==codigo_genetico[1][1]==codigo_genetico[2][2]==codigo_genetico[3][3]) or (codigo_genetico[1][1]==codigo_genetico[2][2]==codigo_genetico[3][3]==codigo_genetico[4][4]) or (codigo_genetico[2][2]==codigo_genetico[3][3]==codigo_genetico[4][4]==codigo_genetico[5][5]):
               mutantes_diag = True ## si se cumple la condicion
     
               numero_mutantes = numero_mutantes + 1
               if (codigo_genetico[0][5]==codigo_genetico[1][4]==codigo_genetico[2][3]==codigo_genetico[3][2]) or (codigo_genetico[1][4]==codigo_genetico[2][3]==codigo_genetico[3][2]==codigo_genetico[4][1]) or (codigo_genetico[2][3]==codigo_genetico[3][2]==codigo_genetico[4][1]==codigo_genetico[5][1]) :
                    mutantes_diag= True
                    numero_mutantes=numero_mutantes+1
        print (f"La presencia de mutantes diagonales es:{mutantes_diag} y el nmuero de mutantes es {numero_mutantes } ")



#####################################################################
def generador_de_codigo1(): ##Generador de codgio genetico
        
        list_codigo = [] ##hacer lista
        for i in range (0,6): #hacer una lista de 6 string de 6 letras
         max_letras=6
         while True: ##Se hace con while true para hacerlo de 6 letras
          codigo = input ("ingrese 6 bases ")
          codigo_min = codigo.lower() ##pasaje a minuscula
          if len(codigo_min) == max_letras : ##valida para que tenga las letras pertinentes
               list_codigo.append(codigo_min )
          
               break
          
          print("cadena incorrecto continue")
           
        return list_codigo
     

codigo_genetico = generador_de_codigo1()

especie1 = Detector("Vitis_Vinifera","Malbec",codigo_genetico)

especie1.mostrar_lista()

print(especie1.get_especie())

especie1.detectar_mutantes_horizontales(codigo_genetico)
especie1.detector_mutantes_verticales(codigo_genetico)
especie1.detector_mutantes_diagonales(codigo_genetico)
   

             
             
                

          
                     


        