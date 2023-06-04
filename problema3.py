#DEFINIMOS LA FUNCION QUE VA A HACER EL PROMEDIO Y VA A MOSTRAR LAS CONDICIONES
def promedio(num1, num2, num3):
    #CREAMOS LA FUNCION PROMEDIO
    promedio = (num1 + num2 + num3) / 3
    if(promedio >= 7):
        print('Gano con nota de: ' + str(promedio))
    elif(promedio >= 4):
        print('Nivel medio con nota de: ' + str(promedio))
    elif(promedio < 4):
        print('Pierde con nota de: ' + str(promedio))
    elif(num1 >= 10 and num2 >=10 and num3>=10):
        print('Alguna de las notas que escribiste sobrepasa el maximo.')

#PEDIMOS LOS VALORES EN UN INPUT
numero1 = int(input('Escribe la primer nota: \n'))
numero2 = int(input('Escribe la segunda nota: \n'))
numero3 = int(input('Escribe la tercera nota: \n'))

#EJECUTAMOS LA FUNCION
promedio(numero1, numero2, numero3)