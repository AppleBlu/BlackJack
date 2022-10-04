from cards import pack_of_cards
import random


class Dealer:

    def __init__(self):
        self.cards = pack_of_cards
        self.users_cards = [random.choice(list(self.cards)) for i in range(2)]
        self.hit_card = None
        self.total_value = 0
        self.dealers_cards = []

    def get_a_hit_card(self):
        self.hit_card = random.choice(list(self.cards))

    def deal_cards(self, lst):
        lst[0] = self.users_cards[0]
        lst[1] = self.users_cards[1]

    def deal_hit_card(self, lst, index):
        lst[index] = self.hit_card

    def get_value(self):
        total = 0
        total += self.cards.get(self.users_cards[0])
        total += self.cards.get(self.users_cards[1])
        return total

    def hit_or_stick(self, turns, cards, total):
        print('\nWould you like to hit or stick?')
        if turns == 0:
            self.get_a_hit_card()
            question = (input('Enter \"h\" for hit and \"s\" for stick: '))
            if question == 'h':
                self.deal_hit_card(cards, 2)
                print(f'\nThe dealer dealt you a [{self.hit_card}]')
            elif question == 's':
                exit()
        elif turns == 1:
            self.get_a_hit_card()
            question = (input('(h/s): '))
            if question == 'h':
                self.deal_hit_card(cards, 3)
                print(f'\nThe dealer dealt you a [{self.hit_card}]')
            elif question == 's':
                exit()
        if turns == 2:
            self.get_a_hit_card()
            question = (input('(h/s): '))
            if question == 'h':
                self.deal_hit_card(cards, 4)
                print(f'\nThe dealer dealt you a [{self.hit_card}]')
            elif question == 's':
                exit()


class User:

    def __init__(self):
        self.cards = ['', '', '', '', '', '', '']
        self.user_turn = 0
        self.total = 0

    def update_turns(self):
        self.user_turn += 1

    def bust_check(self):
        if self.total > 21:
            print('\nSorry your bust')
            exit()

    def blackjack_check(self):
        if self.total == 21:
            print('\nBLACKJACK, You win!!!')
            exit()

    def get_cards(self):
        return self.cards

    def update_total(self):
        if self.user_turn == 0:
            self.total += pack_of_cards.get(self.cards[0])
            self.total += pack_of_cards.get(self.cards[1])
            return self.total
        elif self.user_turn == 1:
            self.total += pack_of_cards.get(self.cards[2])
            return self.total
        elif self.user_turn == 2:
            self.total += pack_of_cards.get(self.cards[3])
            return self.total


# Initiating classes
dealer = Dealer()
user1 = User()


def application():
    dealer.get_a_hit_card()

    print('\nWelcome to blackjack')

    dealer.deal_cards(user1.cards)

    user1.update_total()

    print(f'\nThe dealer dealt you a [{user1.get_cards()[0]}] and a [{user1.get_cards()[1]}]')
    print(f'\nThat brings you to {user1.total}')

    user1.blackjack_check()

    dealer.hit_or_stick(user1.user_turn, user1.cards, user1.total)

    user1.update_turns()
    user1.update_total()

    print(f'\nThat Now brings you to {user1.total}')

    user1.blackjack_check()
    user1.bust_check()

    dealer.hit_or_stick(user1.user_turn, user1.cards, user1.total)

    user1.update_turns()
    user1.update_total()

    print(f'\nThat Now brings you to {user1.total}')

    user1.blackjack_check()
    user1.bust_check()

    print(user1.cards)


application()
