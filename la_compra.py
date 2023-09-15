

SALIDA = "SALIR"
ARCHIVO = "lista compra.txt"

items_del_supermercado = ["pollo", "maiz", "lechuga", "pan"]

def preguntar_producto_usuario():
    item_elegido = input("Introduce un producto[{} para salir] ".format(SALIDA))
    while item_elegido.lower() not in items_del_supermercado and item_elegido != SALIDA:
        print("El item elegido no esta en la lista")
        item_elegido = input("Introduce un producto[{} para salir] ".format(SALIDA))
    return item_elegido

def guardar_lista_a_disco(lista_compra):
    #w write, r read, a append
    #nombre_fichero = input("Como quieres que se llame el fichero? ")
    with open(ARCHIVO, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))

def guardar_item_en_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:
        print("El producto ya existe!")
    else:
        lista_compra.append(item_a_guardar)

def cargar_archivo():
    lista_compra = []
    if input("Quieres cargar la ultima lista de la compra? [S/N] ") == "S":
        try:
            with open(ARCHIVO, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("Archivo de la compra no encontrado!")
    return lista_compra

def mostrar_lista(lista_compra):
    print("\n".join(lista_compra))

def main():
    lista_compra = cargar_archivo()
    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        guardar_item_en_lista(lista_compra, input_usuario)
        mostrar_lista(lista_compra)      
        input_usuario = preguntar_producto_usuario()

    guardar_lista_a_disco(lista_compra)

if __name__=="__main__":
    main()