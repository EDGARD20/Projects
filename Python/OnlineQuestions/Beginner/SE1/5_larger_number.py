'''
Practice programming a larger number print
In this program you read two numbers from the input and
print a larger number at the output. The first line of
input contains the first number. The second line of input
contains the second number. Ensures that the input numbers
are positive integers. If two inputs are equal, print one.
Sample input
17
13
Sample output
17
'''
value1 = int(input())
value2 = int(input())

if value1 >= value2:
    print(value1)
elif value2 >= value1:
    print(value2)
