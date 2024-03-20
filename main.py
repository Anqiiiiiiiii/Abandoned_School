maping_sch = {
    "chemistry_lab":{
        "description":["The lab is brightly lit with white walls and metal countertops. Glass bottles, test tubes and instruments are neatly arranged and chemical reagent bottles are clearly"], 
        "tool":["sufuric acid"]
    },
    "physic_lab":{
        "description":[" In the physics laboratory, reflected in the neat lab bench. The equipment is complete, from high precision instruments to various circuit components. A faint chemical odor permeates the lab, and a slight mechanical hum and electrical cacophony form the background sound."],
        "tool":["ball"],
    },
    "biology_lab":{
        "description":["Microscopes, test tubes and petri dishes are arranged on long tables. Lab benches were neat and organized, with chemicals and biological samples properly stored. The fresh scent of disinfectant filled the air. "],
        "tool":["None"]
    },
    "math_classroom":{
        "description":[" In the math classroom, the whiteboard is covered with math formulas and diagrams. The worn tables were piled up in a small mountain."],
        "tool":["calculator"]
    },
    "english_classroom":{
        "description":["The English classroom wall lined with shelves filled with books ranging from classic literature to contemporary novel."],
        "tool":["bible"]
    },
    "washroom":{
        "description":["Abandoned toilets with splintered walls, rusty facets, and cracked sinks. The broken mirror reflects a blurred figure. Moss grows in the cracks of the bricks on the floor, filling the room with a gloomy odor"],
      "tool":["None"]
    },
    "history_classroom":{
        "description":[" In the dilapidated history classroom, the walls peeled back and dim light poured through the broken windows. Old desks and chairs are scattered. Some worn literature was spread out on the table."],
        "tool":["science information"]
    },
    "psychological_classroom":{
        "description":["In the dilapidated psych classroom, the walls were peeling away, and dim light spilled through the cracked windows, creating an eerie glow. The tables and chairs in the center of the classroom were messy and collapsed, scattered with broken pens and papers."],
        "tool":["None"]
    },
    "computer_science":{
        "description":["The computer lab is dim, shrouded in dust and silence. Old desks and chairs are scattered and tilted, the walls are peeling, and exposed wires hang in a jumble."],
        "tool":["usb"]
    },
    "gym":{
        "description":["In the dilapidated stadium, walls are peeling and exposed rebar is everywhere. Dust and cobwebs intertwine, shrouding the abandoned bleachers."],
        "tool":["ball"]
    },
    "cafeteria":{
        "description":[" In the dilapidated cafeteria, worn tables and chairs are set up, their surfaces covered in dust and stains. The walls peeled away, revealing patches of concrete, and garbage piled up in the corners. Dim lights cast shadows through tattered lampshades. "],
        "tool":["fork"]
    }
}

map = [
  ["chem", "math", "his", "gym"],
  ["biology_lab", "english", "psyc", "front"],
  ["bio", "wc", "cs", "cafe"]
]
map_width = len(map[0])
map_height = len(map)


position = {
    "move":["north, south, west, east"]
}

bagpack = {
    "player_tools":[],
}

player_position = {
    "row":0, 
    "col":0
}

main1 = True


def main_menu():
    global main1
    print("Welcom, scavenger, You are now in a school name Rechimons High School.")
    print("Your mission is:\n1:Find the way to get out\n2:Find the missing knowledge")
    print("Enter 1: For choosing direction\n")
    print("Enter 2: For quit\n")
    playerInput = int(input("Please make your first choice："))
    m_des = True
    while m_des:
        try:
            if playerInput == 1:
                player_movement()
                m_des = False
            elif playerInput == 2:
                main1 = False
            else:
                print("Wrong input number~")
        except ValueError:
            print("Please enter in number form, scavenger!")
        else:
            pass
        finally:
            pass


def player_movement():
    global main1
    print("\nChoose the direction from following list\nEnter 'quit' if you want to quit")
    print(position["move"])
    movement = input("Where do you want to go?")
    if movement.lower() == "north":
        if player_position["row"] == 0:
            print("You can't go North!")
        else:
            player_position["row"] = player_position["row"] - 1
    elif movement.lower() == "south":
        if player_position["row"] == map_height - 1:
            print("You can't go South!")
        else:
            player_position["row"] = player_position["row"] + 1
    elif movement.lower() == "east":
        if player_position["col"] ==
        player_position["col"] = player_position["col"] + 1
    elif movement.lower() == "west":
        player_position["col"] = player_position["col"] - 1
    elif movement.lower() == "quit":
        main1 = False
    if main1:
        print(maping_sch[map[player_position["row"]][player_position["col"]]]["description"])
    else:
        print("Wrong input~ please make sure enter the opition exist in the menu.")


def player_envir():
    if now_pos == "chem":
        print(maping_sch["chemistry_lab"]["description"])
    elif now_pos == "math":
        print(maping_sch["math_classroom"]["description"])
    elif now_pos == "his":
        print(maping_sch["history_classroom"]["description"])
    elif now_pos == "gym":
        print(maping_sch["gym"]["description"])


while main1:
    main_menu()
    


