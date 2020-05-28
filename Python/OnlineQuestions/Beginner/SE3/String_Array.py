
"""
Practice programming: Working with strings
The rookie has learned the discipline of strings.
There is a relatively simple question to get started
with the strings, but you need your help to do it.
The organizer should write a program that reads a letter
string from the input and makes the following changes to it.
4. Clear all vowels.
Make a dot before each silent letter.
Write all the remaining letters in lowercase.
(Are aeiou vowels)
Sample input:
aBAcAba
Sample output:
.b.c.b
"""
words = input()
# array_words = list(word)
seperator = ''

# array_words = word.replace('a' and 'e' and 'i' and 'o' and 'u','.')

vowel =list('aeiouAEIOU')
for i in range(0, len(vowel)):
    words = words.replace(vowel[i],'')

words = list(words.lower())

for i in range(0, len(words)):
    words[i] = '.' + words[i]

print(seperator.join(words))

