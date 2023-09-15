from random import randint
import os

def main():

    rival_life = 130
    victini_life = 170

    rival_initial_life = rival_life
    victini_initial_life = victini_life

    LP_Bar = 10

    while rival_life > 0 and victini_life > 0:
        #the fight begins

        #rival's turn
        print("rival's turn")
        rival_attack = randint(1, 2)
        if rival_attack == 1:
            print("rival used Electro Ball")
            victini_life -= 10
        else:
            print("rival used Thunder Shock")
            victini_life -= 11

        if victini_life < 0:
            victini_life = 0

        rival_LP_porcentage = (round(rival_life/rival_initial_life*LP_Bar))
        rival_empty_porcentage = (LP_Bar-rival_LP_porcentage)
        victini_LP_porcentage = (round(victini_life/victini_initial_life*LP_Bar))
        victini_empty_porcentage = (LP_Bar-victini_LP_porcentage)
        print("\nrival LP = [{}{}] {}/{} \nVictini LP = [{}{}] {}/{}\n".format(rival_LP_porcentage*"#", rival_empty_porcentage*" ", rival_life, rival_initial_life, 
                                                                           victini_LP_porcentage*"#", victini_empty_porcentage*" ", victini_life, victini_initial_life))
        input("Enter for continue...\n\n")
        os.system ("cls")

        #Victini's turn
        print("Victini's turn")

        victini_attack = None
        while victini_attack not in ["A", "B", "C", "D"]:    
            victini_attack = input("\nWhat attack do you want to use?\n"
                                   "V-create [A]\nDouble-Edge [B]\nFlare Blitz [C]\nNo attack[D]\n")

        if victini_attack == "A":
            print("Victini used V-create")
            rival_life -= 19
        elif victini_attack == "B":
            print("Victini used Double-Edge")
            rival_life -= 15
        elif victini_attack == "C":
            print("Victini used Flare Blitz")
            rival_life -= 14
        else:
            print("Victini didn't attack")

        if rival_life < 0:
            rival_life = 0        
        rival_LP_porcentage = (round(rival_life/rival_initial_life*LP_Bar))
        rival_empty_porcentage = (LP_Bar-rival_LP_porcentage)
        victini_LP_porcentage = (round(victini_life/victini_initial_life*LP_Bar))
        victini_empty_porcentage = (LP_Bar-victini_LP_porcentage)
        print("\nrival LP = [{}{}] {}/{} \nVictini LP = [{}{}] {}/{}\n".format(rival_LP_porcentage*"#", rival_empty_porcentage*" ",rival_life,rival_initial_life, 
                                                                           victini_LP_porcentage*"#", victini_empty_porcentage*" ", victini_life,victini_initial_life))
        input("Enter for continue...\n\n")
        os.system ("cls")

    if rival_life > victini_life:
        print("rival Win")
    else:
        print("Victini Win")



if __name__=="__main__":
    main()