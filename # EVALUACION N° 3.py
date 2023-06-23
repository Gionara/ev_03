# EVALUACION N° 3 
# Giovanna espinosa


#IMPORTACION DE FUNCIONES
#import random

#DEFINICION DE  FUNCIONES

def menu ():
    print("\n\n\n---- MENU ----")
    print("[1]  Grabar.")
    print("[2]  Buscar.")
    print("[3]  Imprimir Certificados.")
    print("[4]  Salir.")

#MENU 1 GRABAR
def grabar(lista_vehiculos):
    vehiculo=[]
    tipo = input("Ingrese el tipo de vehiculo.\n >> ") 
    while True:
        try:
            patente = input("Ingrese el patente de vehiculo.\n >> ") 
            letras_patente = patente[:3]
            if len(patente) == 6 and letras_patente.isalpha():
                break
            else:
                print("Patente invalida")
        except:
            print("Patente invalida")
            continue
    marca          = input("Ingrese el marca de vehiculo.\n >> ") 
    while not(len(marca)>=2 and len (marca)<=15):
        marca= input("Ingrese correctamente la marca del vehiculo.")
    while True:
        try:
            precio = input("Ingrese el precio de vehiculo.\n >> ") 
            if  int(precio) >= 5000000:
                break
        except:
            continue
    while True:
        try:
            multa = input("Ingrese el multa de vehiculo.\n >> ") 
            if int(multa) >= 0:
                break
        except:
            print("Ingrese correctamente el valor.")
            continue
    fecha_multa    = input("Ingrese el fecha consulta de las multas de vehiculo. (dd/mm/aaaa)\n >> ")
    while len(fecha_multa) !=10:
           fecha_multa    = input("Ingrese el fecha consulta de las multas de vehiculo. (dd/mm/aaaa)\n >> ")
    fecha_registro = input("Ingrese el fecha de registro. (dd/mm/aaaa)\n >> ") 
    while  len(fecha_registro) !=10:
            fecha_multa    = input("Ingrese el fecha consulta de las multas de vehiculo. (dd/mm/aaaa)\n >> ")
    nombre_dueño   = input("Ingrese el nombre del dueño.\n >> ") 
    vehiculo = [tipo,patente,marca,precio,multa,fecha_multa,fecha_registro,nombre_dueño]
    lista_vehiculos.append(vehiculo)
    
#MENU 2 BUSCAR
def buscar (lista_vehiculos):
    lista_patente=[]
    for vehiculos in lista_vehiculos:
        lista_patente.append(vehiculos[1])
    patente= input("Ingrese patente del vehiculo a consultar.\n >>  ")
    while not (patente in lista_patente):
        patente =input("Patente no esta en los registros.\n Ingrese patente del vehiculo a consultar.\n >>  ")


    for vehiculo in lista_vehiculos:
        if patente == vehiculo[1]:
            datos = vehiculo      
            print("\n\nPatente a consultar    : ",patente)
            print("Tipo de vehiculo        : ",datos[0])
            print("Marca del vehiculo      : ",datos[2])
            print("Precio del vehiculo     : $",datos[3])
            print("Multas del vehiculo     : $",datos[4])
            print("Fecha de consulta multa : ",datos[5])
            print("Fecha de registro       : ",datos[6])   
            print("Nombre del dueño        : ",datos[7])

# MENU 3 IMPRIMIR CERTIFICADOS
def imprimir_certificados (lista_vehiculos):
    patente= input("\nIngrese patente a consultar: ")
    for vehiculo in lista_vehiculos:
        if patente == vehiculo[1]:
            datos = vehiculo   
    opcion,valor = seleccion_certificado()
    if int(opcion) == 1 :
        print("\n\n CERTIFICADO DE EMISION DE CONTAMINANTE")
        print("\n Valor: $",valor)
        print(f" Patente a consultar    : {patente}")
        print(f"Nombre del dueño        : {datos[7]}\n\n")
        
    elif int(opcion) == 2  :
        print("\n\n CERTIFICADO DE ANOTACIONES VIGENTES")
        print("\n Valor: $",valor)
        print(f" Patente a consultar    : {patente}")
        print(f"Nombre del dueño        : {datos[7]}\n\n")
    else:
        print("\n\n CERTIFICADO DE MULTAS")
        print("\n Valor: $",valor)
        print(f" Patente a consultar    : {patente}")
        print(f"Nombre del dueño        : {datos[7]}\n\n")


def seleccion_certificado():
    print(" [1] Certificado de Emision de contaminantes")
    print(" [2] Certificado de Anotaciones vigentes")
    print(" [3] Certificado de Multas")
    while True:
        try:
            opcion= int(input("Ingrese opcion : "))
            if opcion >=1 and opcion <=3:
                #valor=random.ramdint(1500,3500)
                valor= input("Ingrese valor del certificado entre 1500 y 3500 :")
                while not (int(valor)>=1500 and int(valor)<=3500):
                    valor= input("Ingrese valor del certificado entre 1500 y 3500 :")
                return opcion, valor
                break
            
        except:
            print("Ingrese una opcion valida.")
            continue


# MENU 4 SALIDA
def salir ():
    print(" Usted esta saliendo del programa.")
    print(" Muchas gracias.")
    print(" Giovanna Espinosa version 1.0")
    
    
# PROCESAMIENTO
lista_vehiculos = []
while True:
    try:
        menu()
        print(lista_vehiculos)
        opcion= input("\n\n Ingrese opcion : ")
        if   opcion == "1":
            grabar(lista_vehiculos)
        elif opcion == "2":
            buscar(lista_vehiculos)
        elif opcion == "3":
            imprimir_certificados(lista_vehiculos)
        elif opcion == "4":
            salir()
            break
    except:
        print("Opcion no valida, ingrese nuevamente")
        continue