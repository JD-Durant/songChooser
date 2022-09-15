import pyperclip
import time
import os
import random
from win10toast import ToastNotifier

songList = []
songList = [line.strip() for line in open("Text Files/songs.txt", 'r')]
toast = ToastNotifier()

startUpMessage = '''
Loading.. Please wait...
'''

welcomeMessage = '''
Welcome to Song chooser for Billy Bot!

[1] Setup Instructions

[2] Song Chooser

[3] Information

[4] Exit
'''

instructionMessage = '''
==Instructions on how to use==

[1] Put the names of songs you would like to hear on Billy bot in the text file called "songs.txt", this can be located at "Text Files/songs.txt"

[2] Seperate each song by a line, so for example;

Eternal Groove Android 52
82.99 fm Macross 82-99
Memory Lane AcestoAces
Notice Moeshop

==Note; Do not leave a blank spaces (make sure to check the bottom!) as this will cause issues!)==

[3] Once you are happy with the songs you've chose, head to Song Chooser which will create a play command for you every 20 seconds and copy it to your clipboard
'''

informationMessage = '''
==Information===

This was created by Josh using Python 3.6.2, any questions or suggestions please send me a message

When a song is selected it will be copied to your clipboard automatically. This will then change after 20 seconds depending on the amount of songs you want to queue.
'''

def startup():
    print(startUpMessage)
    time.sleep(3)
    os.system('cls||clear')
    main()

def main():
    print(welcomeMessage)
    try:
        userChoice = int(input('Please select an option from the menu above : '))
    except ValueError:
        print("Please enter a number.")
        os.system('cls||clear')
        main()
    if userChoice == 1:
        os.system('cls||clear')
        setupInstructions()
    elif userChoice == 2:
        os.system('cls||clear')
        songChooser()
    elif userChoice == 3:
        os.system('cls||clear')
        information()
    elif userChoice == 4:
        os.system('cls||clear')
        print("Goodbye, hope to see you soon! <3 Billy & Josh")
        time.sleep(2)
    else:
        os.system('cls||clear')
        print("Please enter a valid option!")
        time.sleep(2)
        main()

def setupInstructions():
    print(instructionMessage)
    input('Press enter to return : ')
    os.system('cls||clear')
    main()   

def songChooser():
    try:
        print(f"There are currently {len(songList)} items in the song queue")
        userAmount = int(input("Please enter the NUMBER of songs you would like to play : "))
    except ValueError:
        print("Please enter a number.")
        time.sleep(2)
        os.system('cls||clear')
        songChooser()
    tempList = songList
    if len(songList) < userAmount:
        print("Cannot complete task as number selected is lower than queue length!")
        print("Returning to main menu")
        time.sleep(4)
        os.system('cls||clear')
        main()
    else:
        x = 0
        print(f"Starting task with a delay of 20 seconds..")
        while x != userAmount:
            toast.show_toast(
                "New Song copied to clipboard",
                "20 Seconds till next song",
                duration = 5,
                icon_path = "notificationIcon.ico",
                threaded = True,
            )
            choice = random.choice(tempList)
            pyperclip.copy(f'?play {choice}')
            time.sleep(20)
            tempList.remove(choice)
            x = x + 1
            print("Moving onto next song")
        print("Task complete, returning to main menu..")
        time.sleep(3)
        os.system('cls||clear')
        main()
    
                
def information():
    print(informationMessage)
    input('Press enter to return : ')
    os.system('cls||clear')
    main()

startup()
    
