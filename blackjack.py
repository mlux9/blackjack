# Play Blackjack against computer (dealer)

#!/usr/bin/python

import cards
import sys

# Deal a card from the deck to the given hand
def hit(hand, deck):
	hand.append(cards.deal(deck))
	return hand

# Player stands - Dealer's turn
def dealers_turn(dealer_hand, deck):
	while sum_points(dealer_hand) < 17:
		dealer_hand = hit(dealer_hand, deck)
	return dealer_hand

def compare(dealer_hand, player_hand):
	dealer_points = sum_points(dealer_hand)
	player_points = sum_points(player_hand)

	show_table(player_hand, dealer_hand)
	print ('Dealer has a total of %d points' % dealer_points)
	print ('You have a total of %d points' % player_points)
	if dealer_points > 21:
		print 'Dealer busts! You win'
	else:
		if (dealer_points > player_points):
			print 'You lose!'
		elif (dealer_points == player_points):
			print 'Draw!'
		else:
			print 'You win!'

def check_blackjack(hand):
	if (sum_points(hand) == 21 and len(hand) == 2):
		return True
	return False

# Deal two cards each to player and dealer and show face up cards 
def start_game():
	deck = cards.shuffle()
	player_hand = []
	dealer_hand = []

	for i in range(2):
		player_hand.append(cards.deal(deck))
		dealer_hand.append(cards.deal(deck))

	print
	print 'Starting a new game...'

	return (deck, player_hand, dealer_hand)

# Show current state of the table (all cards that are face up)
# First card in dealer's hand is hole card (dealt face down and not visible to player)
def show_table(player, dealer):
	print '---------------'
	print 'YOUR HAND'
	cards.show(player)
	print '---------------'
	print 'DEALER\'S HAND'
	cards.show(dealer) 
	print '---------------'
	return

# Check status of the game depending on the current points
# If points are under 21 show the highest possible total
# If points equal 21 check for blackjack/dealer's turn
# If points are over 21 bust
# Return 0 if game will continue, 1 if starting a new game
def check_status(points, player_hand, dealer_hand, deck):
	if points < 21:
		show_table(player_hand, dealer_hand[1:])
		print ('Highest total is %d points' % points)
		return 0
	else:
		if points > 21:
			show_table(player_hand, dealer_hand)
			print ('Busted! Lowest total is %d points' % points)
		elif points == 21:
			show_table(player_hand, dealer_hand)
			if (check_blackjack(dealer_hand) and check_blackjack(player_hand)):
				print ('Draw! Dealer also has a Blackjack')
			elif (check_blackjack(player_hand)):
				print ('Blackjack! You win')
			elif (check_blackjack(dealer_hand)):
				print ('Dealer has a Blackjack! You lose')
			else:
				print 'You have a total of 21 points'
				print
				print 'Dealer\'s turn'
				dealer_hand = dealers_turn(dealer_hand, deck)
				compare(dealer_hand, player_hand)
		return 1

# Sum point total of the hand
# Return point total if 21 or under, else return -1 to indicate Busted
def sum_points(hand):
	points = 0
	aces = 0
	for i in range(len(hand)):
		card = cards.find_num(hand[i])

		if card == 'J' or card == 'Q' or card == 'K':
			points += 10
		elif card == 'A':
			aces += 1
		else:
			points += card

	if aces == 1:
		if points + 11 > 21:
			points += 1
		else:
			points += 11
	elif aces > 1:
		if points + 11 + (aces-1) > 21:
			points += aces
		else:
			points += (11 + (aces-1))

	return points

def options():
	print "h --- hit (be dealt a card)"
	print "n --- start new game"
	print "s --- stand (keep hand/end turn)"
	print "q --- exit program"
	print "? --- show these options"
	return

def quit():
	print "Exiting - Thanks for playing"
	sys.exit()

def main():
	(deck, player_hand, dealer_hand) = start_game()

	while True:
		if (check_status(sum_points(player_hand), player_hand, dealer_hand, deck)):
			raw_input('Hit enter to play again!')
			(deck, player_hand, dealer_hand) = start_game()
			continue

		print
		command = raw_input('> ')
		if command == 'h':
			player_hand = hit(player_hand, deck)
		elif command == 'n':
			(deck, player_hand, dealer_hand) = start_game()
		elif command == 's':
			dealer_hand = dealers_turn(dealer_hand, deck)
			compare(dealer_hand, player_hand)
			raw_input('Hit enter to play again!')
			(deck, player_hand, dealer_hand) = start_game()
		elif command == 'q':
			quit()
		elif command == '?':
			options()
		else:
			print "Enter ? for help"

	return

if __name__ == '__main__':
	main()