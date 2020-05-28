number_of_sentences = int(input())
string_in0 = []
string_in = []
my_dict = dict()
for i in range(0, number_of_sentences):
    string_in0.append(input().split())
    string_in = string_in + string_in0[i]

sentence = input().split()

for i in range(0, len(string_in), 2):
    my_dict[string_in[i]] = string_in[i+1]


sentence_make = []
for i in range(len(sentence)):
    result = [val for key, val in my_dict.items() if sentence[i] in key]
    if result:
        sentence_make.append(result)
    else:
        txt = list(sentence[i])
        txt = [''.join(txt)]
        sentence_make.append(txt)

sentence_out = []
for i in range(len(sentence_make)):
    sentence_out = sentence_out + sentence_make[i]
str1 = " "

print(str1.join(sentence_out))