import csv
from girls import Girl
from boys import Boy
from generator import generate
import logging

g = []
b = []
logging.basicConfig(filename='log.log', filemode='w', format='%(asctime)s %(levelname) s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
generate()
with open('girls.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		g.append(Girl(row['Name'], row['Attractiveness'], row['Intelligence'], row['Budget']))

with open('boys.csv') as csvfile1:
	reader = csv.DictReader(csvfile1)
	for row in reader:
		b.append(Boy(row['Name'], row['Attractiveness'], row['Intelligence'], row['Minimum_req'], row['Budget']))
for i in g:
	for j in b:
		logging.info('Checking: ' + i.name + ' with ' + j.name)
		if i.checkElligible(j) and j.checkElligible(i):
			i.relationshipStatus = 'committed'
			j.relationshipStatus = 'committed'
			j.girlFriendName = i.name
			i.boyFriendName = j.name
			logging.info('Committed: ' +  i.name + ' with ' + j.name)
			break
for x in g:
	if x.relationshipStatus == 'single':
		print(x.name + 'isn\'t committed')
	else:
		print(x.name + ' is a girl friend of: ' + x.boyFriendName)


