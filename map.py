# Import library
from tabulate import tabulate

# maps external filename
mapfile = "map.txt"
myfile = "map.txt"
# information about player on reading map
map = [["chemistry_lab", "math_classroom", "history_classroom", "gym"],
   [
       "biology_lab", "english_classroom", "psychological_classroom",
       "front"
   ], ["physic_lab", "washroom", "computer_science", "cafeteria"]]

map_width = len(map[0])
map_height = len(map)

player_action = ["walk", "explore", "check bagpack"]

direction = ["north", "south", "west", "east"]

player_pos = {"row": 0, "col": 0}


def read_map():
    """This function create a visual map for reader after they 
    input walk as their action option.
    """
    try:
        with open(mapfile, 'w') as file:
            file.write(tabulate(map,tablefmt = 'fancy_grid'))
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