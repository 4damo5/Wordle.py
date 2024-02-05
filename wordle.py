import random as r

#*find out how to add color text to console
#https://www.youtube.com/watch?v=u51Zjlnui4Y&ab_channel=TechWithTim

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)

#when a guess is entered, check if each letter in the chosen word 
#if it is present and in the write space, mark green
#if present and not in right position, mark yellow
#if present but there are multiple and in right space only show correct one
#if guess has 2 of same letter but word only has 1 mark second as incorrect
#if letter is not in word, grey
#check letter by letter, and compare to each spot in the word
#if the guess # exceeds 6 attempts user loses
#if the same letter is guessed don't count it as an attempt
#if an invalid character is entered dont count it as an attempt

#Things to fix:
#duplicate yellow characters for words with double letters

#reading word txt and storing as list
words_file = open('valid-wordle-words.txt', 'r')
word_list = words_file.read().split()

#randomize which word is chosen from the word list
word =  list(word_list[r.randint(0, 14854)].upper())

letter_num = 0

for letter in word:
    word[letter_num] = '\x1b[32m' + letter
    letter_num += 1

player_status = False #did they win or not

guess1 = ['_', '_', '_', '_', '_']
guess2 = ['_', '_', '_', '_', '_']
guess3 = ['_', '_', '_', '_', '_']
guess4 = ['_', '_', '_', '_', '_']
guess5 = ['_', '_', '_', '_', '_']
guess6 = ['_', '_', '_', '_', '_']
guesses = []

current_guess = []

guess_num = 1

#display 6x5 grid of empty letter blocks and ask for input
def game_intro(g1, g2, g3, g4, g5, g6):
    guesses = [' '.join(g1), ' '.join(g2), ' '.join(g3), ' '.join(g4), ' '.join(g5), ' '.join(g6)]

    print('\nW O R D L E')
    for guess in guesses:
        print(guess)
        if guess.split() == word:
            print('\n' + Style.BRIGHT + 'You Win!')
            player_status = True
            break
    guesses.clear()
    
#changes color of letters in terminal
def letter_color(guess):
    i = 0
    for letter in current_guess:
        if '\x1b[32m' + letter == word[i]:
            guess.append(Fore.GREEN + letter)
        elif '\x1b[32m' + letter in word:
            guess.append(Fore.YELLOW + letter)
        else:
            guess.append(Fore.WHITE + letter)
        i += 1
        

game_intro(guess1, guess2, guess3, guess4, guess5, guess6)

while player_status != True:
    match guess_num:
        case 1:
            guess1.clear()
            current_guess = input().lower()
            while current_guess not in word_list:
                current_guess = input('invalid\n').lower()
            current_guess = list(current_guess.upper())
            letter_color(guess1)
        
        case 2:
            guess2.clear()
            current_guess = input().lower()
            while current_guess not in word_list:
                current_guess = input('invalid\n').lower()
            current_guess = list(current_guess.upper())
            letter_color(guess2)

        case 3:
            guess3.clear()
            current_guess = input().lower()
            while current_guess not in word_list:
                current_guess = input('invalid\n').lower()
            current_guess = list(current_guess.upper())
            letter_color(guess3)
        
        case 4:
            guess4.clear()
            current_guess = input().lower()
            while current_guess not in word_list:
                current_guess = input('invalid\n').lower()
            current_guess = list(current_guess.upper())
            letter_color(guess4)
        
        case 5:
            guess5.clear()
            current_guess = input().lower()
            while current_guess not in word_list:
                current_guess = input('invalid\n').lower()
            current_guess = list(current_guess.upper())
            letter_color(guess5)

        case 6:
            guess6.clear()
            current_guess = input().lower()
            while current_guess not in word_list:
                current_guess = input('invalid\n').lower()
            current_guess = list(current_guess.upper())
            letter_color(guess6)
        
        case 7:
            print('\n' + Style.BRIGHT + 'Game Over!\n')
            print(f'The word was {' '.join(word)}')
            break
    
    game_intro(guess1, guess2, guess3, guess4, guess5, guess6)
    guess_num += 1
