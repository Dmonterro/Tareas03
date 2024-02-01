def convertirM(kil):
    millas= 0.621371
    return kil * millas
try:
    print("Biengvenido a la convercion de Km a Millas")
    kil = float(input("Ingrese el número de kilometros a convertir: "))
    kil = float(kil)
    millas=convertirM(kil)
    resultado = "{:.3f}".format(millas)
    Total=(kil*0.621371)
    print("Las millas son: " + str(Total))

except ValueError:
    print("Error en convercion: Intenta nuevamente")