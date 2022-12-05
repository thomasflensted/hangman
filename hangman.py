import random

guessedLetters = []
ALLOWEDATTEMPTS = 10


def main():

    word = getWord()

    if guessWord(word):

        print("Congratulations! You guessed the word.")

    else:

        print(f"You used all your attempts. The word was {word}")


def getGuess():

    guess = input("Type a letter: ").upper()

    while True:

        if not guess.isalpha():

            print("Only letters are accepted.\n")
            guess = input("\nType a letter: ")

        elif guess in guessedLetters:

            print("You already tried that letter.\n")
            part1 = ", ".join(guessedLetters[0:len(guessedLetters)-1])
            print(
                f"You also already tried: {part1} and {guessedLetters[len(guessedLetters)-1]}.")
            guess = input("\nType a letter: ")

        else:

            guessedLetters.append(guess)
            return guess


def getWord():

    found = False

    with open("./nouns.txt", "r") as nounList:

        words = nounList.readlines()

        while not found:
            word = random.choice(words).strip().upper()
            if len(word) > 3 and len(word) < 9:
                found = True

    print(f"The word consists of {len(word)} letters")
    return word


def guessWord(word):

    dashWord = "_" * len(word)
    print(f"\n{dashWord}\n")
    attempts = 0

    while attempts <= ALLOWEDATTEMPTS:

        guess = getGuess()
        attempts += 1

        if guess == word:

            print(f"\n{word}\n")
            return True

        elif guess in word:

            dashWord = replaceDashes(dashWord, word, guess)
            print(f"\n{dashWord}\n")

            if dashWord == word:

                return True

    return False


def replaceDashes(dashWord, word, guess):

    for i, letter in enumerate(word):

        if letter == guess:

            dashWord = list(dashWord)
            dashWord[i] = guess
            dashWord = "".join(dashWord)

    return dashWord


if __name__ == "__main__":
    main()
