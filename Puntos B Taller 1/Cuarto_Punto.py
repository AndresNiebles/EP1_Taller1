def info_robot(tipo_robot):
    if tipo_robot == 1:
        return "Robot Cilíndrico", "Posee 3 articulaciones: 2 prismáticas y 1 rotacional"
    elif tipo_robot == 2:
        return "Robot Cartesiano", "Posee 3 articulaciones prismáticas (movimiento lineal en X, Y y Z)"
    elif tipo_robot == 3:
        return "Robot Esférico", "Posee 3 articulaciones: 2 rotacionales y 1 prismática"
    else:
        return None, "Opción no válida"

# Menú para el usuario
print("Seleccione el tipo de robot:")
print("1. Robot Cilíndrico")
print("2. Robot Cartesiano")
print("3. Robot Esférico")

opcion = int(input("¿Cuál Robot desea conocer? "))

# Obtener la información del robot
nombre, descripcion = info_robot(opcion)

if nombre:
    print(f"\nTipo de Robot: {nombre}")
    print(f"Características: {descripcion}")
else:
    print(descripcion)
