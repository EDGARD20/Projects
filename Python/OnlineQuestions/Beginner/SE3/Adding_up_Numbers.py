"""
Programming Practice: Adding Numbers
Somayeh is in second grade at elementary school and is
just starting to learn the numbers. The teacher puts a
number on the board and the students have to count the numbers.
To make things easier, the numbers that need to be added are
just one, two, and three. But that's not enough, and the
student can only do the sum when the numbers are arranged in
descending order (ie, first one, then two, and then three).
And at the output of the phrase that was explained so Somayeh
and the other students could calculate it.
Sample input:
1 + 1 + 3 + 1 + 3
Sample output:
1 + 1 + 1 + 3 + 3
"""

array_number = input()
str_fin = []
list_number = []

array_number = array_number.replace('+', '')
array_number = list(array_number)

for i in range(0, len(array_number)):
    array_number[i] = int(array_number[i])

array_number.sort()
fin_list = [str(i) for i in array_number]

for i in range(0,len(fin_list)):
    str_fin.append(fin_list[i])
    str_fin.append('+')
separator = ''
print(separator.join(str_fin[:len(str_fin)-1]))

