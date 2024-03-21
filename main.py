#############################################################
# Title:calculator_cs30_part1
# Class: CS30
# Assignment: abandoned_school
# coder: Anqi Feng
# Version: 4
###########################################################
"""This program will bring the user into a game name Abandoned school
inside the game, the user will self-chossing their next action as a
scanvengers. and they need to collect the missing knowledge as much 
as they can.
"""
###########################################################
# DATABASE---------------------------------------------------
maping_sch = {
    "chemistry_lab":{
        "description":["This is the starting point. The lab is" 
                       + "brightly lit with white walls and metal countertops." 
                       + " Glass bottles, test tubes and instruments are neatly "  
                       + "arranged and chemical reagent bottles are clearly"], 
        "tool":["sufuric acid"]
    },
    "physic_lab":{
        "description":[" In the physics laboratory, reflected in the neat lab bench. " 
                       + "Equipment is complete, from high precision instruments to " 
                       + "various circuit components. A faint chemical odor permeates " 
                       + "the lab, and slight mechanical hum and electrical cacophony" 
                       + "form the background sound."],
        "tool":["ball"],
    },
    "biology_lab":{
        "description":["Microscopes, test tubes and petri dishes are arranged " 
                       + "on long tables. Lab benches were neat and organized, " 
                       + "with chemicals and biological samples properly stored." 
                       + " The fresh scent of disinfectant filled the air. "],
        "tool":["None"]
    },
    "math_classroom":{
        "description":[" In the math classroom, the whiteboard is covered with " 
                       + "math formulas and diagrams. The worn tables were piled" 
                       + " up in a small mountain."],
        "tool":["calculator"]
    },
    "english_classroom":{
        "description":["The English classroom wall lined with shelves filled with" 
                       + " books ranging from classic literature to contemporay novel"],
        "tool":["bible"]
    },
    "washroom":{
        "description":["Abandoned toilets with splintered walls, rusty facets," 
                       + " and cracked sinks. The broken mirror reflects a blurred" 
                       + " figure. Moss grows in the cracks of the bricks on the " 
                       + "floor, filling the room with a gloomy odor"],
      "tool":["None"]
    },
    "history_classroom":{
        "description":[" In the dilapidated history classroom, the walls peeled back" 
                       + " and dim light poured through the broken windows. Old desks" 
                       + " and chairs are scattered. Some worn literature was spread" 
                       + " out on the table."],
        "tool":["science information"]
    },
    "psychological_classroom":{
        "description":["In the dilapidated psych classroom, the walls were peeling" 
                       + " away, and dim light spilled through the cracked windows," 
                       + " creating an eerie glow. The tables and chairs in the center" 
                       + " of the classroom were messy and collapsed, scattered with" 
                       + " broken pens and papers."],
        "tool":["None"]
    },
    "computer_science":{
        "description":["The computer lab is dim, shrouded in dust and silence. Old" 
                       + " desks and chairs are scattered and tilted, the walls are" 
                       + " peeling, and exposed wires hang in a jumble."],
        "tool":["usb"]
    },
    "gym":{
        "description":["In the dilapidated stadium, walls are peeling and exposed" 
                       + " rebar is everywhere. Dust and cobwebs intertwine, shrouding" 
                       + " the abandoned bleachers."],
        "tool":["ball"]
    },
    "cafeteria":{
        "description":[" In the dilapidated cafeteria, worn tables and chairs are" 
                       + " set up, their surfaces covered in dust and stains. The" 
                       + " walls peeled away, revealing patches of concrete, and" 
                       + " garbage piled up in the corners. Dim lights cast shadows" 
                       + " through tattered lampshades. "],
        "tool":["fork"]
    }
}

map = [
  ["chemistry_lab", "math_classroom", "history_classroom", "gym"],
  ["biology_lab", "english_classroom", "psychological_classroom", "front"],
  ["biology_lab", "washroom", "computer_science", "cafeteria"]
]

map_width = len(map[0])
map_height = len(map)

move = ["walk", "explore"]

direction = ["north", "south", "west", "east"]

bagpack = {
    "player_tools":[],
}

player_pos = {
    "row":0, 
    "col":0
}

main1 = True
# Functions ------------------------------------------------


def main_menu():
    """This function will ask the user input of choosing action
    and if they want to quit or not, this is the main menu
    """
    global main1
    print("Welcom, scavenger, You are now in a school name Rechimons High School.")
    print("Your mission is:\n1:Find the way to get out\n2:Find the missing knowledge")
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
            pass


def player_movement():
    """This function will ask user input the direction they want 
    to go, and it will limit the map boundaries, also it will 
    demonstrate the discription of current environment.
    """
    global main1
    print("\nChoose the direction from following list\nEnter 'quit' if you want to quit")
    print(direction)
    wrongInput = True
    while wrongInput:
        movement = input("Where do you want to go? ")
        if movement.lower() == "north":
            if player_pos["row"] == 0:
                print("You can't go North!")
            else:
                player_pos["row"] = player_pos["row"] - 1
                wrongInput = False
        elif movement.lower() == "south":
            if player_pos["row"] == map_height - 1:
                print("You can't go South!")
            else:
                player_pos["row"] = player_pos["row"] + 1
                wrongInput = False
        elif movement.lower() == "east":
            if player_pos["col"] == map_width - 1:
                print("You can't go East!")
            else:
                player_pos["col"] = player_pos["col"] + 1
                wrongInput = False
        elif movement.lower() == "west":
            if player_pos["col"] == 0:
                print("You can't go West!")
            else:
                player_pos["col"] = player_pos["col"] - 1
                wrongInput = False
        elif movement.lower() == "quit":
            main1 = False
            wrongInput = False
        else:
            print("Wrong input~ please make sure enter the opition exist in the menu.")
    if main1:
        room_info = maping_sch[map[player_pos["row"]][player_pos["col"]]]["description"]
        print("\n" + room_info[0] + "\n")


def player_action(): 
    """This function define player's action when player input 
    number 1 in the main menue function. When user input one 
    this function allow user choose direction they want to go
    and when user input 2 the function will explore current
    enviromment
    """
    global main1
    print("\nChoose what you want to do from following list\nEnter 'quit'" 
          + " if you want to quit")
    print(move)
    action = input("What do you want to do? ")
    if action.lower() == move[0]:
        player_movement()
    elif action.lower() == move[1]:
        result = maping_sch[map[player_pos["row"]][player_pos["col"]]]["tool"][0]
        if result == "None":
            print("There is nothing here")
        else:
            print("You found " + result)
    elif action.lower() == "quit":
        main1 = False
    else:
        print("Wrong input!")

            
# Main--------------------------------------------------
main_menu()

# CHANGERS !!!!!!!!!!!!!!!!
# Changes !!!!
#test
#tessst

    


