import random
import os
import itertools
import matplotlib.pyplot as plt

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

#create a player class that has a hand, money, and a bet
class Player:
    def __init__(self, hand, money, bet):
        self.hand = [hand]
        self.money = money
        self.bet = bet

#creating a dealer class that has a hand
class Dealer:
    def __init__(self, hand):
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
    count = 0
    for card in hand:
        if card[count]['rank'] in ['J','Q','K']:
            handValue += 10
        elif card[count]['rank'] in ['2','3','4','5','6','7','8','9','10']:
            print("value of the card is:",card[count]['rank'])
            handValue += int(card[count]['rank']) 
        elif card[count]['rank'] in ['A']:
            if handValue + 11 > 21:
                handValue += 1
            else:
                handValue += 11
        count += 1
    if handValue > 21:
        return True
    else:
        return False, handValue

def isBlackjack(hand):
    if len(hand) == 2:
        if hand[0]['rank'] in ['10','J','Q','K'] and hand[1]['rank'] in ['A']:
            return True
        elif hand[1]['rank'] in ['10','J','Q','K'] and hand[0]['rank'] in ['A']:
            return True
        else:
            return False
    else:
        return False

#betting
#---------------------------------------------------------------------------------#
def play(hand, dealersCard):
    handValue = isBust(hand)
    if handValue[1] == 9 and dealersCard['rank'] in ['3','4','5','6']:
        play = 'double'
    elif handValue[1] == 10 and dealersCard['rank'] in ['2','3','4','5','6','7','8','9']:
        play = 'double'
    elif handValue[1] == 11:
        play = 'double'
    elif handValue[1] == 12 and dealersCard['rank'] in ['4','5','6']:
        play = 'stand'
    elif handValue[1] in [13,14,15,16] and dealersCard['rank'] in ['2','3','4','5','6']:
        play = 'stand'
    elif handValue[1] == 17:
        play = 'stand'
    elif hand[1]['rank'] == 'A' and hand[0]['rank'] == '2' and dealersCard['rank'] in ['5','6']:
        play = 'double'
    elif hand[1]['rank'] == 'A' and hand[0]['rank'] == '3' and dealersCard['rank'] in ['5','6']:
        play = 'double'
    elif hand[1]['rank'] == 'A' and hand[0]['rank'] == '4' and dealersCard['rank'] in ['4','5','6']:
        play = 'double'
    elif hand[1]['rank'] == 'A' and hand[0]['rank'] == '5' and dealersCard['rank'] in ['4','5','6']:
        play = 'double'
    elif hand[1]['rank'] == 'A' and hand[0]['rank'] == '6' and dealersCard['rank'] in ['3','4','5','6']:
        play = 'double'
    elif hand[1]['rank'] == 'A' and hand[0]['rank'] == '7' and dealersCard['rank'] in ['3','4','5','6']:
        play = 'double'
    elif hand[1]['rank'] == 'A' and hand[0]['rank'] == '7' and dealersCard['rank'] in ['2','3','4','5','6','7','8']:
        play = 'stand'
    elif hand[1]['rank'] == 'A' and hand[0]['rank'] == '8':
        play = 'stand'
    elif hand[1]['rank'] == '2' and hand[0]['rank'] == '2' and dealersCard['rank'] in ['3','4','5','6']:
        play = 'split'
    elif hand[1]['rank'] == '3' and hand[0]['rank'] == '3' and dealersCard['rank'] in ['3','4','5','6']:
        play = 'split'
    elif hand[1]['rank'] == '4' and hand[0]['rank'] == '4' and dealersCard['rank'] in ['5','6']:
        play = 'split'
    elif hand[1]['rank'] == '5' and hand[0]['rank'] == '5' and dealersCard['rank'] in ['2','3','4','5','6','7','8','9']:
        play = 'double'
    elif hand[1]['rank'] == '6' and hand[0]['rank'] == '6' and dealersCard['rank'] in ['2','3','4','5','6',]:
        play = 'split'
    elif hand[1]['rank'] == '7' and hand[0]['rank'] == '7' and dealersCard['rank'] in ['2','3','4','5','6','7']:
        play = 'split'
    elif hand[1]['rank'] == '8' and hand[0]['rank'] == '8':
        play = 'split'
    elif hand[1]['rank'] == '9' and hand[0]['rank'] == '9' and dealersCard['rank'] in ['2','3','4','5','6','8','9']:
        play = 'split'
    elif hand[1]['rank'] == '9' and hand[0]['rank'] == '9' and dealersCard['rank'] in ['7','10','A']:
        play = 'split'
    elif hand[1]['rank'] == 'A' and hand[0]['rank'] == 'A':
        play = 'split'
    elif hand[1] == '10' and hand[1] == '10':
        play = 'stand'
    else:
        play = 'hit'
    return play

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
    hand.append(dealCard(deck))
    return hand

def simulateRound(deck, count, numPlayers):
    #dealers 
    for i in range(1):
        dealersCard = Dealer(dealCard(deck))
        if i == 1:
            count += updateCount(dealersCard.hand, count)
    #players
        for j in range(int(numPlayers)):
            player = Player([dealCard(deck)], 5000, 100)
            if i == 0:
                player.hand.append(dealCard(deck))
            print("Player's hand: ", player.hand)
    print(isBust(player.hand))
    count += updateCount(dealersCard.hand, count)
    return count


#game is played with 1 deck
money = 5000
deck = createShoe(5)
deck = shuffleDeck(deck)

simulateRound(deck, 0, 1)



#plotCountOccurrences(simHands[3])
#print(simHands[1])
