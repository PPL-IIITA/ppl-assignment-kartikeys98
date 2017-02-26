import csv
from random import randint

def generate():
	with open('boys.csv', 'w') as csvfile:
		fieldnames = ['Name', 'Attractiveness', 'Intelligence', 'Budget', 'Minimum_req']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		i = 1
		while i <= 50:
			spam = {'Name': 'boy'+str(i), 'Attractiveness': randint(1,10), 'Intelligence': randint(1,10), 'Budget': randint(100,1000), 'Minimum_req': randint(1,10)}
			writer.writerow(spam)
			i = i+1

	with open('girls.csv', 'w') as csvfile:
		fieldnames = ['Name', 'Attractiveness', 'Intelligence', 'Budget']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		i = 1
		while i <= 10:
			spam = {'Name': 'girl'+str(i), 'Attractiveness': randint(1,10), 'Intelligence': randint(1,10), 'Budget': randint(100,1000)}
			writer.writerow(spam)
			i = i+1
