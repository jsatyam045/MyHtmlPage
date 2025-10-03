import random   # we need random to shuffle

# Step 1: make the deck (all 52 cards)
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = []   # empty deck

# use two loops to combine each rank with each suit
for suit in suits:
    for rank in ranks:
        deck.append(rank + " of " + suit)

print("Original Deck (Before Shuffling):")
for card in deck:
    print(card)
    
# Step 2: shuffle the deck
random.shuffle(deck)

print("\nShuffled Deck (After Shuffling):")
for card in deck:
    print(card)
