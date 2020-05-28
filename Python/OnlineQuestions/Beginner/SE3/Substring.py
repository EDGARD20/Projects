"""
Coding Practice: Substring
Jahangir works for a computer company. Jahangir is going
to write a program that determines whether AB and BA can be
found in another thread, knowing that they overlap.
The order of AB and BA does not matter either.
That is, if the input is ABBA, the answer is YES.
If there is a BAAB entry then the answer is YES.
But if ABA input is NO or if ABHA input is NO again.
Can you help Globalize write this program?

Please print YES and NO exactly in capital letters on the output.
"""

words = input()
words = words.upper()

count_AB = 0
count_BA = 0
for i in words:
    if len(words) >= 2:
        if words[0] == 'A' and words[1] == 'B':
            count_AB += 1
            words = words[2:]
        elif words[0] == 'B' and words[1] == 'A':
            count_BA += 1
            words = words[2:]
        else:
            words = words[1:]
if count_AB == count_BA and count_BA > 0:
    print('YES')

else:
    print('NO')



