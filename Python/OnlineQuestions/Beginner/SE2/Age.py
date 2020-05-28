
"""
Programming Practice: Finding the Biggest Registrant for
the Parliament Write a program that reads the age of Majlis
candidates from the entrance and prints the oldest of
them at the outlet. Your program will continue to read from the
input until the negative number of one is entered.
As soon as the number appears on the input, the program must
terminate the input reading and print the oldest age.
The age range is between 1 and 2 years.
Sample input:
17
15
39
51
14
32
28
-1
Sample output:
51
"""
age = []
while 1:
    age_input = int(input())
    if age_input != -1:
        age.append(age_input)
    else:
        break

print(max(age))
