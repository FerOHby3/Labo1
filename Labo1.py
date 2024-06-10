print("Convertidor de Temperaturas\n ")
print("1. Covertir de Celsius a Fahreneit ")
print("2. Convertir de Fahreneit a Celsius ")
print("3. Cerrar el programa\n")

opcion=""

while opcion!="3":
    opcion=input("Ingrese la Opcion deseada ")
    
    if opcion=="1":
        base=input("Ingrese la Caantidad de Celsius que desea convertir a Fahreneit (Entre -273.15 a 6,000C°): ")
        baseflo=float(base)
        if baseflo>= -273.15 and baseflo<6001: #and base.isdigit():
            resultado=(baseflo*9/5) + 32
            print("El valor en Fahrenheit es igual a: "+"{:.2f}".format(resultado)+"F°\n")
        else:
            print("Ingrese un valor numerico entre -273.15 y 6,000\n")
            opcion=""
    
    if opcion=="2":
        base=input("Ingrese la Caantidad de Fahreneit que desea convertir a Celsius (Entre -459.67 a 10,832F°): ")
        baseflo=float(base)
        if baseflo>= -459.67 and baseflo<10833: #and base.isdigit():
            resultado=(baseflo-32)*5/9
            print("El valor en Fahrenheit es igual a: "+"{:.2f}".format(resultado)+"C°\n")
        else:
            print("Ingrese un valor numerico entre -459.67 y 10,832\n")
            opcion=""
    
    if opcion=="3":
        print("Gracias por usar el programa, tenga buen dia")
    
    if opcion!="" and opcion!="1" and opcion!="2" and opcion!="3":
        print("Ingrese una Opcion Valida\n")