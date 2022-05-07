import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True



class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit



class Deck:
    
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = '' 
        for card in self.deck:
            deck_comp += '\n' + card.__str__() 
        return 'The deck has' + deck_comp
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def add_card(self,card):
    self.cards.append(card)
    self.value += values[card.rank]

  def adjust_for_ace(self):
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1

def hit(deck,hand):
  hand.add_card(deck.deal())
  hand.adjust_for_ace()

def hit_or_stand(deck,hand):
  global playing

  while True:
    x = input("Would you like to Hit or Stand? H = hit  S = stand")
    if x[0].lower() == 'h':
      hit(deck,hand)

    elif x[0].lower() == 's':
      print("Player stands. Dealer is playing.")
      playing = False

    else:
      print("Try again")
      continue
    break

def show_some(player,dealer):
  print("\nDealer's Hand:")
  print("<card hiddenn>")
  print('',dealer.cards[1])
  print("\Player's Hand:", *player.cards, sep='\n')

def show_all(player,dealer):
  print("\nDealer's Hand:", *dealer.cards, sep='\n')
  print("Dealer's Hand =", dealer.value)
  print("\nPlayer's Hand:", *player.cards, sep = '\n')
  print("\Player's Hand:", *player.cards, sep='\n')

def player_busts(player,dealer):
  print("Player Busts!")

def player_wins(player,dealer):
  print("Player Wins!")

def dealer_busts(player,dealer):
  print("Dealer Busts!")

def dealer_wins(player,dealer):
  print("Dealer Wins!")

def push(player,dealer):
  print("Tie! Its a push.")

while True:
  deck = Deck()
  deck.shuffle()

player_hand = Hand()
player_hand.add_card(deck.deal())
player_hand.add_card(deck.deal())

dealer_hand = Hand()
dealer_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())

show_some(player_hand,dealer_hand)

while playing:
  hit_or_stand(deck,player_hand)

  show_some(player_hand,dealer_hand)

  if player_hand.value > 21:
    player_busts(player_hand,dealer_hand,)
    break

  if player_hand.value <= 21:

    while dealer_hand.value < 17:
      hit(deck,dealer_hand)

      show_all(player_hand,dealer_hand)

  if dealer_hand.value > 21:
    dealer_busts(player_hand,dealer_hand)

  elif dealer_hand.value > player_hand.value:
    dealer_wins(player_hand,dealer_hand)

  elif dealer_hand.value < player_hand.value:
    player_wins(player_hand,dealer_hand)

  else:
    push(player_hand, dealer_hand)

  new_game = input("Would you like to play again? 'y' or 'n'")

  if new_game[0].lower()=='y':
    playing=True
    continue
  else:
    print("Thanks for playing!")
    break