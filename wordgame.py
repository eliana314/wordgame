#!/usr/bin/env python
from random import choice

########################################################################################## setting variables

	
wordlength = 5
wordlist = ["dream", "found", "board", "child", "peach","stalk","atone","grind","stair","pixel","could","flyer","swear","train","coast","roast","light","night","swine","frock","choke","scope","score","scone"]

#print("just to make this easier to test the secret word is " + secretword)
# print("")

bad_guess_list = ["that letter is not in the secret word :((", "~secretword~ dont have that letter", "sorry not in the secretword T_T", "nope ;-;"]

good_guess_list = ["yayyyyy that letter is in position ", "you got it!!! :D that's in position ", "good job (=^o^=) you'll find that letter in position ", "whooooohooo that is in position "]

found_secretword_list = ["yayyyyy you guessed the word!!!!!", "Woot woot!! you got it :D", "hooooray you got the word UwU", "good job! you got it :)"]


start_game = True



############################################################			

def game_setup(wordlist, wordlength):

	still_playing = 1
	
	guessed_ltrs_list = []
	
	wordstatus_dict = {
	0:"_",
	1:"_",
	2:"_",
	3:"_",
	4:"_"
	}
	
	secretword = (choice(wordlist))
	
	guessed_word = "" 

	
	for counter in range(wordlength):
		new_word_part = wordstatus_dict[counter]
		guessed_word = guessed_word + " " + new_word_part

	return wordstatus_dict, secretword, guessed_word, still_playing, guessed_ltrs_list





########### setting functions  #################################################

def get_ltr_pos(secretword, ltr_raw, ltr_idx):

	##print("in the user guess function")
	ltr_pos = 0
	
	if len(ltr_raw) == 1:
	
		if ltr_idx == -1:
			print(choice(bad_guess_list))
		else:
			ltr_pos = ltr_idx + 1
			print(choice(good_guess_list) + str(ltr_pos))
		
	return ltr_pos
 


########### show letters  #################################################

def show_ltrs(wordlength, wordstatus_dict):
	
	####trying to display where the letter that they guessed is like "_ _ e _ _"
	guessed_word = "" 
	

	for counter in range(wordlength):
		new_word_part = wordstatus_dict[counter]
		guessed_word = guessed_word + " " + new_word_part
	
	
	print(guessed_word)	
	print("")
	
	return guessed_word 


############################################################
def update_wordstatus_dict(wordstatus_dict, ltr_idx, ltr_raw):
	wordstatus_dict[ltr_idx]=ltr_raw
	return wordstatus_dict


############################################################
def get_ltr():
	
	ltr_raw = raw_input("Guess a letter: ")
	ltr_raw = ltr_raw.lower()
	print("")
	is_ltr = ltr_raw.isalpha()
	
	if len(ltr_raw) > 1:
		print("only enter one letter at a time pls >:(((")
	
	if is_ltr == False:
		print("letters are a, b, c, ect, you must guess a letter to play this game. learn more at https://www.youtube.com/watch?v=w_-lz2BI2Co")
		print("")		
		
		get_ltr()
	return ltr_raw




############################################################	
def show_guessed_ltrs_list(ltr_raw):
	
	if len(ltr_raw) == 1:
		guessed_ltrs_list.append(ltr_raw)
		print("so far you've guessed:")
		print(" ".join(guessed_ltrs_list))
		print("")
	


############################################################	
def get_start_game(guessed_word):	
	
	guessed_word = ""
	start_game_raw = raw_input("would you like to play again (Y/N) ")
	print("")
	start_game_raw = start_game_raw.upper()	

	if len(start_game_raw) > 1:
		print("please only type Y or N")
		get_start_game(guessed_word)
		
	if start_game_raw == "Y":
		start_game = True
	else:
		start_game = False
		
	return guessed_word, start_game
		
####this function is trying to clear the wordstausdict which is basically the guessed word so that the user can play again on a clean slate but i dont rly know how. I took some code from show ltrs and just left outthe show part.  		



#####we need a is_game_over()func which checks teh winning conditions and resets the vars as needed

## if conditions met return TRUE
## check for _ in guessword
## reset the still_playing to 0

def is_game_over(guessed_word):
	is_blank_space = guessed_word.find("_")
	
#### in this case 1 = true and 0-1 = false for the still_playing var	
	
	if is_blank_space == -1:
		still_playing = 0
		
	else:
		still_playing = 1
		
	return still_playing


	

########################################################################################the actual game


while start_game: # this will always be yes by default,since we set it to that
	
	
	wordstatus_dict, secretword, guessed_word, still_playing, guessed_ltrs_list = game_setup(wordlist, wordlength)
	#print("setup:"+ secretword, guessed_word)

	## start the game from the users perspective
	print("lets play a word game!")
	print("the computer will choose a random word that is five letters long. you will guess letters, and the computer will tell 	you if they're in the word and where they are.")
	print("please only enter one letter at a time")
	print(" ")

	while still_playing > 0:
	
		ltr_raw = get_ltr()
		ltr_idx = secretword.find(ltr_raw)

		get_ltr_pos(secretword, ltr_raw, ltr_idx)
		wordstatus_dict = update_wordstatus_dict(wordstatus_dict, ltr_idx, ltr_raw)
		guessed_word = show_ltrs(wordlength, wordstatus_dict)
		show_guessed_ltrs_list(ltr_raw)
	
		
		
		## this is where we decide if teh game has been won
		still_playing = is_game_over(guessed_word)
		
		print("----------------------------------------------------------------------")
		print("")

	# we have broken out of stillplayingloop because no more underscores
	#so give them a success msg
	print(choice(found_secretword_list))
	print("")
			
	guessed_word, start_game = get_start_game(guessed_word)

# this is outside the Y code, and so is triggered when play again != Y
print("")
print("thanks for playing!!")				
print("")
