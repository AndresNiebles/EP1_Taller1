while True:
    respuesta = input("¿Desea continuar Si/No?: ").strip().lower() #.strip().lower() limpia espacios y convierte a minúsculas para evitar errores.
    if respuesta == "no":
        print("Programa finalizado.")
        break
    elif respuesta == "si":
        print("Continuando...")
    else:
        print("Respuesta no válida. Por favor, escriba Si o No.")
