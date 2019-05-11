'''
Suponga que se tiene una lista de listas que se tiene diversas cantidades por persona.
La primera columna con números representa la cantidad en miles de colones que tienen en la cuenta del banco,
la segunda columna la cantidad en crédito en miles de colones y la tercer columna en miles de colones en deuda.
'''

hoja_calculo = {
    'carlos':  {'Debito' : '54.54', 'Credito' : '6.57', 'Deuda':'3.64'},
    'juan':  {'Debito' : '5.54', 'Credito' : '9.57', 'Deuda':'4.64'},
    'luis':  {'Debito' : '9.54', 'Credito' : '7.57', 'Deuda':'1.64'},
}


'''
Suponga que se dispone de una función que procesa la lista para obtener la transpuesta(cambiar las columnas por las filas)
'''

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

'''
b = transpuesta(hoja_calculo)
b #sea b la tabla resultante luego de aplicar transpuesta
'''


[['carlos', 'juan', 'luis'],
 [54.54, 5.54, 9.54],
 [6.57, 9.57, 7.57],
 [3.64, 4.64, 1.64]]


'''
Por otro lado, se puede aplicar matemática o cualquier otra operación a alguna fila en específico. Por ejemplo: dividir todos los números entre 10. Obteniendo:
'''

'''
b[1] = list(map(lambda x: x/10, b[1]))
b
'''

'''
[['carlos', 'juan', 'luis'],
 [5.454, 0.554, 0.954],
 [6.57, 9.57, 7.57],
 [3.64, 4.64, 1.64]]
'''

#1.Contruya un diccionario de funciones matematicas (utilizando funciones lambda) entre todos los números de la lista tales como:
#Promedio
#La suma
#La multiplicación

suma=lambda x,y:x+y
multiple=lambda x,y:x*y
average = lambda x, y: (x+y)/2

lista_matematica = {
    'suma' : suma,
    'multiplica' : multiple,
    'average' : average,
}

#Obtenga utilizando el diccionario de funciones:
#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en promedio todas las personas.
#2. La suma de todas las deudas
#3. la multiplicación de todos los crédito entre si

import statistics

hoja_calculo = {'': None, 'carlos': {'debito': 54.54,
                               'credito': 6.57,
                               'deuda': 3.64, },

           'juan': {'debito': 5.54,
                     'credito': 9.57,
                     'deuda': 4.64, },

            'luis': {'debito': 9.54,
                     'credito': 7.57,
                     'deuda': 1.64, }}

aveValue1 = statistics.mean(d['debito'] for d in hoja_calculo.values() if d)
sumValue2 = sum(d['deuda'] for d in hoja_calculo.values() if d)
#mulValue3 = multiple(d['credito'] for d in hoja_calculo.values() if d)

#meter lambda suma y average

print(aveValue1)
print(sumValue2)
#print(mulValue3)

pass
