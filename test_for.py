


def main():
    """
    user_text = input("enter a phrase")
    spaces = 0
    periods = 0
    commas = 0

    for i in user_text:
        if i == " ":
            spaces += 1
        elif i == ".":
            periods += 1
        elif i == ",":
            commas += 1
    print(spaces, periods, commas)


    x = int(input("Numero: "))
    for i in range(1, 11):
        y = i*x
        print("{} x {} = {}".format(x, i, y))

    numbers = [1, 2, 3, 4, 5, 6]
    print("The min value of the list is: {}".format(min(numbers)))
    print("The max value of the list is: {}".format(max(numbers)))

    
    """
    numeros_introducidos = input("Introduzca los numeros separados por coma: ")#1,2,3,4,5
    numeros_de_ususario = [int(numero) for numero in numeros_introducidos.split(",")]

if __name__=="__main__":
    main()