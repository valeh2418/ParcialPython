import random

gestores = []

materiales = ["PET","CARTON","VIDRIO","METAL"]

datos_recoleccion = {m: [] for m in materiales}

def crear_gestores():

    print("\nCREAR GESTORES")

    for i in range(5):

        nuevo = {
            "id": i+1,
            "nombre": input("Nombre: "),
            "correo": input("Correo: "),
            "clave": input("Clave: "),
            "empresa": input("Empresa: "),
            "rol": input("Rol: ")
        }

        gestores.append(nuevo)


def autenticar():

    print("\nLOGIN")

    for intento in range(3):

        c = input("Correo: ")
        p = input("Clave: ")

        for g in gestores:
            if g["correo"] == c and g["clave"] == p:
                print("Acceso OK")
                return True

        print("Error")

    return False


def generar_mediciones():

    for m in materiales:
        datos_recoleccion[m] = [random.randint(1,20) for _ in range(20)]


def analizar():

    total_global = 0

    for material in datos_recoleccion:

        lista = datos_recoleccion[material]

        prom = sum(lista)/len(lista)

        total_global += prom

        if prom < 8:
            estado = "Bajo"
        elif prom <= 15:
            estado = "Estable"
        else:
            estado = "Alto"

        print(material,"=>",round(prom,2),"kg |",estado)

    prom_global = total_global/len(materiales)

    if prom_global < 10:
        e_global = "Alerta"
    elif prom_global < 15:
        e_global = "Operacion normal"
    else:
        e_global = "Jornada sobresaliente"

    print("\nGLOBAL:",round(prom_global,2),"->",e_global)


crear_gestores()

if autenticar():

    generar_mediciones()

    print("\nRECOLECCIONES:")
    for m,v in datos_recoleccion.items():
        print(m,v)

    print("\nRESULTADOS:")
    analizar()

else:
    print("Sistema bloqueado")
