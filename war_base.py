# War Card Game Simulation (https://en.wikipedia.org/wiki/War_(card_game))


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




# def split_cards(player_1, player_2, deck):
#     """Split deckcards equally"""

#     for _ in range(26):
#         player_1.add_bottom(deck.deal_one())
#         player_2.add_bottom(deck.deal_one())



def main():

    deck = Deck()
    deck.shuffle_deck()

    player_1 = Player("One")
    player_2 = Player("Two")

    # split_cards(player_1, player_2, deck)

    # splits deck cards equally
    for _ in range(26):
        player_1.add_bottom(deck.deal_one())
        player_2.add_bottom(deck.deal_one())


    rounds = 0
    game_on = True    


    while game_on:

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

                if len(player_1.hand_cards) < 5:
                    print(f"{player_1.name} has no cards remaining. {player_2.name} wins the game")
                    game_on = False
                    break

                elif len(player_2.hand_cards) < 5:
                    print(f"{player_2.name} has no cards remaining. {player_1.name} wins the game")
                    game_on = False
                    break

                else:
                    for _ in range(5):
                        player_1_table.append(player_1.remove_top())
                        player_2_table.append(player_2.remove_top())





if __name__ == "__main__":
    main()
