
"""
Coding Practice: lowercase uppercase letters
Aryamesh (also called Darius' son) is so upset
that in the internet people use capital letters when they
write a word. So he decided to write a browser to write words
that have both lowercase and uppercase letters, so that if a
word had its uppercase letters exceed its lowercase,
the whole word would have been written in non-upper case letters.
It will write the whole word in lowercase.

Sample input:

hasTAM
Sample output:
hastam
"""
words = input()


count_lower = 0
count_upper = 0
for i in words:
    if i.islower():
        count_lower += 1
    elif i.isupper():
        count_upper += 1

if count_lower >= count_upper:
    print(words.lower())
elif count_upper > count_lower:
    print(words.upper())
