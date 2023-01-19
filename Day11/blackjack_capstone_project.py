import random
import os
from art import logo

# Hint 4
def deal_card() :
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_card = random.choice(cards)
    return random_card

# Hint 6
def calculate_score(cards) :
    """Take a list of cards and return the score calculated from the cards"""
    # Hint 7
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    # Hint 8
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Hint 13
def compare(user_score, computer_score) :
    if user_score > 21 and computer_score > 21 :
        return "You went over. You lose."
    if user_score == computer_score :
        return "Draw"
    elif computer_score == 0 :
        return "Lose, opponent has Blackjack."
    elif user_score == 0 :
        return "Win with a Blackjack"
    elif user_score > 21 :
        return "You went over. You lose."
    elif computer_score > 21 :
        return "Opponent went over. You win."
    elif user_score > computer_score :
        return "You win."
    else :
        return "You lose."

def play_game() :
    
    print(logo)

    game_over = False
    user_cards = []
    computer_cards = []

    # Hint 5
    for _ in range(2) :
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Hint 9
    while not game_over :
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards}, current score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21 :
            game_over = True
        
        # Hint 10
        else :
            another_card = input("Type 'y' to get another cards, type 'n' to pass : ")
            if another_card == 'y' :
                user_cards.append(deal_card())
            else :
                game_over = True

    # Hint 12
    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards}, final score : {user_score}")
    print(f"Computer's final hand : {computer_cards}, final score : {computer_score}")
    print(compare(user_score, computer_score))

# Hint 14
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ") == 'y' :
    os.system('cls')
    play_game()