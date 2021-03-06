"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from collections import Counter
import csv
with open('data.csv', 'r', newline='') as data:
    data_reader=csv.reader(data, delimiter='\t')
    list_data=list(data_reader)

data=open('data.csv', 'r').readlines()
data=[i.replace('\n', '') for i in data]
data=[i.split('\t') for i in data]





def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    suma=0
    lenght=len(list_data)
    for i in range(lenght):
        suma+=int(list_data[i][1])
    return(suma)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista=[]
    length=len(list_data)
    for i in range(length):
        lista.append(list_data[i][0])
    return(sorted(Counter(lista).most_common(len(lista))))


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    dic=dict()
    for i in data:
        if i[0] not in list(dic.keys()):
            dic[i[0]]=int(i[1])
        elif i[0] in list(dic.keys()):
            dic[i[0]]+=int(i[1])
    return sorted(list(dic.items()))


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    lista=[]
    length=len(list_data)
    for i in range(length):
        lista.append(list_data[i][2][5:7])
    return(sorted(Counter(lista).most_common(len(lista))))


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dic=dict()
    for i in data:
        if i[0] not in list(dic.keys()):
            dic[i[0]]=[int(i[1])]
        elif i[0] in list(dic.keys()):
            dic[i[0]].append(int(i[1]))
    
    result=[(j,max(dic[j]),min(dic[j])) for j in dic.keys()]
    result.sort(key = lambda x: x[0], reverse=False)
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista=[]
    dic=dict()
    length=len(data)
    for i in range(length):
        lista.extend(data[i][4].split(','))
        for j in lista:
            clave=j.split(':')[0]
            valor=j.split(':')[1]
            if clave not in list(dic.keys()):
                dic[clave]=[int(valor)]
            elif clave in list(dic.keys()):
                dic[clave].append(int(valor))
    result=[(k,min(dic[k]),max(dic[k])) for k in dic.keys()]
    result.sort(key = lambda x: x[0], reverse=False)
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    dic=dict()
    for i in data:
        if int(i[1]) not in dic.keys():
            dic[int(i[1])]=[str(i[0])]
        else:
            dic[int(i[1])].append(str(i[0]))
        
    result = list(dic.items())
    result.sort()
    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    dic=dict()
    for i in data:
        if int(i[1]) not in dic.keys():
            dic[int(i[1])]=[i[0]]
        else:
            dic[int(i[1])].append(i[0])
        
    result = sorted(list(dic.items()))
    result = [(j[0], sorted(set(j[1]))) for j in result]
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista=[]
    lista_0=[]
    dic=dict()
    for i in range(len(data)):
        lista.extend(data[i][4].split(','))
    for j in range(len(lista)):
        lista_0.append(lista[j][0:3])
        
    return dict(sorted(Counter(lista_0).most_common(len(lista_0))))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista = []
    for i in data:
        lista.append((i[0], len(i[3].split(',')),len(i[4].split(','))))

    return lista

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    
    diccionario = {}
    for i in data:
        for a in i[3].split(','):
            if a in diccionario.keys():
               diccionario[a] = diccionario[a] + int(i[1])
            else:
                diccionario[a] = int(i[1])
    
    resultado = list(diccionario.items())

    return dict(sorted(resultado, key=lambda tup: tup[0]))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    diccionario = {}
    for i in data:
        c = i[4].split(',')
        if i[0] in diccionario.keys():
            diccionario[i[0]] = diccionario[i[0]] + sum([int(e.split(':')[1]) for e in c])
        else:
            diccionario[i[0]] = sum([int(e.split(':')[1]) for e in c])
    resultado = list(diccionario.items())
    resultado = dict(sorted(resultado, key=lambda tup: tup[0]))
    return resultado
