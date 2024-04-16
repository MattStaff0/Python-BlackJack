import Deck

class Hand():
    #Class attribute
    og_deck = Deck.Deck()

    def __init__(self):
        self.shuffled = Hand.og_deck.shuffle_deck()
        self.played_cards = []
        self.dealer_hand = []
        self.player_hand = []

        print("Passing out your cards... \n")

        for i in range(-1,-3,-1):
            self.dealer_hand.append(self.shuffled[i])
            self.played_cards.append(self.shuffled.pop(i))
        print(f"Dealer's first card: {self.dealer_hand[1]}")


        for i in range(-1, -3, -1):
            self.player_hand.append(self.shuffled[i])
            self.played_cards.append(self.shuffled.pop(i))
        print(f"Player's cards: {self.player_hand[0]}, {self.player_hand[1]}")
    
    
    def get_player_total(self):
        self.total = 0
        for card in self.player_hand:
            self.total += card[2]
        return self.total
    
    def get_dealer_total(self):
        self.total = 0
        for card in self.dealer_hand:
            self.total += card[2]
        return self.total
    
    def check_player_bust(self):
        if self.get_player_total() > 21 and 'Ace' in [y for x in self.player_hand for y in x[0]]:
            for card in self.player_hand:
                if card[0] == 'Ace':
                    card[2] = 1
            return True
        elif self.get_player_total() > 21:
            return False
        else:
            return True

    def check_dealer_bust(self):
        if self.get_dealer_total() > 21 and 'Ace' in [y for x in self.dealer_hand for y in x[0]]:
            for card in self.dealer_hand:
                if card[0] == 'Ace':
                    card[2] = 1
            return True
        elif self.get_dealer_total() > 21:
            return False
        else:
            return True
    
    def hit_player(self):
        try:
            self.player_hand.append(self.shuffled[-1])
            self.played_cards.append(self.shuffled.pop(-1))
            print("\nPlayer Successfully hit\n")
            print(f"Player cards:")
            for i in range(0,len(self.player_hand)):
                print(self.player_hand[i])
        except Exception as e:
            print(f"Error in hitting... {e}")
            
    def hit_dealer(self):
        try:
            self.dealer_hand.append(self.shuffled[0])
            self.played_cards.append(self.shuffled.pop(0))
            print("\nDealer Successfully hit\n")
            print("Dealer's Visible Cards:")
            for i in range(1,len(self.dealer_hand)):
                print(self.dealer_hand[i])
        except:
            print('Error in hitting dealer')

    def stand(self):
         if (self.get_player_total() > self.get_dealer_total()) and self.check_player_bust():
             return 1
         elif (self.get_player_total() == self.get_dealer_total()) and self.check_player_bust():
               return 2
         elif (self.get_player_total() < self.get_dealer_total()) and self.check_player_bust():
               return 3

        


