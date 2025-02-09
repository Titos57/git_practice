from deck import Deck
import random
class Dealer:
    
    def __init__(self):
        self.sum = 0
    
    def dealers_hit(self):
        count = 1
        print('Dealer draws his {} card'.format(count))
        card_num = random.choice(list(Deck.list_deck))
        card_type = random.choice(Deck.list_deck[card_num])
        Deck.list_deck[card_num].remove(card_type)
        Deck.played_cards = (card_num, card_type)
        if isinstance(card_num, int):
            self.sum += card_num
        elif card_num in ['King', 'Queen', 'Jack']:
            self.sum += 10
        elif card_num == 'Aces':
            self.sum += 11 if self.sum + 11 <= 21 else 1
        count += 1
    
        
