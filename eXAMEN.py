#Examen  Montserrat Valdovinos Ochoa
import json
def obtener_municipio():
    municipios=[]
    try:
        archivo=open("CPDescarga.txt",mode="r")
        if archivo.readable():
            for linea in archivo.read().split("\n"):
                if len(linea)>0:
                    codigo = linea.split("|")[0]
                    tipo = linea.split("|")[10]
                    zona=linea.split("|")[12]
                    municipios.append((codigo,tipo,zona))
                archivo.close()
    except FileNotFoundError as ex:
        print("No se puede acceder al archivo")
    return municipios

print(obtener_municipio())
def regresa_nombre():
    nombres = []
    try:
        archivo = open("CPDescarga.txt", mode="r")
        if archivo.readable():
            for linea in archivo.read().split("\n"):
                if len(linea) > 0:
                    codigo = linea.split("|")[0]
                    nombre = linea.split("|")[1]
                    nombres.append((codigo, nombre))
                archivo.close()
    except FileNotFoundError as ex:
        print("No se puede acceder al archivo")
    return nombres
print(regresa_nombre())

def municipio(*args):
    municipios= obtener_municipio()
    nombres=regresa_nombre()
    datos=[]
    try:
        if len(args)>0:
            for nombre in args:
                municipio=[]
                datos_mun={}
                for i in range(0,len(municipios)):
                    if municipios[i][0]==args:
                        for j in range(0,len(nombres)):
                            if nombres[j][0]==nombre:
                                municipio.append(nombres[j][1])
                                datos_mun={"Codigo": municipios[i][0],"Tipo as":municipios[i][1],"Zona":municipios[i][2]}
                                break
                datos.append(datos_mun)
        # for mun in municipios:
        #     for nom in nombres:
        #         if municipios[0]==nombres[0]:
        #             datos_mun={"Municipio":nombres[1],"Codigo": mun[0],"Asentamiento":mun[2], "Zona": mun[3]}
        #             print(datos_mun)
        #             datos.appened(datos_mun)
    except ValueError:
        print("Introduce un municipio valido")
    return datos
print(municipio("Santa Maria"))

def regresa_estado():
    codigos = []
    try:
        archivo = open("CPDescarga.txt", mode="r")
        if archivo.readable():
            for linea in archivo.read().split("\n"):
                if len(linea) > 0:
                    codigo = linea.split("|")[0]
                    Estado = linea.split("|")[4]
                    codigos.append((codigo, Estado))
                archivo.close()
    except FileNotFoundError as ex:
        print("No se puede acceder al archivo")
    return codigos
print(regresa_estado())