from player import Player
from deck import Deck
from dealer import Dealer

name = input("Welcome to the Blackjack table! What is your name?\n")
player = Player(name)
deck = Deck(52) # based on player how many cards we need as parameter
dealer = Dealer()
print("Nice to meet you {}, Would you like to start playing (y/n)?".format(player.name))
answer = input()
player.answer_check(answer)
while(answer != 'n'):
    print('How many chips would you like to bet?')
    bet_amount = input()
    player.bet(bet_amount)
    deck.amount = bet_amount
    deck.first_card() # first card comes in
    deck.hit()# second one
    while(deck.lost == False and deck.win == False):
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
            print('You got only {} chips back'.format(deck.amount))
        else:
            print('Invalid input try again!')
    if deck.lost == False:
        while(dealer.sum <= 17):
            dealer.dealers_hit()
            if(dealer.sum > 21):
                burnt = True
                print("Dealer got burnt you won! Great Job.")
                player.amount = player.amount * 2
            else:
                print('The Dealer stays at {}'.format(dealer.sum))
        if deck.sum > dealer.sum:
            print("Your cards are stronger {}, You won!".format(player.name.title()))
            player.amount = player.amount * 2
        else:
            print('You lost Dealer got you in that one, Good luck next time.')



