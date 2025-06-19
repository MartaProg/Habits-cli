from datetime import datetime
import json
from collections import defaultdict
import os
RUTA_ARCHIVO = "data/habitos.json"

habitos = {}


def mostrar_menu(): 
    print("""
          Habits+ - Seguimiento de habitos saludables
          1: Añadir nuevo habito 
          2: Ver habitos existentes
          3: Ver habitos por categoría
          4: Borrar habito
          5: Salir
          """)
    



def cargar_habitos(): 
    global habitos
    try:
        
        with open(RUTA_ARCHIVO,"r",encoding="utf-8")as archivo: 
            datos = json.load(archivo)
            habitos.update(datos)
    except json.JSONDecodeError:
                print("El archivo JSON está dañado o vacío.")
    except FileNotFoundError:
        print("El archivo 'habitos.json' no existe todavía. Se creará cuando añadas hábitos.")
        
cargar_habitos()

def añadir_habito(): 
    nuevo_habito = input("Introduce el nuevo hábito que deseas añadir: ").lower()
    categoria = input("Introduce la categoría del habito.").lower()
    while categoria.strip() == "":
        categoria = input("Por favor, introduce una categoría válida: ").strip()

    existe = False
    for habito in habitos.get(categoria, []):
        if habito["nombre"].lower() == nuevo_habito:
                existe = True
                break

    if existe:
        print(" Ese hábito ya está en la lista.")
    else:
        fecha_actual = datetime.today().strftime("%Y-%m-%d")
        dic_habito = {"nombre": nuevo_habito, "fecha_creacion": fecha_actual}
        habitos.setdefault(categoria, []).append(dic_habito)

        print(" Hábito añadido con éxito.")
    guardar_habitos()

def ver_habitos(): 
    if not habitos: 
        print("No tienes habitos aún. Usa la opción 1 para añadir uno")
        return
    for categoria, lista_habitos in habitos.items():
        for habito in lista_habitos:
            nombre = habito["nombre"]
            fecha = habito["fecha_creacion"]
            
            print(f"{nombre} (añadido el  {fecha} -- Categoría: {categoria})")


    
def guardar_habitos():
    agrupados = defaultdict(list)
    for categoria, lista_habitos in habitos.items():
        agrupados[categoria].extend(lista_habitos)

    os.makedirs("data", exist_ok=True)
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(agrupados, archivo, indent=4, ensure_ascii=False)





def borrar_habito():
    categoria_borrar_habito = input("¿De qué categoría quieres borrar un hábito?: ").strip().lower()

    habito_borrar = input("Elija un habito a borrar: ").lower().strip()
    if categoria_borrar_habito not in habitos:
        print("Esa categoría no existe.")
        return
    else:    
        for habito in habitos[categoria_borrar_habito]: 
            if habito["nombre"].strip().lower() == habito_borrar: 
                habitos[categoria_borrar_habito].remove(habito)

                guardar_habitos()
                print(f"Habitdo eliminado: {habito}")
                return
                
    print("Habito no encontrado.")


def ver_habito_categoria():
    categoria_elegida = input("Introduce una categoría para ver sus hábitos: ").lower()

    if categoria_elegida in habitos:
        print(f"\nHábitos de la categoría: {categoria_elegida}")
        for habito in habitos[categoria_elegida]:
                nombre = habito["nombre"]
                fecha = habito["fecha_creacion"]
                print(f"- {nombre} (añadido el {fecha})")
    else:
        print(f"No se encontraron hábitos en la categoría '{categoria_elegida}'.")
