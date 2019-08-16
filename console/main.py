from parser import RandomWord ## needed if program find random word form internet
from parser import RandomRightWord ## needed if program find random word form internet
from parser import Dictionary ## needed if you will change random word class to RandomRightWord
import random
import os

hostname = "randomword.com"
response = os.system("ping -c 1 " + hostname)
os.system('clear')

if response == 0:
	#a = RandomWord() ## this
	a = RandomRightWord() ## ot this to get random word
	word = a.get_word()
	ans = ''
	while ans != 1 and ans !=2:
		print('''
1 - get random word from internet
2 - get random word from dictionary (dictionary.txt)
		''')
		try:
			ans = int(input("What you will choose? "))
		except ValueError:
			pass
		os.system('clear')
else:
	ans = 2

if ans == 2:
	with open('dictionary.txt', 'r') as f:
		f = f.read().split('\n')
		for x in range(len(f)-1, -1, -1):
			if f[x]=='':
				del f[x]
		random.shuffle(f)
		word = f[0].split('||')
		word = {'word': word[0], 'description': word[1]}

print(word)

