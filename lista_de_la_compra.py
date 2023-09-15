import os

def main():
    lista = []
    while True:
        os.system("cls")
        x = input("Programa lista de la compra\n\nQue desea comprar? ([Q] para salir) > ")
        if x == "Q":
            break
        elif (x in lista) == False:
            lista.append(x)
            y = input("Seguro que quiere añadir \"{}\" [S/N] > ".format(x))
            if y == "S":
                print("{} Añadido".format(x))

    print("La lista de la compra es:")
    print(lista)


if __name__=="__main__":
    main()