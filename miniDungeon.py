import random


def comprobation():
    while True:
        x = input()
        x = x.upper()
        if x == "A" or x == "B":
            break
        else:
            print("Invalid option, write again")
    return x


def main():
    number = random.randint(20, 100)
    cValue = number/2
    neko = 1
    ratItem = 0
    i=0


    print("You are charged with a murder you did not commit." 
          "\nTo avoid being executed the next day you decide to escape."
          " What are you going to do?\n\n")
    

    print("A Wait on the cell\nB Look into the room")
    question = comprobation()
    if question == "A":
        while i != 3:
            print("\n\nA Beg for forgivenes\nB Scream about your innocence")
            comprobation()
            print("I spend 1 hour")
            i += 1
        print("This didn't help at all")
    else:
        print("\n\nFound a rat and a flat file\nA Take the flat file\nB Talk to the rat")
        question = comprobation()
        if question == "A":
            print("\n\nA Cut the bars of the window\nB Cut the bars of the door")
            question = comprobation()
            if question == "A":
                print("\nYou hear steps, If you hear it {} meters from the cell advancing at 2 m/s, how much time (seconds) you have to cut the bars? V=D/T".format(number))
                while neko == 1:
                    x = input()
                    try:
                        float(x)
                        if float(x) == cValue:
                            print("You look out the window, see that there is no way to escape, the guard arrives")
                        else:
                            print("Wrong answer, the guard arrives")
                        neko = 0
                    except ValueError:
                        print("Invalid option, write again as number")
            else:
                print("\nYou hear steps, If you hear it {} meters from the cell advancing at 2 m/s, how much time (seconds) you have to cut the bars? V=D/T".format(number))
                while neko == 1:
                    x = input()
                    try:
                        float(x)
                        if float(x) == cValue:
                            print("\n\nA Run to the prison dining hall\nB Run to the front door")
                            question = comprobation()
                            if question == "A":
                                print("\n\nA Talk to the cook\nB Talk to the janitor")
                                question = comprobation()
                                if question == "A":
                                    print("\n\nA You exchange the flat file for cheese\nB You exchange the flat file for a knife")
                                    question = comprobation()
                                    if question == "A":
                                        ratItem = 1
                                    else:
                                        ratItem = 2
                                else:
                                    print("He scream for help, the guards discovers you")
                            else:
                                print("The guards discovers you")
                        else:
                            print("Wrong answer, the guard arrives")
                        neko = 0
                    except ValueError:
                        print("Invalid option, write again as number")

                
        else:
            print("The rat took the flat file and escape")
    

    if ratItem != 0:
        print("\n\nYou look the rat, the rat tolds you, if you give me cheese I teleport you.")
        if ratItem == 1:
            print("\nYou have it, you escape!\nYOU WIN!!!")
        elif ratItem == 2:
            print("\nYou don't have it\n--GAME OVER--")
    else:
        print("\n--GAME OVER--")
    

if __name__=="__main__":
    main()