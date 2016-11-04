import time, random

name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!\n\n")
story = """
    Evil SKYNET is trying to take control over the world. And guess,
    who is the only hope for the mankind? Yes, you're right - it's you!
    And you must prove your skills, knowledge and intelligence by showing,
    that you are smart and able to guess words!
    """
time.sleep(1)
print(story)
time.sleep(2)   #wait for 1 second
print("\nStart guessing...")
time.sleep(0.5)

word = ["TIRANA", "YEREVAN", "VIENNA", "BAKU",
        "MINSK", "BRUSSELS", "SARAJEVO", "SOFIA", "ZAGREB", "NICOSIA", "PRAGUE",
        "COPENHAGEN", "TALLINN", "HELSINKI", "PARIS", "TBILISI", "BERLIN", "ATHENS",
        "BUDAPEST", "REYKJAVIK", "DUBLIN", "ROME", "ASTANA", "PRISTINA", "RIGA",
        "VADUZ", "VILNIUS", "LUXEMBOURG", "SKOPJE", "VALLETTA", "CHISINAU", "MONACO",
        "PODGORICA", "AMSTERDAM", "OSLO", "WARSAW", "LISBON", "BUCHAREST", "MOSCOW",
        "BELGRADE", "BRATISLAVA", "LJUBLJANA", "MADRID", "STOCKHOLM",
        "BERN", "ANKARA", "KYIV", "LONDON"]
chosen_word = random.choice(word)
guesses = []  #creates an variable with an empty value
turns = 10
good_letter = 0
guess = ""
underline = ""
for lenght in range(len(chosen_word)):
    underline += "_"

while turns > 0:  #check if the turns are more than zero
    print(underline)
    print("\nYou have", + turns, 'more guesses')
    choise = input("Enter l to choise letter or w to write word: ")
    if choise == "l":
        print("Letter history: ", guesses)
        guess = input("\nPlease select a letter between A-Z" + "\n> ").upper()

        if not guess.isalpha(): # check the input is a letter. Also checks an input has been made.
            print("That is not a letter. Please try again.")

        elif len(guess) > 1: # check the input is only one letter
            print("That is more than one letter. Please try again.")

        elif guess in guesses: # check it letter hasn't been guessed already
            print("You have already guessed that letter. Please try again.")

        elif guess not in chosen_word:
            turns -= 1    # turns counter decreases with 1 (now 5)
            print("\nWrong")

        guesses.append(guess)

        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                temp = list(underline)
                temp[position] = guess
                underline = "".join(temp)
                good_letter += 1

        if good_letter == len(chosen_word):
            print(chosen_word)
            print("Congratulations", name, "You Win!")
            again = input("Do you wanna play again? [y - yes] [anything else to quit]")
            if again == "y":
                chosen_word = random.choice(word)
                guesses = []
                turns = 10
                good_letter = 0
                underline = ""
                for lenght in range(len(chosen_word)):
                    underline += "_"
            else:
                exit()

    elif choise == "w":
        userword = input("Enter the word: ").upper()
        if userword == chosen_word:
            print(chosen_word)
            print("Congratulations", name, "You Win!")
            again = input("Do you wanna play again? [y - yes] [anything else to quit]")
            if again == "y":
                chosen_word = random.choice(word)
                guesses = []
                turns = 10
                good_letter = 0
                underline = ""
                for lenght in range(len(chosen_word)):
                    underline += "_"
            else:
                exit()
        else:
            print("Wrong word!")
            turns -= 2
    else:
        print("Wrong input")

    if turns <= 0:       # if the turns are equal to zero
        print(name, "You Loose :(")
        print("Chosen word: ",chosen_word)
        again = input("Do you wanna play again? [y - yes] [anything else to quit]")
        if again == "y":
            chosen_word = random.choice(word)
            guesses = []
            turns = 10
            good_letter = 0
            underline = ""
            for lenght in range(len(chosen_word)):
                underline += "_"
        else:
            exit()
