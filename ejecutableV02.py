from clases import Detector, Radiacion, Virus, Sanador

def obtener_matriz():
    print("""
Ingresa la secuencia de ADN:
    Bases nitrogenadas permitidas Adenina(A), Timina(T), Guanina(G) y Citocina(C)
    Debe tener 6 bases nitrogenadas cada fila
          """)
    matriz = []
    for i in range(6):
        while True:
            fila = input(f"Fila {i + 1}: ").strip().upper()
            if len(fila) == 6 and all(base in "ATCG" for base in fila):
                matriz.append(fila)
                break
            else:
                print("Secuencia no permitida. Debe tener solo 6 bases nitrogenadas (A, T, G y C)")
    return matriz

def obtener_entrada_mutacion():
    while True:
        try:
            tipo = input("Selecciona tipo de mutación (1 - Radiacion, 2 - Virus): " ).strip()
            if tipo not in ["1", "2"]:
                raise ValueError("Opción inválida.")
            
            base = input("Seleccione una base nitrogenada (A/T/C/G): ").strip().upper()
            if base not in "ATCG":
                raise ValueError("Base nitrogenada inválida.")
            
            fila = int(input("Fila inicial (0-5): ").strip())
            col = int(input("Columna inicial (0-5): ").strip())
            if not (0 <= fila < 6 and 0 <= col < 6):
                raise ValueError("Las coordenadas deben estar entre 0 y 5.")
            
            if tipo == "1":
                orientacion = input("Orientación (H/V): ").strip().upper()
                if orientacion not in ["H", "V"]:
                    raise ValueError("Orientación inválida.")
                return tipo, base, fila, col, orientacion
            elif tipo == "2":
                return tipo, base, fila, col, None
        except ValueError as e:
            print(e)

def main():
    matriz = obtener_matriz()
    while True:
        print("""
------------------------------
Seleccione una opción:
    1. Detectar mutaciones
    2. Crear mutación
    3. Sanar mutaciones
    4. Mostrar matriz actual
    5. Salir    
            """)
       
    
        opcion = input("Opción: ").strip()

        match opcion:
            case "1":
                detector = Detector("Detector de ADN")
                if detector.detector_mutantes(matriz):
                    print ("Se ha detectado una mutacion.")
                else:
                    print("No se presentan mutaciones.")
            case "2":
                tipo, base, fila, col, orientacion = obtener_entrada_mutacion()
                if tipo == "1":
                    radiacion = Radiacion(base, "Mutación", "Alta")
                    matriz = radiacion.crear_mutante(base, [fila, col], orientacion, matriz)
                elif tipo == "2":
                    virus = Virus(base, "Mutación", "Alta")
                    matriz = virus.crear_mutante(base, [fila, col], matriz)
                    
                print("Matriz mutada:")
                for fila in matriz:
                    print(f"\t{fila}")
                print(f"Se ha realizado la mutacion")
            case "3":
                sanador = Sanador("Sanador de ADN", "Regeneración")
                matriz = sanador.sanar_mutantes(matriz)
                print("Matriz sanada:")
                for fila in matriz:
                   print(f"\t{fila}")
            case "4":
                print("matriz actual")
                for fila in matriz:
                    print(f"\t{fila}")
            case "5":
                print("Salir")
                break
            case _:
                print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
