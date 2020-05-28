'''
Programming Practice: Calculates twice the number of Reverse
of a number. Write a program that reads a three-digit number
from the input and prints it twice of the Reverse in the output.
You can be sure that the input is a three-digit number.
For example, if the input at 765 is hit, print at output
567 * 2 ie 1134.
Sample input
765
Sample output
1134
'''

Reverse = 0
Number = int(input())
while Number > 0:
    Reminder = Number % 10
    Reverse = (Reverse * 10) + Reminder
    Number = Number // 10
print(Reverse * 2)

