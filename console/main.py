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

attempt_count=''
while True:
	try:
		attempt_count = int(input("How many attempt do you want? from 0 to 16 (0 = infinity count) "))
		if attempt_count >= 0 and attempt_count <=16:
			break
	except ValueError:
		print("Enter number from 0 to 16")

answered = ['*' for x in word['word']]
all_prev = []
prev = ''
right_att = True ## variable to check is last attempt is right
repeated_att = False ## variable to check is last attempt is repeted

while attempt_count != -1:
	print()
	print("Word: "+ ''.join(answered))
	print("Description of word: "+word['description'])
	print("Previous guess: "+ prev)
	print("Attempt left: " + ("infinity" if attempt_count == 0 else str(attempt_count)))
	if not right_att:
		print("In this word no letter: " + prev)
	if repeated_att:
		print("This letter you have already entered")
	ans = input("Choose the letter: ")
	for x in all_prev:
		if x == ans:
			repeated_att = True
			os.system('clear')
			continue
	right_att = False
	for x in range(0,len(word['word'])):
		if ans == word['word'][x]:
			answered[x] = ans
			print(''.join(answered),word['word'])
			print(''.join(answered) == word['word'])
			right_att = True
	os.system('clear')
	if ''.join(answered) == word['word']:
		break
	if attempt_count != 0 and not right_att:
		attempt_count -= 1
		if attempt_count == 0:
			attempt_count = -1
	prev = ans
	all_prev.append(prev)

if attempt_count> -1:
	print()
	print("Word: "+ ''.join(answered))
	print()
	print("Сongratulations, you guessed this word)")
	print()
else:
	print("You loose this game(")
