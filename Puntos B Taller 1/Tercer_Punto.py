import math  # Para usar π

# Calculos de Volumenes
def volumen_prisma(base, altura):
    return base * altura

def volumen_piramide(base, altura):
    return (base * altura) / 3

def volumen_cono_truncado(r1, r2, altura):
    return (1/3) * math.pi * altura * (r1**2 + r2**2 + (r1 * r2))

def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

# Menú para selección de figura
print("Cálculo de volúmenes:")
print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")

opcion = int(input("Seleccione el Sólido: "))


if opcion == 1:
    base = float(input("Ingrese el área de la base del prisma: "))
    altura = float(input("Ingrese la altura del prisma: "))
    volumen = volumen_prisma(base, altura)
    print(f"El volumen del prisma es: {volumen:.3f}")

elif opcion == 2:
    base = float(input("Ingrese el área de la base de la pirámide: "))
    altura = float(input("Ingrese la altura de la pirámide: "))
    volumen = volumen_piramide(base, altura)
    print(f"El volumen de la pirámide es: {volumen:.3f} ")

elif opcion == 3:
    r1 = float(input("Ingrese el radio mayor del cono truncado: "))
    r2 = float(input("Ingrese el radio menor del cono truncado: "))
    altura = float(input("Ingrese la altura del cono truncado: "))
    volumen = volumen_cono_truncado(r1, r2, altura)
    print(f"El volumen del cono truncado es: {volumen:.3f}")

elif opcion == 4:
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    volumen = volumen_cilindro(radio, altura)
    print(f"El volumen del cilindro es: {volumen:.3f}")

else:
    print("Opción no válida.")
