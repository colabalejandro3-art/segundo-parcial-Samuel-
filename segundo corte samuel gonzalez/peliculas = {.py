peliculas = {
    "1": ("Sonic", 12000, 50),
    "2": ("Mario Bros", 10000, 40),
    "3": ("Duna", 15000, 30),
    "4": ("Barbie", 11000, 25)
}

historial = []

def mostrar():
    print("\nPeliculas disponibles:")
    for i in peliculas:
        print(i, peliculas[i][0], "-", peliculas[i][1], "Disponibles:", peliculas[i][2])

def comprar():
    mostrar()
    op = input("Elija pelicula: ")
    
    if op not in peliculas:
        print("Opcion mala")
        return
    
    nombre, precio, disp = peliculas[op]
    
    try:
        cant = int(input("Cuantas boletas: "))
    except:
        print("Eso no es numero")
        return
    
    if cant > disp:
        print("No hay tantas")
        return
    
    total = cant * precio
    peliculas[op] = (nombre, precio, disp - cant)
    
    historial.append((nombre, cant, total))
    
    print("Compraste", cant, "para", nombre)
    print("Total:", total)

def ver_historial():
    if len(historial) == 0:
        print("Nada comprado")
    else:
        for h in historial:
            print(h)

while True:
    print("\n1. Comprar")
    print("2. Historial")
    print("3. Salir")
    
    op = input("-> ")
    
    if op == "1":
        comprar()
    elif op == "2":
        ver_historial()
    elif op == "3":
        break
    else:
        print("No valido")