import random
import os
import itertools
import matplotlib.pyplot as plt

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

#create a player class that has a hand, money, and a bet
class Player:
    def __init__(self, hand, money, bet):
        self.hand = hand
        self.money = money
        self.bet = bet

#creating a dealer class that has a hand
class Dealer:
    def __init__(self, hand, privHand):
        self.privHand = privHand
        self.hand = hand

#plotting the data
# ---------------------------------------------------------------------------------#
def plotCountOccurrences(countTracker):
    counts = {}
    for count in countTracker:
        if count in counts:
            counts[count] += 1
        else:
            counts[count] = 1
    x = list(counts.keys())
    y = list(counts.values())
    plt.bar(x, y)
    plt.xlabel('Count')
    plt.ylabel('Occurrences')
    plt.title('Count Occurrences')
    plt.show()

#creating decks and shuffling them
# ---------------------------------------------------------------------------------#
def createShoe(numDeck):
    ranks = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    shoe = [{'rank': rank, 'suit': suit} for _ in range(numDeck) for rank, suit in itertools.product(ranks, suits)]
    return shoe

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def dealCard(deck):
    if len(deck) > 0:
        return deck.pop()
    else:
        return None

# Keeping track of the count
#---------------------------------------------------------------------------------#
#using zen counting method from https://betandbeat.com/blackjack/strategy/card-counting/systems/
def updateCount(card, count):
    if card['rank'] in ['2','3','7']:
        count += 1
    elif card['rank'] in ['4','5','6']:
        count += 2
    elif card['rank'] in ['10','J','Q','K',]:
        count -= 2
    elif card['rank'] in ['A']:
        count -= 1
    return count

#Checking values of hands
#---------------------------------------------------------------------------------#
def isBust(hand):
    handValue = 0
    for card in hand:
        if card['rank'] in ['J','Q','K']:
            handValue += 10
            print("value of the card is: 10")
        elif card['rank'] in ['2','3','4','5','6','7','8','9','10']:
            handValue += int(card['rank']) 
            print("value of the card is:",card['rank'])
        elif card['rank'] in ['A']:
            print("value of the card is: 1 or 11")
            if handValue + 11 > 21:
                handValue += 1
            else:
                handValue += 11
    if handValue > 21:
        return True
    else:
        return False, handValue
        

def isBlackjack(hand):
    if len(hand) == 2:
        for card in hand:
            if card['rank'] in ['10','J','Q','K'] and card['rank'] in ['A']:
                return True
            elif card['rank'] in ['10','J','Q','K'] and card['rank'] in ['A']:
                return True
            else:
                return False
    else:
        return False

