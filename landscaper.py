## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "earn": 1, "cost": 0},
]


while(True):
    user_choice = input("[1] Mow Lawn [2] Check Stats [Q] Quit")
    
    if (user_choice == "Q"):
        break
    elif (user_choice == "1"):
        
        print("User mowed the lawn")