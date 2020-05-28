array_words = input()
array_words = list(array_words)

for i in range(0, len(array_words)):
    if array_words[i] == 'a' and 'e' and 'i' and 'o' and 'u':
        array_words[i] = '.'
    elif array_words[i] == 'A' and 'E' and 'I' and 'O' and 'U':
        array_words[i] = '.'
    else:
        array_words[i] = array_words[i].lower()

seperator = ''
print(seperator.join(array_words))