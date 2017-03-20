import os
import random
import time

print '########################'
print '#                      #'
print '#       Omega II       #'
print '#                      #'
print '########################'

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = cards * 4

values = [1, 2, 0, -1, -2]

def value(card):
	if card == 'A':
		val = 0
	elif card == '2':
		val = 1
	elif card == '3':
		val = 1
	elif card == '4':
		val = 2
	elif card == '5':
		val = 2
	elif card == '6':
		val = 2
	elif card == '7':
		val = 1
	elif card == '8':
		val = 0
	elif card == '9':
		val = -1
	elif card == '10':
		val = -2
	elif card == 'J':
		val = -2
	elif card == 'Q':
		val = -2
	elif card == 'K':
		val = -2

	return val

def rand_deck(deck):
	random.shuffle(deck)
	s = random.choice(deck)
	return s

print '\nNumbers?'
num = raw_input('>>> ')
num = int(num)
print 'Time?'
tim = raw_input('>>> ')
tim = int(tim)
print 'Loop?'
lop = raw_input('>>> ')
lop = int(lop)

print '''
______________________________________________________
|_A_|_2_|_3_|_4_|_5_|_6_|_7_|_8_|_9_|_10_|_J_|_Q_|_K_|
|   |   |   |   |   |   |   |   |   |    |   |   |   |
| 0 | 1 | 1 | 2 | 2 | 2 | 1 | 0 | -1| -2 | -2| -2| -2|
|____________________________________________________|
'''

ent = raw_input('Press enter to contine.')
time.sleep(2)

print '________________________\n\n'

while tim >= 0:

	for q in range(lop):
		cardz = []
		print '[',

		cardz.append(rand_deck(deck))
		print cardz[0],
		inc = 1

		for w in range(num-1):
			cardz.append(rand_deck(deck))
			print '\t' + str(cardz[inc]),
			inc = inc + 1

		print ']',

		time.sleep(tim)

		val_c = []
		val_c.append(value(cardz[0]))
		incr = 1
		for p  in range(num-1):
			temp = value(cardz[incr])
			val_c.append(temp)
			incr = incr+ 1

		total_v = sum(list(val_c))

		print '\t\t:: ' + str(total_v) + str(val_c)

	tim = tim - 1







