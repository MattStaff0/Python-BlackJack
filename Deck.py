from Card import*
from random import shuffle

class Deck():
    #class attribute 
    

    #init method
    def __init__(self):
        self.all_cards = []

        for suit in Card.suit_tup:
            for name in Card.name_tup:
                make_card = Card(suit, name)

                self.all_cards.append(make_card.card_info)
    
    def shuffle_deck(self):
        self.shuffled_deck = []
        for list_card in self.all_cards:
            self.shuffled_deck.append(list_card)
        
        shuffle(self.shuffled_deck)
        print(f'Cards Shuffled!\n')
        return self.shuffled_deck
        
        
    def __str__(self):
        for card in self.all_cards:
            print((card))
        return "All cards!"
        
            
        



        


