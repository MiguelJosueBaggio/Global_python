import random
class Detector:
    metodo = "Polimorfismo de conformacion de cadena sencilla" 
    siglas = "SSCP"

    def __init__(self,nombre:str):
        self.nombre = nombre
        self.resultadoHorizontal = None
        self.resultadoVertical = None #como la funciona para crear? De momento las copie del global para probar que funcione
        self.resultadoDiagonal = None
        self.mutado = False

    def detector_mutantes(self,matrizADN):
        # otra posible solucion return any([ 
        #self.detector_horizontal(matrizADN),
        #self.detector_vertical(matrizADN),
        #self.detector_diagonal(matrizADN)
    ######])
        # print(any(matrizADN)) devuelve TRUE si al menos uno de los elementos es TRUE
        # self.mutado = any([resultadoHorizontal,resultadoVertical,resultadoDiagonal])
        resultadoHorizontal = self.detector_horizontal(matrizADN)
        resultadoVertical = self.detector_vertical(matrizADN)
        resultadoDiagonal = self.detector_diagonal(matrizADN)
        self.mutado= resultadoHorizontal or resultadoVertical or resultadoDiagonal
        return self.mutado
    
    def detector_horizontal(self, matrizADN):
        for fila in matrizADN: #
            for i in range(len(fila) - 3): #La idea es de encontrar 4 caracteres juntos. por eso se analiza de 6 (longitud de la fila menos 3 para uqe no se pase)
                secuencia = fila[i:i+4] #luego el set, cuanta los caracteres unicos, entonces si hay 4 iguales lo tomaria como 1
                if len(set(secuencia)) == 1: #set, cuenta los caracteres unicos
                    return True #En base al set hice los demas, solo que con mas for
        return False
    
    def detector_vertical(self, matrizADN):
        # Recorrer las posiciones de las columnas
        for i in range(len(matrizADN[0])):  #  todas las palabras tienen la misma longitud
        # Recorrer las filas de la columna, pero asegurándonos de no ir más allá de la longitud de la matriz
            for j in range(len(matrizADN) - 3):  # Restamos 3 para asegurarnos de que podemos obtener 4 caracteres consecutivos
            # Crear una secuencia de 4 caracteres consecutivos en la columna
                secuencia = [matrizADN[j+k][i] for k in range(4)]
            
            # Verificar si la secuencia tiene todos los caracteres iguales
                if len(set(secuencia)) == 1:  # Si la secuencia tiene solo un elemento distinto
                    return True  # Se encontró una mutación, retornar True
        return False
    
    def detector_diagonal(self, matrizADN):
        filas = len(matrizADN)
        columnas = len(matrizADN[0])
        secuencia = 4  # Número de letras consecutivas que estamos buscando

    # Verificar diagonales descendentes (de izquierda a derecha) (range no incluye el valor final)
        for i in range(filas - secuencia + 1):  # Iteramos sobre las filas range(0,3)-0,1,2
            for j in range(columnas - secuencia + 1):  # Iteramos sobre las columnas
            # Comprobamos la secuencia diagonal descendente
                letras = [matrizADN[i+k][j+k] for k in range(secuencia)]
                if len(set(letras)) == 1:  # Si todas las letras son iguales
                    return True

    # Verificar diagonales ascendentes (de abajo hacia arriba)
        for i in range(secuencia - 1, filas):  # Comenzamos desde la fila inferior range(3,6)-(3,4,5)
            for j in range(columnas - secuencia + 1):  # Iteramos sobre las columnas
            # Comprobamos la secuencia diagonal ascendente
                letras = [matrizADN[i-k][j+k] for k in range(secuencia)]
                if len(set(letras)) == 1:  # Si todas las letras son iguales
                    return True

        return False
    
class Sanador(Detector):#Lo hice como si fuera hija asi hereda el detector mutante (lo dijo el profe en una co)
    def __init__(self,nombre:str, nombreMetodo:str):
        super().__init__(nombre) #??
        self.metodo_sanacion = nombreMetodo

    def sanar_mutantes(self,matrizADN):
        self.mutado = super().detector_mutantes(matrizADN) #Aca se fija si hay mutacion
        print("Es mutado o no?", self.mutado) #Esto es para mi, porque no sabia si salia bien el codigo se puede borrar despues
        bases_permitidas = ["C","T","A","G"]
        while self.mutado == True:#Si hay genera una random, como las letras permitidas
            matriz_sanada = [''.join(random.choice(bases_permitidas)for _ in range(6)) for _ in range(6)]
            self.mutado = super().detector_mutantes(matriz_sanada) #Verifica si tiene mutacion
            
            if self.mutado == False:#Recien cuando no tenga la imprime
                print(matriz_sanada)
        return matriz_sanada  
