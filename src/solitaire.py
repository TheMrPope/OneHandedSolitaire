from deck import Deck
from hand import Hand
import sys

def playGame(f):
    # Set up deck and hand
    deck = Deck()
    hand = Hand()

    # Write deck setup
    f.write("Deck: ")
    for i in range(len(deck)):
        f.write(deck.view(i).getNickName() + " ")

    f.write("\n")

    stillPlaying = True
    needToDraw = True
    noMatch = False

    while stillPlaying:

        # draw up to 4 if able and if need to
        while (len(hand) < 4 and needToDraw) or noMatch:
            if len(deck) > 0:
                hand.add(deck.draw())
                noMatch = False
            else:
                break

        needToDraw = False


        while not needToDraw:
            if not isMatch(hand) and not isSuit(hand):
                needToDraw = True
                noMatch = True
            elif isMatch(hand):
                hand.matchRemove()
            elif isSuit(hand):
                hand.suitsRemove()

        if len(deck) == 0 and noMatch:
            stillPlaying = False


    # Determine Results
    cardsLeft = len(hand)
    f.write("Ending Hand: ")

    for j in range(cardsLeft):
        f.write(hand.view(j).getNickName() + " ")

    f.write("\n" + str(cardsLeft) + " Cards Left\n\n")

    if cardsLeft == 0:
        return True
    else:
        return False

def isMatch(h):
    if len(h) < 4:
        return False
    else:
        return h.view(0).getRank() == h.view(3).getRank()

def isSuit(h):
    if len(h) < 4:
        return False
    else:
        return h.view(0).getSuit() == h.view(3).getSuit()

def main(games=10000):

    winCount = 0

    # Set up stats file
    f = open("stats.txt", "w")

    for i in range(games):
        if playGame(f):
            winCount += 1

    winPercent = (winCount / games) * 100

    f.write("\n")
    f.write("Final Stats: \n")
    f.write("Games Played: " + str(games) + "\t" + "Games Won: " + str(winCount) + "\t" + "Winning %: " +
            str(winPercent))
    f.close()


if len(sys.argv) > 1:
    try:
        numGames = int(sys.argv[1])
        main(numGames)
    except:
        print("ERROR: Unaccepted argument \'" + sys.argv[1] + "\' is not an integer")
        sys.exit(1)
else:
    main()

