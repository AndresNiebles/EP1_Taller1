# Cálculo de la potencia eléctrica

# Solicitud de datos 
voltaje = float(input("Ingrese el voltaje (V): "))
corriente = float(input("Ingrese la corriente (A): "))

# Calculo de potencia
potencia = voltaje * corriente


print(f"\nLa potencia consumida es: {potencia:.2f} W")
