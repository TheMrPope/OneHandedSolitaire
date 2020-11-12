import random
from card import Card

# Deck Class Provided by the Computer Science Department at Utah State University
class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        for i in range(52):
            self.__deck.append(Card(i))
        random.shuffle(self.__deck)

    def draw(self):
        return self.__deck.pop()

    # This function written by Jake Pope
    def view(self, index):
        return self.__deck[index]

    # This function written by Jake Pope
    def __len__(self):
        return len(self.__deck)
