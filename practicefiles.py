#!/usr/bin/env python

import os

### practicing creatiing files for the user
## i want all the use files to be in a folder (directory is that the same thing???) together

## set global vars
user_file_dir = "user_file_dir/"
file_ending = ".txt"


def mk_user_filepath(user_name):
	
	user_filepath = user_file_dir + user_name + file_ending
	
	return user_filepath



def get_user_name():
	
	user_name = raw_input("great! please type your username: ") 
	
	return user_name

def new_player_username(): ####### creat user name for the first time, this should be triggered if you dont have one

	print("welcome new player!!")

	user_name = raw_input("what would you like your username to be? ")
	
	print("")
	
	user_name = is_username_taken(user_name)
		
	return user_name
	
	
def is_username_taken(user_name):
	
	#### this section would be to check if the user name they picked already exists but idk how to search
	
	user_filepath = mk_user_filepath(user_name)

	
	if is_existing(user_filepath):

		print("sorry that username already exists")
		user_name = raw_input("please pick another one ")
		
		is_username_taken(user_name)
			
	return user_name
		



def mk_user_file(user_filepath, user_name):
	
	user_file = open(user_filepath, "a")
	user_file.write("Welcome to " + user_name + "'s user file.")
	print("")
	user_file.close()


def read_user_file(user_filepath):

	user_file = open(user_filepath, "r")
	print(user_file.read()) 
	user_file.close()


def is_existing(doiexist):
	
	existornot = os.path.exists(doiexist) ## this function chekcs to see if the file path exists
	
	return existornot
	
def is_account_existing():
	
	print("")
	has_username = raw_input("do you have a user name? (Y/N) ") #####bad variable name means does the player have a usernam
	print("")
	has_username = has_username.upper()
	
	return has_username
	
def game_main():
	
	has_username = is_account_existing()

	if has_username == "N":
		
		user_name = new_player_username()
	
		user_filepath = mk_user_filepath(user_name)
		mk_user_file(user_filepath, user_name)
	
	if has_username == "Y":
		
		user_name = get_user_name()
		user_filepath = mk_user_filepath(user_name)
		
		if is_existing(user_filepath) == False:
			
			print("sorry, that user name doesn't exist")
			
			game_main()	
	
	return user_filepath
	


############################################
# setup

####check to see if the user_file_dir that we want to put all the user files in exists
if (is_existing(user_file_dir) == False):
	#make dir since it doesn't exist
	os.mkdir(user_file_dir)


# this is where user experience starts

print("")
print("hello!!")

user_filepath = game_main()
	

print("")
read_user_file(user_filepath)
print("")

