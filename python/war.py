"""War Card Game Simulation (https://en.wikipedia.org/wiki/War_(card_game))"""

from random import shuffle


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return f"{self.rank} of {self.suit}"
    

class Deck:

    def __init__(self):
        print("Deck Created")
        
        self.deck_cards = []

        for suit in suits:
            for rank in ranks:

                created_card = Card(suit, rank)
                self.deck_cards.append(created_card)

    def shuffle_deck(self):
        """Shuffles deck cards"""

        print("Shuffling deck cards")
        shuffle(self.deck_cards)

    def deal_one(self):
        """Remove one card from the list of all_cards"""

        return self.deck_cards.pop()



class Player:

    def __init__(self, name):
        self.name = name
        self.hand_cards = []

    def remove_top(self):
        """Removes one top card"""

        return self.hand_cards.pop(0)
    

    def add_bottom(self, cards):
        """Adds one card to bottom"""

        if type(cards) == type([]):
            self.hand_cards.extend(cards)
        else:
            self.hand_cards.append(cards)





def main():
    """Main Script"""

    print("Welcome to War Card Game")

    # Set rules
    cards_out = 3  # number of cards to take out during a war
    shuffle_cards_on = True  # shuffle cards after each round (Yes/No)
    round_limit = 5000  # round limit before the game ends in a draw

    input_on = True

    # Exception handling for input
    while input_on:
        try:
            cards_out = int(input("Number of cards to take out during a war (1-25): "))
            if cards_out < 1 or cards_out > 25:
                print("Please enter a number between 1 and 25.")
                continue

            round_limit = int(input("Round limit: "))
            if round_limit <= 0:
                print("Round limit must be a positive integer.")
                continue

            shuffle_input = int(input("Shuffle cards after each round (1 for Yes, 0 for No): "))
            if shuffle_input not in (0, 1):
                print("Please enter 0 or 1")
                continue
            shuffle_cards_on = bool(shuffle_input)

            input_on = False  # Exit loop if all inputs are valid

        except ValueError:
            print("Sorry! Invalid input")

    deck = Deck()
    deck.shuffle_deck()

    player_1 = Player("One")
    player_2 = Player("Two")

    # Split deck cards equally
    for _ in range(26):
        player_1.add_bottom(deck.deal_one())
        player_2.add_bottom(deck.deal_one())

    rounds = 0
    game_on = True

    while game_on and round_limit > rounds:
        if shuffle_cards_on and rounds > 0:  # Starts from round 1
            print("Shuffling player cards")
            shuffle(player_1.hand_cards)
            shuffle(player_2.hand_cards)

        rounds += 1
        print(f"Round {rounds}")

        # Check if any player has no cards left
        if len(player_1.hand_cards) == 0:
            print(f"{player_1.name} has no cards remaining. {player_2.name} wins the game")
            game_on = False
            break
        elif len(player_2.hand_cards) == 0:
            print(f"{player_2.name} has no cards remaining. {player_1.name} wins the game")
            game_on = False
            break

        # Each player plays one card (face-up)
        player_1_t_card = player_1.remove_top()
        player_2_t_card = player_2.remove_top()
        table = [player_1_t_card, player_2_t_card]


        while True:
            # Normal battle: compare top cards
            if player_1_t_card.value > player_2_t_card.value:
                print(f"{player_1.name} wins the battle")
                player_1.add_bottom(table)
                break
            elif player_1_t_card.value < player_2_t_card.value:
                print(f"{player_2.name} wins the battle")
                player_2.add_bottom(table)
                break
            else:
                # WAR CASE
                print("WAR!")

                # Check if players have enough cards for war
                if len(player_1.hand_cards) < cards_out + 1:
                    print(f"{player_1.name} doesn't have enough cards for war. {player_2.name} wins the game")
                    game_on = False
                    break
                elif len(player_2.hand_cards) < cards_out + 1:
                    print(f"{player_2.name} doesn't have enough cards for war. {player_1.name} wins the game")
                    game_on = False
                    break

                # Add face-down war cards
                for _ in range(cards_out):
                    table.append(player_1.remove_top())
                    table.append(player_2.remove_top())
            
            # Add face-up cards for comparison
                player_1_card = player_1.remove_top()
                player_2_card = player_2.remove_top()
                table.append(player_1_card)
                table.append(player_2_card)

    
    if round_limit <= rounds:
            print("Round limit reached. It's a draw")
        




if __name__ == "__main__":
    main()
