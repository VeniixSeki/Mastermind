import os
import readchar
import random


def main():
    POS_X = 0
    POS_Y = 1

    NUM_OF_MAP_OBJECTS = 11

    obstacle_definition = """\
##########################
######                ####
#######               ####
######                ####
##############      ######
##############      ######
##############      ######
##############      ######
######                ####
#######               ####
######                ####
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

    my_position = [10, 2]
    tail_length = 0 
    tail = []
    map_objects = []

    #create a obstacle map
    obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
    
    MAP_WIDTH = len(obstacle_definition[0])
    MAP_HEIGHT = len(obstacle_definition)

    end_game = False

    while not end_game:
        os.system("cls")

        #Generate random objects
        while len(map_objects) < NUM_OF_MAP_OBJECTS:
            new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

            if new_position not in map_objects and new_position != my_position:
                map_objects.append(new_position)
            
        #Draw map
        print("+" + "-" * MAP_WIDTH * 2 + "+")

        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")

            for coordinate_x in range(MAP_WIDTH):

                char_to_draw = " "
                object_in_cell = None
                tail_in_cell = None

                for map_object in map_objects:
                    if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                        char_to_draw = "*"
                        object_in_cell = map_object
                
                for tail_piece in tail:
                    if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                        char_to_draw = "@"
                        tail_in_cell = tail_piece

                if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                    char_to_draw = "@"

                    if object_in_cell:
                        map_objects.remove(object_in_cell)
                        tail_length += 1
                    
                    if tail_in_cell:
                        print("You are death")
                        end_game = True

                if obstacle_definition[coordinate_y][coordinate_x] == "#":
                    char_to_draw = "#"
                
                print(" {}".format(char_to_draw), end="")
            print("|")

        print("+" + "-" * MAP_WIDTH * 2 + "+")

        #Ask user where he wants to move
        direction = readchar.readchar()
        print(direction)
        
        if direction == "w":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position[POS_Y] -= 1
            my_position[POS_Y] %= MAP_HEIGHT
        elif direction == "s":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position[POS_Y] += 1
            my_position[POS_Y] %= MAP_HEIGHT
        elif direction == "a":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position[POS_X] -= 1
            my_position[POS_X] %= MAP_WIDTH
        elif direction == "d":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position[POS_X] += 1
            my_position[POS_X] %= MAP_WIDTH
        elif direction == "q":
            end_game = True


if __name__=="__main__":
    main()