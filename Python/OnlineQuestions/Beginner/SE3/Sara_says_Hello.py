

"""
Programming Practice: Sarah says hello

Sarah has just learned to type and go online.
As she went online she decided to go into a chat and say hello.
Sara entered a word in the chat room. If it does, delete
some of the letters of the word that Sarah entered and leave
the last word hello, which means Sarah could say hello otherwise.

It is guaranteed that the entry is made up of only lowercase
English letters.
Sample input:
ahhellllloou

Sample output:
YES

Sample input:
hlelo
Sample output:
NO
"""


words = input()
words.lower()

List_words = list(words)

count = 0
for i in range(0, len(List_words)):

    if List_words[i] == 'h' and count == 0:
        count += 1

    elif List_words[i] == 'e' and count == 1:
        count += 1

    elif List_words[i] == 'l' and count == 2:
        count += 1

    elif List_words[i] == 'l' and count == 3:
        count += 1

    elif List_words[i] == 'o' and count == 4:
        count += 1
if count == 5:
    print('YES')
else:
    print('NO')

