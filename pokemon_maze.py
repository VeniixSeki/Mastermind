import os
import readchar
import random

def fight(num):
    if num == 1:
        rival = "Pikachu"
        rival_life = 130
        attack1 = "rival used Electro Ball"
        damage_attack1 = 10
        attack2 = "rival used Thunder Shock"
        damage_attack2 = 11
    elif num == 2:
        rival = "Electrode"
        rival_life = 150
        attack1 = "rival used Swift"
        damage_attack1 = 13
        attack2 = "rival used Discharge"
        damage_attack2 = 15
    elif num == 3:
        rival = "Zapdos"
        rival_life = 170
        attack1 = "rival used Thunder"
        damage_attack1 = 12
        attack2 = "rival used Zap Cannon"
        damage_attack2 = 19
    
    victini_life = 170

    rival_initial_life = rival_life
    victini_initial_life = victini_life

    LP_Bar = 10
    os.system("cls")
    while rival_life > 0 and victini_life > 0:
        #the fight begins

        #rival's turn
        print("rival's turn")
        rival_attack = random.randint(1, 2)
        if rival_attack == 1:
            print(attack1)
            victini_life -= damage_attack1
        else:
            print(attack2)
            victini_life -= damage_attack2

        if victini_life < 0:
            victini_life = 0

        rival_LP_porcentage = (round(rival_life/rival_initial_life*LP_Bar))
        rival_empty_porcentage = (LP_Bar-rival_LP_porcentage)
        victini_LP_porcentage = (round(victini_life/victini_initial_life*LP_Bar))
        victini_empty_porcentage = (LP_Bar-victini_LP_porcentage)
        print("\n{} LP = [{}{}] {}/{} \nVictini LP = [{}{}] {}/{}\n".format(rival, rival_LP_porcentage*"#", rival_empty_porcentage*" ", rival_life, rival_initial_life, 
                                                                        victini_LP_porcentage*"#", victini_empty_porcentage*" ", victini_life, victini_initial_life))
        input("Enter for continue...\n\n")
        os.system ("cls")

        #Victini's turn
        print("Victini's turn")

        victini_attack = None
        while victini_attack not in ["A", "B", "C", "D"]:    
            victini_attack = input("\nWhat attack do you want to use?\n"
                                "V-create [A]\nDouble-Edge [B]\nFlare Blitz [C]\nNo attack[D]\n")
            victini_attack = victini_attack.upper()

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
        print("\n{} LP = [{}{}] {}/{} \nVictini LP = [{}{}] {}/{}\n".format(rival, rival_LP_porcentage*"#", rival_empty_porcentage*" ",rival_life,rival_initial_life, 
                                                                        victini_LP_porcentage*"#", victini_empty_porcentage*" ", victini_life,victini_initial_life))
        input("Enter for continue...\n\n")
        os.system ("cls")

    if rival_life > victini_life:
        print("Rival Win")
        victories = 0
    else:
        print("Victini Win")
        victories = 1
    
    input("\nEnter for continue...\n\n")
    os.system ("cls")
    return victories

def main():
    print("Los controles de movimiento son WASD y Q para salir")
    input("Enter for continue...")
    os.system ("cls")

    POS_X = 0
    POS_Y = 1

    obstacle_definition = """\
##########################
######                 ###
#######                ###
######                 ###
##############      ######
##############      ######
##############      ######
##############      ######
######                 ###
#######                ###
######                 ###
##############      ######
##############      ######
##############      ######
##############      ######
#                        #
#                        #
#                        #
#                        #
#                        #
##########################\
"""
    
    win_condition = 0
    my_position = [10, 2]
    obstacles = []
    map_objects = [[21, 2], [9, 9], [3, 17]]
    one = True
    two = True

    #create a obstacle map
    obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
    
    MAP_WIDTH = len(obstacle_definition[0])
    MAP_HEIGHT = len(obstacle_definition)

    end_game = False

    while not end_game:
        os.system("cls")
            
        #Draw map
        print("+" + "-" * MAP_WIDTH * 2 + "+")

        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")

            for coordinate_x in range(MAP_WIDTH):

                char_to_draw = " "
                object_in_cell = None
                obstacle_in_cell = None

                for map_object in map_objects:
                    if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                        char_to_draw = "*"
                        object_in_cell = map_object

                for hashtag in obstacles:
                        if hashtag[POS_X] == coordinate_x and hashtag[POS_Y] == coordinate_y:
                            obstacle_in_cell = hashtag

                if obstacle_definition[coordinate_y][coordinate_x] == "#":
                    char_to_draw = "#"
                    while one and two:
                        obstacles.append([coordinate_x, coordinate_y])
                        one = False
                    one = True

                if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                    char_to_draw = "@"

                    if object_in_cell:
                        if coordinate_x == 3 and coordinate_y == 17:
                            num = 3
                        elif coordinate_x == 9 and coordinate_y == 9:
                            num = 2
                        elif coordinate_x == 21 and coordinate_y == 2:
                            num = 1

                        win_condition += fight(num)
                        map_objects.remove(object_in_cell)

                    if obstacle_in_cell:
                        end_game = True
       
                print(" {}".format(char_to_draw), end="")
            print("|")

        print("+" + "-" * MAP_WIDTH * 2 + "+")

        while one:
            one = False
            two = False

        #Ask user where he wants to move
        direction = readchar.readchar()
        
        if direction.upper() == "W":
            my_position[POS_Y] -= 1
            my_position[POS_Y] %= MAP_HEIGHT
        elif direction.upper() == "S":
            my_position[POS_Y] += 1
            my_position[POS_Y] %= MAP_HEIGHT
        elif direction.upper() == "A":
            my_position[POS_X] -= 1
            my_position[POS_X] %= MAP_WIDTH
        elif direction.upper() == "D":
            my_position[POS_X] += 1
            my_position[POS_X] %= MAP_WIDTH
        elif direction.upper() == "Q":
            end_game = True

    print("\n--GAME OVER--")
    if win_condition == 3:
        print("\nYou win")
    else:
        print("\nYou lose")

    


if __name__=="__main__":
    main()