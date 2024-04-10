
player_tools = []


def addingTool(item):
  global player_tools
  player_tools.append(item)


def function(result):
    if result == "None":
        print("\nThere is nothing here")
    else:
        print("\nYou found " + result)
        addingTool(result)