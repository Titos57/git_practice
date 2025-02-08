from deck import Deck
import random
class Dealer:
    sum = 0
    def __init__(self):
        pass

    def dealers_first_card(self):
        card_num = random.choice(list(Deck.list_deck))
        card_type = random.choice(Deck.list_deck[card_num])
        Deck.list_deck[card_num].remove(card_type)
        Deck.played_cards = (card_num, card_type)
        self.sum += card_num
        print("Dealer is at {} from his first card".format(self.sum))
    
    def dealers_hit(self):
        count = 2
        while(self.sum <= 17):
            print('Dealer draws his {} card'.format(count))
            card_num = random.choice(list(Deck.list_deck))
            card_type = random.choice(Deck.list_deck[card_num])
            Deck.list_deck[card_num].remove(card_type)
            Deck.played_cards = (card_num, card_type)
            self.sum += card_num
            count += 1
        print('Dealer stays at {} reveal your cards'.format(self.sum))
        
