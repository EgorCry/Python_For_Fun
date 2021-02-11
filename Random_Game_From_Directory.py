import glob
from random import randint
from os import startfile

def random_game():
    print()
    print("-"*100)
    files = glob.glob("Path to your games/*.lnk")
    files_steam = glob.glob("Path to your games/*.url")
    print("Do you want Steam games or ordinary?", "Steam: 1", "Ordinary: 2", sep="\n")
    message = input()
    if(message == '1'):
        startfile(files_steam[randint(0, len(files_steam)-1)])
    elif(message == '2'):
        startfile(files[randint(0, len(files)-1)])
    else:
        print("Please, check your input")
        random_game()

random_game()