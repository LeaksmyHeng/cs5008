"""
The algorithm that we are going to use would be the binary search algorithm.
Explanation:
    First, we will initialized the guess_count to 0
    Then the algorithm would first pick the middle word.
        If the word is the correct one, then guess_count = guess_count + 1, we will print total number of guesses return True.
        If the word is not the correct one which means the actual word could be:
            Before the chosen word, we will pick the middle word between the word that just chosen and the first word
            After the chosen word, we will pick the middle word between the word that just chosen and the last word
            We will increment guess_count to guess_count + 1
        we will run this in a recursive or a loop of k guesses until we find the chosen word.
    return False if it exceed k guesses

Runtime: Since we split it in half, the runtime for this would be log base 2 of (2^k)-1 = k where (2^k)-1 is the words.
        This will give us k guesses at most.

Pseudocode for guessing word game:
    Note: we return true if we found the random word and it is within the k guesses and False if it is not. We do have print statement
    through out to indicate high, low, middle (which is the guess word) and number of guesses.
    I also have a demo for binary search but it is implemented with integer instead cause demoing with word in the dictionary
    is difficult and demo with integer is the same conceptually.

def binary_search_word():
    picked_word = word      # pick random word
    first_word_in_dictionary = 'first_word_in_dictionary'
    final_word_in_dictionary = 'final_word_in_dictionary'

    num_of_guess = 1
    # since it is 2^k-1 words, we will add 1 to the final word so that it is a perfect 2^k and that can avoid error in finding word
    mid_word = (first_word_in_dictionary + (final_word_in_dictionary+1))/2
    print(f'Initial guess: final_word: {final_word_in_dictionary} & first_word: {first_word_in_dictionary} => middle word: {mid_word}')

    # k_guesses is the log base 2 of 2^(k-1) words in dictionary
    for i in range(k_guesses):
        if mid_word == picked_word:
            print(f'Take {count_guess} guesses to guess the word {mid_word}')
            return True
        elif mid_word > picked_word:
            final_word_in_dictionary = mid_word
            mid_word = (first_word_in_dictionary + (final_word_in_dictionary+1))/2
            print(f'Guess lower: final_word: {final_word_in_dictionary} & first_word: {first_word_in_dictionary} => middle word: {mid_word}')
            count_guess += 1
        else:
            first_word_in_dictionary = mid_word
            mid_word = (first_word_in_dictionary + (final_word_in_dictionary+1))/2
            print(f'Guess higher: final_word: {final_word_in_dictionary} & first_word: {first_word_in_dictionary} => middle word: {mid_word}')
            count_guess += 1
    return False
"""

import random
import math


def binary_search(total_number):
    """
    The idea to search for a word in a dictionary and search for the number is technically the same since we are going
    to use binary search, so I will implement this using the number search instead since it is easier to demo.
    """
    # random number are number in between 0 -> total number
    random_number = random.randint(0, total_number)
    total_guess = int(math.log(total_number, 2))
    count_guess = 1
    low = 0
    high = 1024
    number_pick = int((low + (high+ 1)) / 2)
    print(f'This program should take at most {total_guess} to guess the random number\n')
    print(f'Initial guess: high = {high} & low = {low} => middle pick {number_pick}')
    for i in range(total_guess):
        if number_pick == random_number:
            print(f'Take {count_guess} guess the number {random_number} to win')
            return True
        elif number_pick > random_number:
            high = number_pick
            number_pick = int((low + (high+ 1)) / 2)
            print(f'Guess lower: high = {high} & low = {low} => middle pick {number_pick}')
            count_guess += 1
        else:
            low = number_pick
            number_pick = int((low + (high+ 1)) / 2)
            print(f'Guess lower: high = {high} & low = {low} => middle pick {number_pick}')
            count_guess += 1
    print(f'It seems like you already uses all of your guess. Are you sure you follow binary search?')
    return False


def guessing_game(total_number):
    random_num = random.randint(0, total_number)
    total_guess = int(math.log(total_number, 2))

    # if we follow binary search, the total number of guess should be log base 2 of 1024 = 10
    # so the total number of guess shouldn't exceed 10
    user_input = int(input(f'Can you put the number that you want to guess between 0 to {total_number}? '))
    count_guesses = 1
    for i in range(total_guess):
        if isinstance(user_input, int):
            if user_input == random_num:
                print(f'You found the number {user_input} with {count_guesses} guesses')
            elif user_input > random_num:
                user_input = int(input('Try again lower: '))
                count_guesses += 1
            else:
                user_input = int(input('Try again higher: '))
                count_guesses += 1
    print(f'It seems like you already uses all of your guess. Are you sure you follow binary search?')
    return


if __name__ == '__main__':
    ### if you want to play the guessing game, run guess_game
    #guessing_game(1024)
    ### if you want a demo for binary search, run binary_search
    binary_search(1024)