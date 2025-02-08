class Player:
    def __init__(self, name):
        self.name = name
    
    def answer_check(self, answer):
        if answer.lower() == 'y':
            print("Great, Let's shuffle the cards and start!")
        else:
            print("Let me know when you are ready to play!")

    def bet(self, amount):
        self.amount = amount
        print('You betted {} chips'.format(amount))
    