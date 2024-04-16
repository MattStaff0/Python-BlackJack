import Card
import Deck
import Chips 
import Hand

# Basic Methods

def welcome():
    print("[!] Welcome to BlackJack [!]\n")

def make_deck():
    deck = Deck.Deck()
    return deck

def make_chip():
    chips = Chips.Chips(get_balance())
    return chips

def get_balance():
    while True:
        try:
            bal = float(input("Enter your balance: "))
        except:
            print(f'Looks like that is not a valid balance, please retry')
        else:
            break
    print("Successfully stored balance.\n")
    return bal

def make_hand():
    hand = Hand.Hand()
    return hand

def ask_for_bet():
    while True:
        try:
            bet = float(input('Enter your bet: '))
        except Exception as e:
            print(f'Error: {e}')
        else:
            break
    return bet

    
def ask_hit_or_stand():
    while True:
        try:
            result = input('Would you like to stand or hit?:\n').lower().strip()
            if result == 'hit':
                return True
            elif result == 'stand':
                return False
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")
        except Exception as e:
            print(f"Error: {e}")

def hit_check_player(hand,chips,amount):
    hand.hit_player()
    if not(hand.check_player_bust()):
        print("You Busted!")
        print("Dealer's Cards:\n")
        for i in range(0,len(hand.dealer_hand)):
                print(hand.dealer_hand[i])
        print("\nSubtracting Funds From Balance...")
        chips.withdraw(amount)
        return True
    return False

def hit_check_dealer(hand,chips,amount):
    if hand.get_dealer_total() >= 17:
        print("\nDealer Stands...")
        return False
    hand.hit_dealer()
    if not(hand.check_dealer_bust()):
        print("Dealer Busted!")
        print("Dealer's Cards:\n")
        for i in range(0,len(hand.dealer_hand)):
                print(hand.dealer_hand[i])
        print("\nAdding Bet Back To Balance...")
        chips.deposit(amount)
        
        return True
    return False

def check_stand(hand, chips,amount):
    if hand.stand() == 1:
        print(f'Player wins!')
        print("Dealer's Cards:\n")
        for i in range(0,len(hand.dealer_hand)):
                print(hand.dealer_hand[i])
        print("\nAdding Funds To Balance...")
        chips.deposit(amount)
        if play_again() == 'yes':
            play_game(chips)
        else:
            quit()
        
    if hand.stand() == 2:
        print(f'Draw!')
        print("Dealer's Cards:\n")
        for i in range(0,len(hand.dealer_hand)):
                print(hand.dealer_hand[i])
                print("\nAdding Bet Back To Balance...")
        chips.deposit(amount)
        if play_again() == 'yes':
            play_game(chips)
        else:
            quit()
          
    if hand.stand() == 3:
        print("Dealer Wins!")
        print("Dealer's Cards:\n")
        for i in range(0,len(hand.dealer_hand)):
                print(hand.dealer_hand[i])
        print("\nSubtracting Funds From Balance...")
        chips.withdraw(amount)
        if play_again() == 'yes':
            play_game(chips)
        else:
            quit()

def play_again():
    while True:
        try:
            result = input("Would you like to play again?:\n")
            return result.lower().strip()
        except Exception as e:
            print(f'Error: {e}')

def ask_deposit():
    while True:
        try:
            result = input("Would you like to deposit any money into your account?:\n")
            if result.lower().strip() == 'yes':
                return True
            else:
                return False
        except Exception as e:
            print(f'Error: {e}')



def play_game(chips):
    print(f'\n\nWelcome Back!')
    print(f'Your current balance: {chips.bal}')
    if ask_deposit():
        while True:
            try:
                amount = float(input('Enter amount to deposit: '))
            except Exception as e:
                print(f'Error: {e}')
            else:
                break
        chips.deposit(amount)
    if chips.bal == 0:
        print(f"Your balance is currently: {chips.bal} you need to deposit money to keep playing")
        while chips.bal == 0:
                try:
                    amount = float(input('Enter amount to deposit(enter -1 to quit): '))
                    if amount == -1:
                        quit()
                    elif amount < 0:
                        print("Invalid deposit amount. Please enter a positive value.")
                        continue
                except Exception as e:
                    print(f'Error: {e}')
                else:
                    chips.deposit(amount)
   
    while True:
        bet_amount = ask_for_bet()
        if chips.bet(bet_amount):
            break
        else:
            continue
    
    #hand logic
    hand = make_hand()
    hit_or_stand = ask_hit_or_stand()
    while hit_or_stand == True:
        if hit_or_stand:
            if hit_check_player(hand,chips,bet_amount):
                choice = play_again()
                if play_again() == 'yes':
                    play_game(chips)
                else:
                    quit()

            if hit_check_dealer(hand,chips,bet_amount):
                if play_again() == 'yes':
                    play_game(chips)
                else:
                    quit()
        hit_or_stand = ask_hit_or_stand()
    check_stand(hand,chips,bet_amount)

# basic logic
def main():
    #For first time playing
    welcome()

    #Bet Logic
    chips = make_chip()

    #input validation to make sure bet is within balance
    while True:
        bet_amount = ask_for_bet()
        if chips.bet(bet_amount):
            break
        else:
            continue
    
    #hand logic
    hand = make_hand()
    hit_or_stand = ask_hit_or_stand()
    while hit_or_stand == True:
        if hit_or_stand:
            if hit_check_player(hand,chips,bet_amount):
                choice = play_again()
                if play_again() == 'yes':
                    play_game(chips)
                else:
                    quit()

            if hit_check_dealer(hand,chips,bet_amount):
                if play_again() == 'yes':
                    play_game(chips)
                else:
                    quit()
        hit_or_stand = ask_hit_or_stand()
    check_stand(hand,chips,bet_amount)
            
    
    




    
    
    
    

if __name__ == '__main__':
    main()


    




    