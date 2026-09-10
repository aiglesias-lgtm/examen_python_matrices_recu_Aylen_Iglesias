#la matriz empieza vacia :
matriz = None 
# menu :
while True:
    print ("\n MENU")
    print ("1. Carga de matrices")
    print ("2. Mostrar la matriz cargada")
    print ("3. Sumatoria")
    print ("4. Productoria")
    print ("5. Transrespuesta")
    print ("6. Salir")

    opcion = int(input("Ingrese la opcion deseasa: "))

# si es opcion 1 :
    if opcion == 1:
        fila = int(input("\n Ingrese la cantidad de filas deseada: "))
        columna = int(input("\n Ingrese la cantidad de columnas deseada: "))
        matriz = []

        for i in range(fila):
            fila = []
            for j in range(columna):
                posicion = int(input("ingrese los valores deseados: "))
                fila.append(posicion)
            matriz.append(fila)
        print ("\n Matriz cargada")

#si es opcion 2 :
    elif opcion == 2:
        if matriz is None:
            print ("Se debe de cargar una matriz antes")
        else:
            print ("Matriz cargada: ")
            for fila in matriz:
                print (fila)

#si es opcion 3 :
    elif opcion == 3:
        if matriz is None:
            print ("se debe de hacer una matriz antes")
        else: 
            suma = 0

            for fila in matriz:
                for elemento in fila:
                    suma += elemento 
            print ("\n La suma total de la matriz es ",suma)

#si es opcion 4 :
    elif opcion == 4:
        if matriz  is None:
            print ("Se debe de hacer una matriz")
        else:
            productorio = 1
            for fila in matriz:
                for elemento in fila:
                    productorio *= elemento
            print ("\n La productoria total es: ",productorio)

#si es opcion 5 :
    elif opcion == 5:
        if matriz is None:
            print ("Se debe de hacer una matriz")
        else:
            cantidad_filas = len(matriz)
            cantidad_columnas= len(matriz)
            for i in range(cantidad_filas):
                transpuesta= []
                for j in range(cantidad_columnas):
                    transpuesta.append(matriz [j][i])
                print ("\n La transpuesta es: ",transpuesta)

#si es opcion 6 :
    elif opcion == 6:
        print ("Saliendo . . .")
        break 

    #tenia otro repositorio no vinculado con github por que le cambie el nombre,la clase que viene te meustro