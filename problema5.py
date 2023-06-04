#DEFINIMOS LO ARREGLOS QUE VAN A GUARDAR LOS MULTIMPLOS
arreglo_principal = []

#DEFINIMOS LA FUNCION QUE VA A GUARDAR LOS NUMEROS QUE SON MULTIPLOS DE 3 Y 5
def multiplos_3_5(arreglo):
    #CREAMOS EL ARREGLO DE MULTIPLO DE 3 y 5
    arreglo3 = []
    arreglo5 = []

    #RECORREMOS EL ARREGLO 10 VECES
    for i in range(10):
        #AGREGAMOS LOS VALORES AL ARREGLO PRINCIPAL
        numero = int(input('Escribe el numero: \n'))
        arreglo.append(numero)
        #RECORREMOS EL ARREGLO Y DIVIDIMOS
        if arreglo[i] % 3 == 0:
            arreglo3.append(arreglo[i])
        elif arreglo[i] % 5 == 0:
            arreglo5.append(arreglo[i])
    
    #RETORNAMOS LOS DATOS
    print('Los multiplos de 3 son:\n' + str(arreglo3))
    print('Los multiplos de 5 son:\n' + str(arreglo5))

#IMPLEMENTAMOS LA FUNCION
multiplos_3_5(arreglo_principal)