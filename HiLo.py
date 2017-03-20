# made by Mauri Vanoro

import os
import time
import random

sets = [1, 0, -1]
random.shuffle(sets)

def numb():
	random.shuffle(sets)
	s = random.choice(sets)
	return s

print   "#############################"
print	"#                           #"
print	"#                           #"
print	"#      Cardu Countingu      #"
print	"#        Mauri Vanoro       #"
print	"#                           #"
print	"#                           #"
print	"#############################"


print "Total Numbers?"
tn = raw_input('>>> ')
tn = int(tn)
print "Delay?"
secs = raw_input('>>> ')
secs = int(secs)
print "Rounds?"
rounds = raw_input('>>> ')
rounds = int(rounds)

brode = []
print '_______________________'

while rounds > 0:
	for i in range(rounds):
		print "[",
		brode.append(numb())
		print brode[0],
		de = 1

		for s in range(tn-1):
			brode.append(numb())
			print '\t' + str(brode[de]),
			de = de + 1
		print "]",
		time.sleep(secs)
		print '\t\t',
		numsum = sum(list(brode))
		print ":: " + str(numsum)
		brode = []


