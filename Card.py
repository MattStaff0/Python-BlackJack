'''
BlackJack Card Game Card Class to define card ranks
'''


class Card():
    #class attribute
    rank_dict = {
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '10':10,
        'Jack':10,
        'Queen':10,
        'King':10,
        'Ace':11,
    }
    suit_tup = ('Spades', 'Hearts', 'Diamond', 'Club')
    name_tup = ('2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace')

    #init method
    def __init__(self, card_suit, card_name):
        self.card_suit = card_suit
        self.card_name = str(card_name)
        self.card_rank = Card.rank_dict[card_name]
        self.card_info = [self.card_name, self.card_suit, self.card_rank]

    def __str__(self):
        return f'name: {self.card_name}, suit: {self.card_suit}, rank: {self.card_rank}'
    
    def ace_chage_one(self):
        Card.rank_dict['Ace'] = 1
        self.card_rank = Card.rank_dict[self.card_name]

    def ace_chage_eleven(self):
        Card.rank_dict['Ace'] = 11
        self.card_rank = Card.rank_dict[self.card_name]

       
