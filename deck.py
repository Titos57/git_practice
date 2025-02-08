import random
from player import Player
class Deck:
    lost = False
    win = False
    list_deck = {2:['Spades', 'Diamonds', 'Hearts', 'Clubs'], 3:['Spades', 'Diamonds', 'Hearts', 'Clubs'], 4:['Spades', 'Diamonds', 'Hearts', 'Clubs'], 5: ['Spades', 'Diamonds', 'Hearts', 'Clubs'], 6: ['Spades', 'Diamonds', 'Hearts', 'Clubs'], 7: ['Spades', 'Diamonds', 'Hearts', 'Clubs'], 8:['Spades', 'Diamonds', 'Hearts', 'Clubs'], 9:['Spades', 'Diamonds', 'Hearts', 'Clubs'], 10: ['Spades', 'Diamonds', 'Hearts', 'Clubs'], 'King': ['Spades', 'Diamonds', 'Hearts', 'Clubs'], 'Queen':['Spades', 'Diamonds', 'Hearts', 'Clubs'], 'Jack': ['Spades', 'Diamonds', 'Hearts', 'Clubs'], 'Aces': ['Spades', 'Diamonds', 'Hearts', 'Clubs']}
    played_deck =[]
    def __init__(self, amount_of_cards):
        self.amount_of_cards = amount_of_cards

    def first_card(self):
        card_num = random.choice(list(Deck.list_deck)) # choose a random key(2 for example)
        card_type = random.choice(Deck.list_deck[card_num])# in 2 chooses one of 4 values
        print('Your first card is {} of {}'.format(card_num, card_type))
        Deck.list_deck[card_num].remove(card_type)
        Deck.played_cards = (card_num, card_type)
        self.sum = card_num

    def hit(self):
        card_num = random.choice(list(Deck.list_deck))
        card_type = random.choice(Deck.list_deck[card_num])
        print("Your next card is {} of {}".format(card_num, card_type))
        Deck.list_deck[card_num].remove(card_type)
        Deck.played_cards = (card_num, card_type)
        if isinstance(card_num, int):
            self.sum += card_num
        elif card_num in ['King', 'Queen', 'Jack']:
            self.sum += 10
        elif card_num == 'Aces':
            self.sum += 11 if self.sum + 11 <= 21 else 1
        print("You now are at {}".format(self.sum))
        if sum == 21:
            print('You win you have the strongest hand!')
            self.win = True
        elif sum > 21:
            print('Unfortunately you lost...')
            self.lost = True
    
    def stand(self):
        print('Great, you stayed at {}, now it is dealers turn to draw his cards.'.format(self.sum))
        self.win = True
    
    def double_down(self):
        print('You increased your bet, and draw one last card.')
        self.hit()
        Player.amount = Player.amount * 2
        self.win = True
    
    def surrender(self):
        print('You gave up half your bet chips and lost.')
        self.lost = True
        Player.amount = Player.amount / 2