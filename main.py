############################################################################
# Title:calculator_cs30_part1
# Class: CS30
# Assignment: abandoned_school
# coder: Anqi Feng
# Version: 5
###########################################################################
"""This program will bring the user into a game name Abandoned school
inside the game, the user will self-chossing their next action as a
scanvengers. and they need to collect the missing knowledge as much 
as they can.
"""
###########################################################################
#Library Import
from tabulate import tabulate
import map as m
import room as r
import item as i
# DATABASE---------------------------------------------------



main1 = True
# Functions ------------------------------------------------


def main_menu():
    """This function will ask the user input of choosing action
    and if they want to quit or not, this is the main menu
    """
    global main1
    print(
        "Welcom, scavenger, You are now in a school name Rechimons High School."
    )
    print(
        "Your mission is:\n1:Find the way to get out\n2:Find the missing knowledge"
    )
    print("Enter 1: For choosing an action\n")
    print("Enter 2: For quit\n")
    m_des = True
    while m_des:
        try:
            playerInput = int(input("Please make your first choice："))
        except ValueError:
            print("Please enter in number form, scavenger!")
        else:
            if playerInput == 1:
                while main1:
                    player_action()
                m_des = False
            elif playerInput == 2:
                m_des = False
            else:
                print("Wrong input number~")
        finally:
            print("Keep going Scavengers!")


def player_movement():
    """This function will ask user input the direction they want 
    to go, and it will limit the map boundaries, also it will 
    demonstrate the discription of current environment.
    """
    global main1
    print(
        "\nChoose the direction from following list\nEnter 'quit' if you want to quit"
    )
    print(m.direction)
    wrongInput = True
    while wrongInput:
        try:
            movement = input("where do you want to go?")
        except ValueError:
            print("Please enter in write form Scavanger.")
        else:
            if movement.lower() == "north":
                if m.player_pos["row"] == 0:
                    print("You can't go North!")
                else:
                    m.player_pos["row"] = m.player_pos["row"] - 1
                    wrongInput = False
            elif movement.lower() == "south":
                if m.player_pos["row"] == m.map_height - 1:
                    print("You can't go South!")
                else:
                    m.player_pos["row"] = m.player_pos["row"] + 1
                    wrongInput = False
            elif movement.lower() == "east":
                if m.player_pos["col"] == m.map_width - 1:
                    print("You can't go East!")
                else:
                    m.player_pos["col"] = m.player_pos["col"] + 1
                    wrongInput = False
            elif movement.lower() == "west":
                if m.player_pos["col"] == 0:
                    print("You can't go West!")
                else:
                    m.player_pos["col"] = m.player_pos["col"] - 1
                    wrongInput = False
            elif movement.lower() == "quit":
                main1 = False
                wrongInput = False
            else:
                print(
                    "Wrong input~ please make sure enter the opition exist in the menu."
                )
        finally:
            print("Never stop your adventure Scavanger!")
        


def player_action():
    """This function define player's action when player input 
    number 1 in the main menue function. When user input one 
    this function allow user choose direction they want to go
    and when user input 2 the function will explore current
    enviromment
    """
    global main1
    try:
        current_pos = m.map[m.player_pos["row"]][m.player_pos["col"]]
        print("\nScavengers you are now in: " + current_pos)
        room_info = r.maping_sch[m.map[m.player_pos["row"]][
            m.player_pos["col"]]]["description"]
        print("\n" + room_info[0] + "\n")
        print("Choose what you want to do from following list\nEnter 'quit'" +
              " if you want to quit")
        print(m.move)
        action = input("What do you want to do? ")
    except ValueError:
        print("Please enter in correct form Scavenger!")
    else:
        if action.lower() == m.move[0]:
            with open('map.txt', 'r') as file:
              print(file.read())
            player_movement()
        elif action.lower() == m.move[1]:
            i.function(r.maping_sch[m.map[m.player_pos["row"]][
                      m.player_pos["col"]]]["tool"][0])
            print("\nScavengers, now you have:\n")
            print(i.player_tools)
        elif action.lower() == "quit":
            main1 = False
        else:
            print("Wrong input!")
    finally:
        print("")


# Main--------------------------------------------------
main_menu()