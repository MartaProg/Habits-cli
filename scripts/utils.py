from datetime import datetime
import json


habitos = []


def mostrar_menu(): 
    print("""
          Habits+ - Seguimiento de habitos saludables
          1: Añadir nuevo habito 
          2: Ver habitos existentes
          3: Ver habitos por categoría
          4: Salir
          """)
    


def añadir_habito(): 
    nuevo_habito = input("Introduce el nuevo hábito que deseas añadir: ").lower()
    categoria = input("Introduce la categoría del habito.")
    while categoria.strip() == "":
        categoria = input("Por favor, introduce una categoría válida: ").strip()

    existe = False
    for habito in habitos:
        if habito["nombre"].lower() == nuevo_habito:
            existe = True
            break

    if existe:
        print(" Ese hábito ya está en la lista.")
    else:
        fecha_actual = datetime.today().strftime("%Y-%m-%d")
        dic_habito = {"nombre": nuevo_habito, "fecha_creacion": fecha_actual, "categoria": categoria}
        habitos.append(dic_habito)
        print(" Hábito añadido con éxito.")
    guardar_habitos()

def ver_habitos(): 
    if not habitos: 
        print("No tienes habitos aún. Usa la opción 1 para añadir uno")
    for habito in habitos:
        nombre = habito["nombre"]
        fecha = habito["fecha_creacion"]
        categoria = habito["categoria"]
        print(f"{nombre} (añadido el  {fecha} -- Categoría: {categoria})")

def guardar_habitos(): 
    with open("data/habitos.json","w")as archivo: 
        json.dump(habitos,archivo, indent=4, ensure_ascii=False)

def ver_habito_categoria():
    categoria_elegida = input("Introduce una categoría para ver sus hábitos: ").lower()
    encontrado = False

    for habito in habitos:
        if habito["categoria"].lower() == categoria_elegida:
            if not encontrado:
                print(f"\nHábitos de la categoría: {categoria_elegida}")
                encontrado = True
            nombre = habito["nombre"]
            fecha = habito["fecha_creacion"]
            print(f"- {nombre} (añadido el {fecha})")

    if not encontrado:
        print(f"No se encontraron hábitos en la categoría '{categoria_elegida}'.")