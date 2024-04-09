from tabulate import tabulate

myfile = "map.txt"

map = [["chemistry_lab", "math_classroom", "history_classroom", "gym"],
   [
       "biology_lab", "english_classroom", "psychological_classroom",
       "front"
   ], ["physic_lab", "washroom", "computer_science", "cafeteria"]]

mapfile = 'map.txt'

with open(mapfile, 'w') as file:
    file.write(tabulate(map,tablefmt = 'fancy_grid'))

map_width = len(map[0])
map_height = len(map)

move = ["walk", "explore"]

direction = ["north", "south", "west", "east"]

bagpack = {
"player_tools": [],
}

player_pos = {"row": 0, "col": 0}

#function
def read_map():
    try:
        with open(myfile, "r") as f:
            f2 = f.readlines()
    except:
        print("")
    else:
        for line in f2:
            print(line)
    finally:
        print("")

read_map()

