import os

realpath = "user_file_dir/testuser.txt"
fakepath = "user_file_dir/hiiiiii.txt"

username = raw_input("whats yout username? ")
userpath = "user_file_dir/" + username + ".txt"

isexist = os.path.exists(userpath)
print(isexist)


