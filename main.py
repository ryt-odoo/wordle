from tools import *
from tools.word_treatment import *
from tools.display import *
def main():
    """this game consists of guessing a chosen word from a predefined list
        the player has only six chances to findout the word."""
    word = choose_a_word.choose_a_word()
    print(f"the word is {word}")
    non_existing = []
    count = 0
    while count < 6:
        while True:
            your_guess = input("enter a five letter word:")
            try:
                assert your_guess.isalpha()
            except AssertionError:
                print("you only can enter letters")
                continue
            try:
                assert len(your_guess) == 5
            except AssertionError:
                print("the length of the word must be 5 letters")
                continue
            try:
                assert len(set(your_guess).intersection(set(non_existing))) == 0
            except AssertionError:
                print("Avoid excluded letters !!!!!!!!")
                continue

            break
        if your_guess == word:
            print (f"congratulation you guessed the right word in {count+1} steps")
            print (f"the word was: {word}")
            break
        non_existing.extend(non_existing_letters.non_existing_letters(your_guess,word))
        result = compare_words.compare_words(your_guess,word)
        print(non_existing)
        display_result.display_result(result)
        count += 1
        if count == 6:
            print("sorry you lost!!!!")
            print(f"the word was {word}")


if __name__ == "__main__":
    main()