import random

cards = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}
card_list = list(cards.keys())

def deal(x: int):
    """compra X cartas"""
    return [random.choice(list(cards.keys())) for n in range(x)]

def calc_hand(hand):
    value = sum(cards[c] for c in hand)  # sugestao do chat, faz mt mais sentido pra cada AS contabiliza -10 e -1 AS se maior q 21
    aces = hand.count('A')

    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value

class Player:
    def __init__(self):
        self.hand = []
        self.money = 0

    def hit(self):
        self.hand.extend(deal(1))
    
    def value(self):
        return calc_hand(self.hand)

    def show(self):
        return f"{', '.join(self.hand)} ({self.value()})"

class Dealer(Player):
    def play(self):
        while self.value() < 17:
            self.hit()


class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.player.money = 2500
    
    def play_round(self):
        # clear hands
        self.player.hand = []
        self.dealer.hand = []
        
        print(f"Money available: ${self.player.money}")

        bet = int(input('Place your bets: $'))
        while bet > self.player.money or bet <= 0:
            print(f"You cannot bet more than you have.")
            bet = int(input('Please place a valid bet amount: $'))
        self.player.money -= bet

        # draw begins
        self.player.hit()
        self.dealer.hit()
        self.player.hit()

        if self.player.value() == 21:
            player_status = 'blackjack'
        else:
            player_status = None

        # show hands
        print(f'Dealer has: {self.dealer.show()}')
        print(f'You have: {self.player.show()}')

        # player turn
        while True:
            if self.player.value () >= 21:
                break

            choice = input('Hit or stay? h/s: ').lower()
            if choice == 's':
                break

            self.player.hit()
            print(f"You have: {self.player.show()}")

        if self.player.value() > 21:
            print("You bust! Dealer wins.")
            return
        
        # Dealer turn
        print("\nDealer's turn...")
        self.dealer.hit()
        if self.dealer.value() == 21:
            dealer_status = 'blackjack'
        else:
            dealer_status = None
            self.dealer.play()
        print(f"Dealer has: {self.dealer.show()}")

        # decide winner
        p = self.player.value()
        d = self.dealer.value()

        if player_status == 'blackjack' and dealer_status == 'blackjack':
            print('Draw')
            self.player.money += bet
            print(f"You got your ${bet} back.")
        elif player_status == 'blackjack' and dealer_status is None:
            print('You win with natural Blackjack')
            self.player.money += bet * 2.5
            print(f'You gained ${bet * 2} ({bet} + {1.5 * bet} reward)')
        elif player_status is None and dealer_status == 'blackjack':
            print("You lose due to dealer's natural Blackjack")
        else:
            if d > 21:
                print('Dealer busts! You win!')
                self.player.money += bet * 2
                print(f'You gained ${bet * 2} ({bet} + {bet} reward)')
            elif p > d:
                print('You win!')
                self.player.money += bet * 2
                print(f'You gained ${bet * 2} ({bet} + {bet} reward)')
            elif p < d:
                print('You lose!')
            else:
                print('Draw')
                self.player.money += bet
                print(f"You got your ${bet} back.")


def main():
    game = Game()
    playing = True

    while playing:
        game.play_round()
        print()
        again = input("Play again? y/n: ").lower()
        if again != 'y':
            playing = False

if __name__ == "__main__":
    main()