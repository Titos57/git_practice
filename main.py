from player import Player
from deck import Deck
from dealer import Dealer

name = input("Welcome to the Blackjack table! What is your name?\n")
player = Player(name)
deck = Deck(52) # based on player how many cards we need as parameter
print("Nice to meet you {}, Would you like to start playing (y/n)?\n".format(player.name))
answer = input()
player.answer_check(answer)
print('How many chips would you like to bet?')
bet_amount = input()
player.bet(bet_amount)
deck.first_card() # first card comes in
deck.hit()# second one
while(deck.lost == False or deck.win == False):
    print('Do you want to Hit, Stand, Double Down or Surrender?')
    next_play = input()
    if str(next_play).lower() == 'hit':
        deck.hit()
    elif str(next_play).lower() == 'stand':
        deck.stand()
    elif str(next_play).lower() == 'double down':
        deck.double_down()
    elif str(next_play).lower() == 'surrender':
        deck.surrender()
        print('You lost half your bet, you got only {} chips back'.format(player.amount))
    else:
        print('Invalid input try again!')


