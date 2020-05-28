
"""
Programming Practice: Finding the Age of the Largest
Candidate and the Second Largest Candidate
Write a program that reads the age of the Majlis
candidates from the entrance and prints the age of the
eldest and the second largest in the output.
Your program will continue to read from the input until
the negative number of one is entered. As soon as the number
appears on the input, the program must terminate the input
reading and print the oldest age. The age range is between
1 and 2 years. Ensures that candidates are at the same entrance
(meaning no two people will be the same at the entrance)
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
51 39
Please note that in the output there are only two numbers that are separated by space. The first number is the largest age and the second is the second largest number.
"""

age = []
while 1:
    age_input = int(input())
    if age_input != -1:
        age.append(age_input)
    else:
        break
age_max = max(age)
age.remove(age_max)
print(age_max, max(age))
