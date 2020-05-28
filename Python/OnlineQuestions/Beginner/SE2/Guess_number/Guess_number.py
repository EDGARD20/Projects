"""
Project Guess the Numbers Game
The steps of the game are as follows:
The user first specifies a number in his mind and
does not tell the computer this number
(does not give the number as an input to the computer)
(numbers between 0 and 1)
We run the program
The program guesses and prints a number
The printed number creates three modes
8. Or is it larger than the number you have in mind
when you type in the letter k to say that the number
in your mind is smaller than the number printed on
the program and the program has to guess and display
another number and so on. (It should be noted that in this case,
by typing k the program must guess a smaller number than
its previous guess to finish the game sooner)
3. Or the printed number is smaller than the number you have
in mind when you say to the program with the letter b that
the number in your mind is larger than the number printed and
the program has to guess another number and Show and ...
(it should be noted that in this case, by typing b the program
must guess a larger number than its previous guess to finish the
game sooner)
3. Or the printed number is the number that you had in mind and
you type the letter d into the program, which is right guess and
the program ends
"""

import random


def user_answer():
    return input()


def pc_guess_value(num1):
    range_list = sorted(random.sample(range(num1), num1))
    range_list = range_list[1:]
    pc_guess = random.choice(range_list)
    print(pc_guess)
    return pc_guess, range_list


if __name__ == '__main__':
    count = 0
    value, List_value = pc_guess_value(100)
    user = user_answer()

    while user != 'd':
        if user == 'k':
            List_value = List_value[:List_value.index(value)]
            value = random.choice(List_value)
        elif user == 'b':
            List_value = List_value[List_value.index(value):]
            value = random.choice(List_value)
        print(value)
        user = user_answer()


