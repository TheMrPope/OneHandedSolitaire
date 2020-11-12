from deck import Deck
from hand import Hand

def playGame(f):
    # Set up deck and hand
    deck = Deck()
    hand = Hand()

    # Write deck setup
    f.write("Deck: ")
    for i in range(52):
        f.write(deck.view(i).getNickName() + " ")

    f.write("\n")

    # Gameplay Loop
    while len(deck) > 0:

        foundMatch = False

        # draw up to 4 cards
        while len(hand) < 4:
            if len(deck) > 0:
                hand.add(deck.draw())
            else:
                break

        if len(hand) < 4:
            break

        if hand.view(0).getRank() == hand.view(3).getRank():
            hand.matchRemove()
            foundMatch = True

        elif hand.view(0).getSuit() == hand.view(3).getSuit():
            hand.suitsRemove()
            foundMatch = True

        if not foundMatch:
            if len(deck) > 0:
                hand.add(deck.draw())

    # Determine Results
    cardsLeft = len(hand)
    f.write(str(cardsLeft) + " Cards Left\n\n")

    if cardsLeft == 0:
        return True
    else:
        return False

def main():

    NUM_GAMES = 10000
    winCount = 0

    # Set up stats file
    f = open("stats.txt", "w")

    for i in range(NUM_GAMES):
        if playGame(f):
            winCount += 1

    winPercent = (winCount / NUM_GAMES) * 100

    f.write("\n")
    f.write("Final Stats: \n")
    f.write("Games Played: " + str(NUM_GAMES) + "\t" + "Games Won: " + str(winCount) + "\t" + "Winning %: " +
            str(winPercent))
    f.close()



# Run File
main()