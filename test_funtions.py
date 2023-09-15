import random 

def guess_the_number():
    a = random.randint(1, 100)
    b = int(input("Adivina el numero (del 1 al 100) = "))
    
    while a != b:
        b = int(input("Ese no es, intenta de nuevo = "))

    print("felicidades")

def fake_upper(arg):
    print(arg.swapcase(), '\n')

def es_impar(num):
    if num%2 != 0:
        var = True
    else:
        var = False
    return var

def sum_the_list(the_list):
    total = 0

    for i in the_list:
        total += i

    return total

def potencia(numero, base=2):
    resultado = numero
    for a in range(1, base):
        resultado *= numero
    return resultado

def fibonacciR(n):
    if n<= 1:
        return 1
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)

def medir_largos(iterable, *args):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        return largos
    return len(iterable)

def larger_string(*args):
    strings = [args]
    temp_num = -1

    for i in args:
        if len(i) > temp_num:
            temp_num = len(i)
            larger = i
    
    return larger

def main():
    """
    print(medir_largos("hola"))
    print(medir_largos("hola", "como", "estas"))

    for f in range(8):
        print(fibonacciR(f))

    print(potencia(4))
    print(potencia(4, 5))

    print(larger_string("hola", "como", "estas"))

    print(sum_the_list([1,2,3,4,5]))

    print(es_impar(3))
    print(es_impar(24))

    fake_upper("holiwis kiwis")
    """
    guess_the_number()
    
if __name__ == "__main__":
    main()