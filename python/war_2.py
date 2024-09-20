# War Card Game Simulation (https://en.wikipedia.org/wiki/War_(card_game))


from war_base import *



# set rules

min_card = 3       # numbers of minimum card required to play (1/2 doesn't work)

cards_out = 3      # numbers of card to take out while at war

shuffle_cards_on = True    # shuffle cards after each round (Yes/No)

round_limit = 5000      # if limit is reached, it's a draw


input_on = True


# Exception handling

while input_on:
    try:
        min_card = int(input("Numbers of minimum card required to play : "))
        cards_out = int(input("Numbers of card to take out while at war : "))
        round_limit = int(input("Limit of the rounds : "))
        shuffle_cards_on = bool(input("shuffle cards after each round (True(1) / False(0)) : "))
        break
    except:
        print("Sorry! Invalid Input")
        continue



deck = Deck()
deck.shuffle_deck()

player_1 = Player("One")
player_2 = Player("Two")


# splits deck cards equally
for _ in range(26):
    player_1.add_bottom(deck.deal_one())
    player_2.add_bottom(deck.deal_one())


rounds = 0
game_on = True    


while game_on and round_limit > rounds:

    if shuffle_cards_on and rounds > 1:
        print("Shuffling player cards")
        shuffle(player_1.hand_cards)
        shuffle(player_2.hand_cards)

    rounds += 1
    print(f"Round {rounds}")
    at_war = True

    if len(player_1.hand_cards) == 0:
        print(f"{player_1.name} has no cards remaining. {player_2.name} wins the game")
        game_on = False
        break
    elif len(player_2.hand_cards) == 0:
        print(f"{player_2.name} has no cards remaining. {player_1.name} wins the game")
        game_on = False
        break

        
    player_1_table = []
    player_2_table = []
    player_1_table.append(player_1.remove_top())
    player_2_table.append(player_2.remove_top())

    while at_war:
            
        if player_1_table[-1].value > player_2_table[-1].value:
            print(f"{player_1.name} has won the battle")
            player_1.add_bottom(player_1_table)
            player_1.add_bottom(player_2_table)
            at_war = False
            break

        elif player_1_table[-1].value < player_2_table[-1].value:
            print(f"{player_2.name} has won the battle")
            player_2.add_bottom(player_1_table)
            player_2.add_bottom(player_2_table)
            at_war = False
            break

        else:

            print("WAR!")

            if len(player_1.hand_cards) < min_card:
                print(f"{player_1.name} has no cards to play war. {player_2.name} wins the game")
                game_on = False
                break

            elif len(player_2.hand_cards) < min_card:
                print(f"{player_2.name} has no cards to play war. {player_1.name} wins the game")
                game_on = False
                break

            else:
                for _ in range(cards_out):
                    player_1_table.append(player_1.remove_top())
                    player_2_table.append(player_2.remove_top())
else:
    if round_limit <= rounds:
        print("Out of limit. It's a draw")
    else:
        pass
