def selection(opt):
    pass

if __name__ == "__main__":
    opt: int = 0
    
    while(opt != 6):
        opt = int(input("""
                    Escoge una de las siguientes opciones:\n
                    1. Suma\n
                    2. Resta\n
                    3. Multiplicacion\n
                    4. Division\n
                    5. Potencia\n
                    6. Salir\n
                """))
        selection(opt)
