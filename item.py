# player bagpack list
player_tools = []

# Database for tools description inside the room
item_sch = {
  "sufuric acid": {
      "description": "A funnel with some corrosive liquid inside, could it melt metal?"
  },
  "ball":{
      "description": "A round ball with some butterfly on it."
  },
    "calculator":{
        "description": "A pink calculator, seems there is still some battery left"
    },
    "bible":{
        "description": "The story of Jesus is recorded on the old rolled-edged paper."
    },
    "science information":{
        "description": "Some infomration is unreadable, but it seems like a lab report"
    },
    "usb":{
        "description": "The bracket is broken, but it seems still could use"
    },
    "fork":{
        "description": "The metal peice seems oxidate."
    }
}


def addingTool(item):
    """This function is used for adding players' pick up
    tool after they explore something inside the room, and 
    help to put the tool into their bagpack.
    """
    global player_tools
    player_tools.append(item)


def exploreTool(result):
    """This function help players to eplore their tool inside the
    room and double check if they want to add it into their bagpack 
    or not.
    """
    if result == "None":
        print("\nThere is nothing here")
    else:
        print("\nYou found " + result + "\n" + item_sch[result]["description"])
        print("\nScavengers, Do you want to pick up the tool?")
        pick_tool = input("Enter Yes/No: ")
        if pick_tool.lower() == "yes":
            addingTool(result)
        elif pick_tool.lower() == "no":
            print("Respect your choice Scavnger!")
        else:
            print("Opps, Wrong input!")