import random


class Dealer:

    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 1,
                      2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.c1 = random.choice(self.cards)
        self.c2 = random.choice(self.cards)
        self.c3 = random.choice(self.cards)
        self.c4 = random.choice(self.cards)

    def remove_cards(self):
        self.cards.remove(self.c1)
        self.cards.remove(self.c2)
        self.cards.remove(self.c3)
        self.cards.remove(self.c4)


class Player:

    def __init__(self, card_1, card_2, card_3, card_4):

        self.card_1 = card_1
        self.card_2 = card_2
        self.card_3 = card_3
        self.card_4 = card_4
        self.total = 0
        self.hit_or_stick_1 = None
        self.hit_or_stick_2 = None
        self.hit_or_stick_3 = None
        self.hit_or_stick_4 = None
        self.player_turn = 0

    def hit_or_stick(self):
        if self.player_turn == 0:
            print('Would you like to hit or stick?')
            self.hit_or_stick_1 = (input('Enter \"h\" for hit and \"s\" for stick: '))
            self.player_turn += 1
            print(self.hit_or_stick_1)
        elif self.player_turn == 1:
            print('Would you like to hit or stick?')
            self.hit_or_stick_2 = (input('Enter \"h\" for hit and \"s\" for stick: '))
            self.player_turn += 1
            print(self.hit_or_stick_2)
        elif self.player_turn == 2:
            print('Would you like to hit or stick?')
            self.hit_or_stick_3 = (input('Enter \"h\" for hit and \"s\" for stick: '))
            self.player_turn += 1
            print(self.hit_or_stick_3)
        elif self.player_turn == 3:
            print('Would you like to hit or stick?')
            self.hit_or_stick_4 = (input('Enter \"h\" for hit and \"s\" for stick: '))
            self.player_turn += 1
            print(self.hit_or_stick_4)

    def get_total(self):
        self.total = self.card_1 + self.card_2
        return self.total

    def hit(self):
        if self.hit_or_stick_1 == 'h':
            total_after_move_1 = self.total = self.total + self.card_3
            print(f'The dealer delt you a {self.card_3}. Your new total is {total_after_move_1}')
            self.hit_or_stick_1 = ''
        elif self.hit_or_stick_1 == 's':
            exit()
        elif self.hit_or_stick_2 == 'h':
            total_after_move_2 = self.total = self.total + self.card_4
            print(f'The dealer delt you a {self.card_4}. Your new total is {total_after_move_2}')
            self.hit_or_stick_2 = ''
        elif self.hit_or_stick_2 == 's':
            exit()

    def bust_check(self):
        if self.total > 21:
            print('Sorry your bust')
            exit()

    def blackjack_check(self):
        if self.total == 21:
            print('BLACKJACK, You win!!!')
            exit()

    def __repr__(self):
        print(
            f'The dealer delt you a {self.card_1} and a {self.card_2}, '
            f'which brings you to a card total of {self.total}.')
        print('\n---------------------------\n')
        self.hit_or_stick()
        print('\n---------------------------\n')
        self.hit()
        self.bust_check()
        self.blackjack_check()
        print('\n---------------------------\n')
        self.hit_or_stick()
        print('\n---------------------------\n')
        self.hit()
        self.bust_check()
        self.blackjack_check()

        return ''


dealer = Dealer()
player1 = Player(dealer.c1, dealer.c2, dealer.c3, dealer.c4)
player1.get_total()

print(player1)

# dealer.remove_cards()
# print(dealer.cards)
# print(dealer.get_cards())
# print(dealer.get_delt_cards())
# cards = [player1.card_1, player1.card_2]
# print(player1.get_total())
# print(player1)
