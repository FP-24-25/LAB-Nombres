

import csv

from collections import namedtuple

FrecuenciaNombre = namedtuple('Registro', 'año,nombre,frecuencia,genero')



def leer_frecuencias_nombres():

    with open("C:/Users/simo bennaji/Documents/Ejercicio de laboratorio, Nombres/data/frecuencias_nombres.csv", "r", encoding="utf-8") as csvfile:
        leer = csv.DictReader(csvfile)

        registro = []

        for linea in leer:
            elregistro = FrecuenciaNombre(año=int(linea["Año"]) ,
                                        nombre=linea["Nombre"],
                                        frecuencia=int(linea["Frecuencia"]),
                                        genero=linea["Género"])
            registro.append(elregistro)           

    return registro



def filtrar_por_genero(genero):
    
    registrofiltrado = []
    nombres = leer_frecuencias_nombres()

    for elregistro in nombres:
        if elregistro.genero == genero:
            registrofiltrado.append(elregistro)

    return registrofiltrado
                                    


def calcular_nombres(genero):
    generolista = set()
    listafiltrada = filtrar_por_genero(genero)
    listanofiltrada = leer_frecuencias_nombres()
    lista = listanofiltrada if genero is None else listafiltrada
    for nom in lista:
        nombres=nom.nombre
        generolista.add(nombres)
    return generolista



def calcular_top_nombres_de_año(año, genero, límite=10):
    registro = leer_frecuencias_nombres()
    nuevo = []
    for nom in registro:
        if nom.año == int(año) and (nom.genero == genero or genero is None):
            nuevo.append((nom.nombre, nom.frecuencia))

    nuevo_ordenada = sorted(nuevo,key=lambda x: x[1], reverse=True)
    return nuevo_ordenada[:límite]



def calcular_nombres_ambos_generos():
    hombres = calcular_nombres("Hombre")
    mujeres = calcular_nombres("Mujer")
    commun = hombres.intersection(mujeres)
    return commun



def calcular_nombres_compuestos(genero):
    return {
        nom.nombre
        for nom in leer_frecuencias_nombres()
        if (nom.genero == genero or genero is None) and len(nom.nombre.split()) > 1
        
    }



def calcular_frecuencia_media_nombre_años(nombre, año_inicial, año_final):
    registro = leer_frecuencias_nombres()
    frecuencias = []
    for frec in registro:
        if frec.nombre == nombre and año_inicial <= frec.año < año_final:
            frecuencias.append(int(frec.frecuencia))
    
    if not frecuencias:
        return 0

    media = sum(frecuencias) / len(frecuencias)
    
    return media



def calcular_nombre_mas_frecuente_año_genero(año, genero):
    FILTRADAS = [ 
        nom
        for nom in leer_frecuencias_nombres() if nom.año == año and nom.genero == genero
    ]

    if not FILTRADAS:
        return None

    NMF = max(FILTRADAS, key= lambda x: x.frecuencia)
    return NMF.nombre
    


def calcular_año_mas_frecuencia_nombre(nombre):
    FILTRADA = [
        nom for nom in leer_frecuencias_nombres() if nom.nombre == nombre 
    ]

    if not FILTRADA:
        return None

    AMF = max(FILTRADA, key= lambda x: x.frecuencia)
    return AMF.año



def calcular_nombres_mas_frecuentes(genero, decada, n):
    from collections import defaultdict
    filtrada = [
        nom for nom in leer_frecuencias_nombres() if nom.genero == genero and decada <= nom.año < decada + 10
    ]

    diccio = defaultdict(int)
    for Y in filtrada:
        diccio[Y.nombre] += Y.frecuencia


    NMF = sorted(diccio.items(), key= lambda x: x[1], reverse= True)[:n]

    return [z[0] for z in NMF]



def calcular_año_frecuencia_por_nombre(genero):
    from collections import defaultdict
    filtrada = [
        nom for nom in leer_frecuencias_nombres() if nom.genero == genero
    ]
    diccionario = defaultdict(list)
    for Y in filtrada:
        diccionario[Y.nombre].append((Y.año, Y.frecuencia))

    output = f"- Frecuencias de nombres de género {genero}\n"
    for X, Z in diccionario.items():
        output += f"             -{X}-->{Z}\n"

    return output



def calcular_nombre_mas_frecuente_por_año(genero):
    lista = [
        nom for nom in leer_frecuencias_nombres() if nom.genero == genero
    ]

    diccio = {}
    for n in lista:
        if n.año not in diccio or n.frecuencia > diccio[n.año][1]:
            diccio[n.año] = (n.nombre, n.frecuencia)

    nmfa = [(a, b, c) for a, (b, c) in diccio.items()]
    nmfa.sort(key= lambda x: x[1])
    return nmfa


    
def calcular_frecuencia_por_año(nombre):
    dicc = {}
    for nom in leer_frecuencias_nombres():
        if nom.nombre == nombre:
            if nom.año in dicc:
                dicc[nom.año] += nom.frecuencia
            
            else:
                dicc[nom.año] = (nom.frecuencia)
    
    nmfa = sorted((año, frecuencia) for año, frecuencia in dicc.items())
    return nmfa



def mostrar_evolucion_por_año(nombre):
    import matplotlib.pyplot as plt
    datos = calcular_frecuencia_por_año(nombre)

    años = [año for año, _ in datos]
    frecuencias = [frecuencia for _, frecuencia in datos]
    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show()

    
def calcular_frecuencias_por_nombre():
    diccionario = {}
    for nom in leer_frecuencias_nombres():
        if nom.nombre in diccionario:
            diccionario[nom.nombre] += nom.frecuencia
        else:
            diccionario[nom.nombre] = nom.frecuencia

    return diccionario      



def mostrar_frecuencias_nombres(límite=10):
    import matplotlib.pyplot as plt
    dicc = calcular_frecuencias_por_nombre()
    data = sorted(dicc.items(), key= lambda x: x[1], reverse= True)[:límite]
    nombres = [nombre for nombre, _ in data]
    frecuencias = [frecuencia for _, frecuencia in data]
    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(límite))
    plt.show()




