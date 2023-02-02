## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0},
    {"name": "pair of rusty scissors", "profit": 5, "cost": 5},
    {"name": "old-timey push lawnmower", "profit": 50, "cost": 25},
    {"name": "fancy battery-powered lawnmower", "profit": 100, "cost": 250},
    {"name": "team of starving students", "profit": 250, "cost": 500}
]

## Game Options

def cut_lawn():
    tool = tools[game['tool']]
    print(f"You mowed a lawn with your {tool['name']} and made ${tool['profit']}")
    game['money'] += tool['profit']
    
def check_stats():
    tool = tools[game['tool']]
    print(f"You currently have ${game['money']} and using {tool['name']}")
    
def shop():
    if (game['tool'] >= len(tools) - 1):
        print("No more upgrades available")
    next_tool = tools[game['tool']+1]
    if (next_tool is None):
        print("There is no more tools")
        return 0
    if (game['money'] < next_tool['cost']):
        print("Not enough money")
        return 0
    print("You are upgrading your tool")
    game['money'] -= next_tool['cost']
    game['tool'] += 1
    
def win_check():
    if (game['tool'] == 4 and game['money'] >= 1000):
        print("You Win")
        return True
    return False

while(True):
    user_choice = input("[1] Mow Lawn [2] Check Stats [3] Purchase [4] Quit")
    
    if (user_choice == "1"):
        cut_lawn()
        
    if (user_choice == "2"):
        check_stats()
        
    if (user_choice == "3"):
        shop() 
    
    elif (user_choice == "4"):
        print("You quit the game")
        break

    elif (win_check()):
        break  