# Generates a shuffled deck (shuffled list of numbers from 1 - 52)
# Numbers are converted to appropriate card number and suit as needed

# Program options:
# Enter 'd' to deal a card
# Enter 'n' to shuffle a new deck
# Enter 'p' to show deck
# Enter 'q' to exit the program
# Enter '?' for these options

#!/usr/bin/python

import sys
import random

def shuffle():
	deck = range(1, 53)
	random.shuffle(deck)
	return deck

def deal(deck):
	next_card = deck.pop()
	return next_card

# Find suit of the card - 1 to 13 is Spades, 14 to 26 is Hearts, 27 to 39 is Diamonds and 40 to 52 is Clubs
def find_suit(card):
	if card >= 40:
		suit = 'Club'
	elif card >= 27:
		suit = 'Diamond'
	elif card >= 14:
		suit = 'Heart'
	else:
		suit = 'Spade'
	return suit

# Find card number and convert to face card if needed
def find_num(card):
	card = card % 13
	if card == 1:
		card = 'A'
	elif card == 11:
		card = 'J'
	elif card == 12:
		card = 'Q'
	elif card == 0:
		card = 'K'
	return card

# Show cards in the deck or hand
def show(cards):
	for i in range(len(cards)):
		print ('%2s %s' % (find_num(cards[i]), find_suit(cards[i])))

def quit():
	print "Exiting"
	sys.exit()

def options():
	print "d --- deal card"
	print "n --- shuffle new deck"
	print "p --- show deck"
	print "q --- exit program"
	print "? --- show these options"
	return

def main():
	deck = shuffle()
	while True:
		command = raw_input('> ')
		if command == 'd':
			card = deal(deck)
			print ('%2s %s' % (find_num(card), find_suit(card)))
		elif command == 'n':
			print "Shuffled new deck"
			deck = shuffle()
		elif command == 'p':
			show(deck)
		elif command == 'q':
			quit()
		elif command == '?':
			options()
		else:
			print "Enter ? for help"

if __name__ == '__main__':
	main()