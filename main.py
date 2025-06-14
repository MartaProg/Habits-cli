import scripts.utils as utils

def main():
        while True: 
            utils.mostrar_menu()
            opcion = input("Elige una opción (1-5): ")

            if opcion == "1":
                utils.añadir_habito()
            elif opcion == "2":
                utils.ver_habitos()
            elif opcion == "3":
                utils.ver_habito_categoria()

            elif opcion == "4":
                utils.borrar_habito()
            
            elif opcion == "5":
                print("Hasta luego.")
                break
            else:
                print("Opción no válida. Intenta otra vez.")
            
if __name__ == "__main__": 
    main()
