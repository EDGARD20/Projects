'''
Programming Practice: Calculate the Next Multiple Ten
Write a program that reads an integer to print the next first multiple of a larger one. For example, if 1 is read from the input, the number 1 should be printed. If number 1 is read, number 1 should be printed.
Input sample
34
Output Sample
40
'''


number = int(input())
next_ten_multiplicity = (10 - (number % 10)) + number
print (next_ten_multiplicity)


