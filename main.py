import random

def pick_word(file):
	f = open(file, 'r')
	ls = []
	for line in f:
		ls.append(line)
	
	f.close()

	if len(ls) == 0:
		print("No words in file")
		exit()
	else:
		word = ls[random.randint(0, len(ls))]

	return word

def check_letter(letter, dictionary):
	if letter in dictionary:
		return True
	else:
		return False

def draw_board(hang_man, lives):
	pass

hang_man = [
"""
+------|
|      O
|     
|	  
|
=========""",

"""
+------|
|      O
|      |
|	   
|
=========""",
"""
+------|
|      O
|     /|
|	  
|
=========
""",
"""
+------|
|      O
|     /|\\
|	  
|
=========
""",
"""
+------|
|      O
|     /|\\
|     / 
|
=========""",
"""
+------|
|      O
|     /|\\
|     / \\
|
=========
"""
]

# NEEDS TO BE FINISHED
# - Draw board showing current hangman status and current letters guessed
# - statment to ask the user if they want to guess a word (USE check_letter function) or a letter (Check if guessed word is equal to chosen_word, doesnt need to be a function)
# - 

if __name__ == "__main__":
	lives = 5 #5 is being used just as an example
	f = input("Enter the name of the file containing a list of words: ")

	if ".txt" not in f:
		print("File must be a txt file")
		exit()
	else:
		chosen_word = pick_word(f)
		letters = {}

		for l in chosen_word:
			if l in letters:
				letters[l] = letters[l] + 1
			else:
				letters[l] = 1

		#Test to show word picked
		print(chosen_word)
		#Test to print letters dictionary and check if a letter is in the dictionary
		while lives > 0:
			guess = input("Enter a letter to see if it is in the chosen word: ")
			print(check_letter(guess, letters))
			lives -= 1

	