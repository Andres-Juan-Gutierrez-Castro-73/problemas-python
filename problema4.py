#DEFINIMOS UN ARREGLO QUE GUARDE LOS VALORES
arreglo_notas = []

#DEFINIMOS LA FUNCION QUE VA A HACER EL PROMEDIO
def promedio(array):
    promedio = (sum(array)) / len(array)

    print('El promedio de las 10 notas: ' + str(promedio))

#DEFINIMOS LA FUNCION QUE VA A PEDIR 10 VECES EL VALOR
def pedir_numero(arreglo_notas):
    for i in range(10):
        numero = int(input('Escribe el numero: \n'))
        arreglo_notas.append(numero)

    for i in range(5):
        suma += arreglo_notas[-1 * i]
        print(suma)
    
    #LLAMAMOS LA FUNCION ANTERIOR PARA HACER EL PROMEDIO CON LOS VALORES DEL ARREGLO
    #promedio(arreglo_notas)
    #print('La suma de las 5 u')

pedir_numero(arreglo_notas)
