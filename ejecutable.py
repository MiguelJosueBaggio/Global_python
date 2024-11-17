import random
from Clases import Detector, Radiacion, Virus, Sanador

def obtener_matriz():
    print("Ingresa la matriz de ADN (6 filas, 6 columnas):")
    matriz = [input().strip().upper() for i in range(6)] #el metodo .strip remueve los espacios vacios al momento de ingresar la cadena 
    return matriz

def main():
    matriz = obtener_matriz()
    print("Selecciona una opción:")
    print("1. Detectar mutaciones")
    print("2. Crear mutación")
    print("3. Sanar mutaciones")

    
    opcion = input("Opción: ").strip()

    if opcion == "1":
        detector = Detector("Detector de ADN")
        if detector.detector_mutantes(matriz):
            print("Mutaciones detectadas.")
        else:
            print("No se detectaron mutaciones.")
    elif opcion == "2":
        print("Selecciona tipo de mutación:")
        print("1. Radiación (horizontal/vertical)")
        print("2. Virus (diagonal)")
        tipo = input("Tipo: ").strip()
        base = input("Base nitrogenada (A/T/C/G): ").strip().upper()
        fila = int(input("Fila inicial (0-5): ").strip())
        col = int(input("Columna inicial (0-5): ").strip())
        if tipo == "1":
            orientacion = input("Orientación (H/V): ").strip().upper()
            radiacion = Radiacion(base, "Mutación", "Alta")
            nueva_matriz = radiacion.crear_mutante(base, [fila, col], orientacion, matriz)
        elif tipo == "2":
            virus = Virus(base, "Mutación", "Alta")
            nueva_matriz = virus.crear_mutante(base, [fila, col], matriz)
        print("Matriz mutada:")
        for fila in nueva_matriz:
            print(fila)
    elif opcion == "3":
        sanador = Sanador("Sanador de ADN", "Regeneración")
        nueva_matriz = sanador.sanar_mutantes(matriz)
        print("Matriz sanada:")
        for fila in nueva_matriz:
            print(fila)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