#Actions
#---------------------------------------------------------------------------------#
def perfPlay(hand, dealersCard):
    handValue = isBust(hand)
    play = ''
    while play != 'stand' and handValue[1] < 21:
        if handValue == 9 and dealersCard['rank'] in ['3','4','5','6']:
            play = 'double'
        elif handValue == 10 and dealersCard['rank'] in ['2','3','4','5','6','7','8','9']:
            play = 'double'
        elif handValue == 11:
            play = 'double'
        elif handValue == 12 and dealersCard['rank'] in ['4','5','6']:
            play = 'stand'
        elif handValue in [13,14,15,16] and dealersCard['rank'] in ['2','3','4','5','6']:
            play = 'stand'
        elif handValue == 17:
            play = 'stand'
        elif any(card['rank'] == 'A' for card in hand) and any(card['rank'] == '2' for card in hand) and dealersCard['rank'] in ['5','6']:
            play = 'double'
        elif any(card['rank'] == 'A' for card in hand) and any(card['rank'] == '3' for card in hand) and dealersCard['rank'] in ['5','6']:
            play = 'double'
        elif any(card['rank'] == 'A' for card in hand) and any(card['rank'] == '4' for card in hand) and dealersCard['rank'] in ['4','5','6']:
            play = 'double'
        elif any(card['rank'] == 'A' for card in hand) and any(card['rank'] == '5' for card in hand) and dealersCard['rank'] in ['4','5','6']:
            play = 'double'
        elif any(card['rank'] == 'A' for card in hand) and any(card['rank'] == '6' for card in hand) and dealersCard['rank'] in ['3','4','5','6']:
            play = 'double'
        elif any(card['rank'] == 'A' for card in hand) and any(card['rank'] == '7' for card in hand) and dealersCard['rank'] in ['3','4','5','6']:
            play = 'double'
        elif any(card['rank'] == 'A' for card in hand) and any(card['rank'] == '7' for card in hand) and dealersCard['rank'] in ['2','3','4','5','6','7','8']:
            play = 'stand'
        elif any(card['rank'] == 'A' for card in hand) and any(card['rank'] == '8' for card in hand):
            play = 'stand'
        elif all(card['rank'] == '2' for card in hand) and dealersCard['rank'] in ['3','4','5','6']:
            play = 'split'
        elif all(card['rank'] == '3' for card in hand) and dealersCard['rank'] in ['3','4','5','6']:
            play = 'split'
        elif all(card['rank'] == '4' for card in hand) and dealersCard['rank'] in ['5','6']:
            play = 'split'
        elif all(card['rank'] == '5' for card in hand) and dealersCard['rank'] in ['2','3','4','5','6','7','8','9']:
            play = 'double'
        elif all(card['rank'] == '6' for card in hand) and dealersCard['rank'] in ['2','3','4','5','6',]:
            play = 'split'
        elif all(card['rank'] == '7' for card in hand) and dealersCard['rank'] in ['2','3','4','5','6','7']:
            play = 'split'
        elif all(card['rank'] == '8' for card in hand):
            play = 'split'
        elif all(card['rank'] == '9' for card in hand) and dealersCard['rank'] in ['2','3','4','5','6','8','9']:
            play = 'split'
        elif all(card['rank'] == '9' for card in hand) and dealersCard['rank'] in ['7','10','A']:
            play = 'split'
        elif all(card['rank'] == 'A' for card in hand):
            play = 'split'
        elif all(card['rank'] == '10' for card in hand):
            play = 'stand'
        else:
            play = 'hit'
        break
    return play

#hit, stand, double, split
def hit(hand, deck, isDoubled):
    if isDoubled == False:
        hand.append(dealCard(deck))
        return hand
    else:
        return hand
    
def stand(hand,):
    return hand

def double(hand, deck):
    hand.append(dealCard(deck))
    return hand

def split(hand, deck):
    hand = [hand[0], dealCard(deck)]
    return hand
#playing the game
#---------------------------------------------------------------------------------#
def simulateHands(numHands, deck, count):
    countTracker = []    
    for i in range(numHands):
        hand = playHand(deck)
        for card in hand:
            count = updateCount(card, count)
            print(count, card['rank'])
        countTracker.append(count)
        #time.sleep(.01)
    return count, max(countTracker), min(countTracker), countTracker

def playHand(deck):
    hand = []
    hand.append(dealCard(deck))
    return hand

def simulateRound(deck, count, numPlayers):
    #dealers 
    for i in range(1,2):
        print(i)
        if i == 1:
            dealersCard = Dealer([dealCard(deck)],[])
        else:
            dealersCard.privHand(dealCard(deck))
    #players
        for j in range(int(numPlayers)):
            player = Player([dealCard(deck)], 5000, 100)
            player.hand.append(dealCard(deck))
    print("Player's hand: ", player.hand)
    print("Dealer's hand: ", dealersCard.hand)
    #Simulates start of round ----------------------------------------------------#
    #if player has blackjack
    
    if isBlackjack(player.hand) == True:
        print("Player has blackjack")
        player.money += player.bet
        print("Player wins")
    else:
        print(perfPlay(player.hand, dealersCard.hand,))
    count += updateCount(dealersCard.hand, count)
    return count

#game is played with 1 deck
money = 5000
deck = createShoe(5)
deck = shuffleDeck(deck)

simulateRound(deck, 0, 1)

#plotCountOccurrences(simHands[3])
#print(simHands[1])
