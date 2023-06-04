#DEFINIMOS LA FUNCION QUE DIGA SI EL NUMERO ES MAYOR O MENOR

def numero_mayor(num1, num2):
    if(num1>num2):
        suma = num1 + num2
        print('El numero ' + str(num1) + ' es mayor')
        print('El valor de la suma es: ' + str(suma))
    elif (num1 == num2):
        print("Los numeros son iguales")
    else:
        resta = num1 - num2
        print('El numero ' + str(num2) + ' es mayor')
        print('El valor de la resta es: ' + str(resta))

#RECIBIMOS LO VALORES

numero1 = int(input("Escribe el primer numero: \n"))
numero2 = int(input("Escribe el segundo numero: \n"))

#IMPLMENTAMOS LA FUNCION
numero_mayor(numero1, numero2)