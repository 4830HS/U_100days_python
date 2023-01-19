from art import logo
from art import vs
from game_data import data
import random
import os

random.shuffle(data)

def game() :
    game_end = False
    score = 0
    position = 0
    while not game_end :
        print(logo)

        a = data[position]
        a1 = a['name']
        a2 = a['description']
        a3 = a['country']
        a4 = a['follower_count']

        b = data[position + 1]
        b1 = b['name']
        b2 = b['description']
        b3 = b['country']
        b4 = b['follower_count']

        print(f"Compare A : {a1}, {a2}, {a3}.")

        print(vs)

        print(f"Against B : {b1}, {b2}, {b3}.")

        answer = input("Who has more followers? Type 'A' or 'B' : ").lower()

        position = (position + 1) % len(data)    
        os.system('cls')
        if a4 > b4:
            win = "a"
        else : 
            win = "b"
        if answer == win:
            score += 1
            print(f"You're right! Current score : {score}.")
        else :
            print(logo)
            print(f"Sorry, that's wrong. Final score : {score}.")
            game_end = True
    
game()