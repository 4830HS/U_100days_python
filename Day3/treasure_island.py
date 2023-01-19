print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# left_or_right = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")
# input('You\'re at a crossroad, where do you want to go? Type "left" or "right".')
left_or_right = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()

if (left_or_right) == 'left' :
#   swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if (swim_or_wait) == 'wait' :
#       door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if (door) == 'red' :
            print("Bunred by fire. Game over.")
        elif (door) == 'blue' :
            print("Eaten by beasts. Game over.")
        elif (door) == 'yellow' :
            print("You win.")
        else :
            print("Game over.")        
    else :
        print("Attacked by trout. Game over.")
else :
    print("Fall into a hole. Game over.")