# Step 1- Create a Card Class but First make Global Variable
import random
suits = ('Heart','Diamond','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank+ ' of ' + self.suit
    
#Step 2 create Deck class
class Deck:
    
    def __init__(self):
        self.deck = [] #start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The Deck has :" +deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

'''
test_deck = Deck()
test_deck.shuffle()
print(test_deck)

'''
#Hand Class holding objs
class Hand:
    def __init__(self):
        self.cards = [] #star with empty list as we did in class 
        self.value = 0 #start with zero value
        self.aces = 0 #add an attribute to keep track of aces
    
    def add_card(self,card):
        #card passed in from Deck.deal--> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        #track aces
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):
        #check self.value 21 if total value > 21 and still have an ace
        #than change ace to be 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -=10
            self.aces -=1
'''    
test_deck = Deck()
test_deck.shuffle()
#player
test_player = Hand()
#Deal i card from the deck Card(suit,rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

'''
#chip class
class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet 
#Function for Bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many Chips would you like to bet? :  "))
        except ValueError:
            print("Sorry please provide an Integer")
        else:
            if chips.bet>chips.total:
                print('Sorry, Your bet can not exceed', chips.total)
            else:
                break
#Step 7 function for taking hits
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#Step 8 function prompting player to hit or stand
def hit_or_stand(deck,hand):
    global playing #to control an upcoming while loop
    
    while True:
        x = input('Hit or Stand? Enter h or s')
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print('Player stands. Dealer is playing')
            playing=False
        else:
            print('Sorry, Please try again')
            continue
        break

#Step 8 function to display cards
def show_some(player,dealer):
    #Show only one of the dealer's cards
    print("\n Dealer Hand : ")
    print('First card hidden!')
    print(dealer.cards[1])
    
    #Show all (2 cards) of the player's hand/cards
    print("\n Player's hand : ")
    for card in player.cards:
        print(card)
        
def show_all(player,dealer):
    #show all the dealer's cards
    print("\n Dealer's Hand : ")
    for card in dealer.cards:
        print(card)
    '''
    This an other way to show/print card using *args
    print("\n Dealer's hand :",*dealer.cards,sep='\n')
    '''
    #calculate and displa value (3+k == 20)
    print(f'value of Dealer hand is : {dealer.value}')
    
    #show all the player cards
    print("\n Player's hand : ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is : {player.value}")

#Step 9 function to handle end of game scenarios
def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS ! DEALER BUSTED")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("PLAYER WINS ! DEALER BUSTED")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and player tie ! push")

#Buinding UP
while True:
    #Print on opening statement
    print("Welcome to Black Jack")
    #Create & shuffle the deck, deal two cards to each players
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    #Set up the player's chips
    player_chips = Chips()
    
    #prompt the player for their bet
    take_bet(player_chips)
    
    #show cards(but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    while playing: #recall this variable from our hit_or_stand func
        #prompt for player to hit or stand
        hit_or_stand(deck,player_hand)
        
        #show cards(but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        #if player hand exceed 2, run player_bust and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
        #if player hasn't busted, play dealer hand untill dealerreached 17
        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck,dealer_hand)
        #show all cards
        show_all(player_hand,dealer_hand)
        
        #run different wining scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        
        #inform player of thier chip total
        print('\n player total chips are at : {}'.format(player_chips.total))
        
        #ask to play again
        new_game = input("Would youu like to play another hand? y/n")
        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print("Thank You For Playing")
            
            break