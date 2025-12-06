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

def deal(x: int):
    """compra X cartas"""
    return [random.choice(list(cards.keys())) for n in range(x)]  # sugestão do chat, evitar chamar a lista em toda iteração
    # output = []
    # for n in range(x):
    #     output.append(random.choice(list(cards.keys())))
    # return output

def calc_hand(hand):
    value = sum(cards[c] for c in hand)  # sugestao do chat, faz mt mais sentido pra cada AS contabiliza -10 e -1 AS se maior q 21
    aces = hand.count('A')

    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value

    # value = 0  # minha logica original
    # for i in hand:
    #     value += cards[i]
    # for i in hand:
    #     if i == 'A' and value > 21:
    #         value -= 10
    # return value

def main():
    keep_going = True
    money = 2500

    while keep_going:
        # place bets
        bet = 0
        print(f'You have ${money}.')
        bet = int(input('How much would you like to bet? $'))
        money -= bet

        # initial draw
        player_hand = deal(2)
        dealer_hand = deal(1)
        player_status = ''
        dealer_status = ''
        player_value = calc_hand(player_hand)
        dealer_value = calc_hand(dealer_hand)

        print(f'The dealer has: {', '.join(dealer_hand)} ({dealer_value})')
        print(f'You have: {', '.join(player_hand)} ({player_value})')
        if player_value == 21:
            player_status = 'blackjack'
        elif player_value > 21:
            player_status = 'bust'
        else:
            stay = False
            if input('Hit or stay? h/s: ').lower() == 's':
                stay = True
                player_status = 'stay'
            while not stay:
                player_hand.extend(deal(1))  # draws one more
                player_value = calc_hand(player_hand)  # updates value of player hand
                
                print(f'You have: {', '.join(player_hand)} ({player_value})')  # shows current value

                if player_value > 21:
                    stay = True
                    player_status = 'bust'
                    print('Bust!')
                    break
                if input('Hit or stay? h/s: ').lower() == 's':
                    stay = True
                    player_status = 'stay'

            
            dealer_hand.extend(deal(1))
            dealer_value = calc_hand(dealer_hand)
            print(f'Dealer has: {', '.join(dealer_hand)} ({dealer_value})')
        if dealer_value == 21:
            dealer_status = 'blackjack'
        else:
            while dealer_value < 17:
                dealer_hand.extend(deal(1))  # draws one more
                dealer_value = calc_hand(dealer_hand)  # updates hand value
                print(f'Dealer has: {', '.join(dealer_hand)} ({dealer_value})')  # shows hand
            if dealer_value > 21:
                print('Dealer busts!')
                dealer_status = 'bust'
            else:
                dealer_status = 'stay'

        # compare statuses
        if player_status == 'blackjack' and dealer_status != 'blackjack':
            print('You win!')
            money += 2.5 * bet  # 3:2
            print(f'You gained ${2.5*bet} (${bet} + ${1.5*bet} reward)')
        elif player_status != 'blackjack' and dealer_status == 'blackjack':
            print('You lose!')
        elif player_status == 'bust' and dealer_status == 'bust':
            print('Draw!')
            money += bet  # push
            print(f'You got your ${bet} back!')
        elif player_status == 'bust' and dealer_status != 'bust':
            print('You lose!')
        elif player_status != 'bust' and dealer_status == 'bust':
            print('You win!')
            money += 2 * bet  # 1:1
            print(f'You gained ${2*bet} (${bet} + ${bet} reward)')
        elif player_status == 'stay' and dealer_status == 'stay':
            if player_value > dealer_value:
                print('You win!')
                money += 2 * bet  # 1:1
                print(f'You gained ${2*bet} (${bet} + ${bet} reward)')
            elif player_value < dealer_value:
                print('You lose!')
            elif player_value == dealer_value:
                print('Draw!')
                money += bet  # push
                print(f'You got your ${bet} back!')

        if input('Keep going? y/n: ').lower() != 'y':
            keep_going = False

main()