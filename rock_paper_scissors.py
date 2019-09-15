# Lets play the game with python code 

import random # Thank you google for helping me on this module import 

available_options = ['rock', 'paper', 'scissors']

python_choice = random.choice(available_options)
user_choice = input('Enter your choice rock, paper, scissors : ')

# Making sure user knows how to play the game 
if user_choice not in available_options :
	print('\n\n', 'You need to learn the game before you play!')
	print('Good Bye!', '\n\n')
else :
	print('Python picked : ', python_choice)
	print('You picked : ',user_choice)


	# Lets see who wins the game 
	while(True) :
		if python_choice == user_choice :
			print('\n\n', 'Game Tied. Try again', '\n\n')
			python_choice = random.choice(available_options)
			user_choice = input('Enter your choice rock, paper, scissors : ')
			print('Python picked : ', python_choice)
			print('You picked : ',user_choice)
		elif python_choice == 'rock' and user_choice == 'scissors' :
			print('\n\n', 'Python is the winner!')
			print('Good Bye!', '\n\n')
			break;
		elif python_choice == 'paper' and user_choice == 'rock' :
			print('\n\n', 'Python is the winner!')
			print('Good Bye!', '\n\n')
			break;
		elif python_choice == 'scissors' and user_choice == 'paper' :
			print('\n\n', 'Python is the winner!')
			print('Good Bye!', '\n\n')
			break;
		else :   
			print('\n\n', 'You are the winner!')
			print('Good Bye!', '\n\n')
			break;

