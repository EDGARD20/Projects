
num = int(input())
get_list = []
man = []
women = []
for i in range(0, num):
    p = input().lower()
    words = p.split('.')
    if words[0] == 'm':
        man.append(words)
    if words[0] == 'f':
        women.append(words)

man.sort(key=lambda x: x[1])
women.sort(key=lambda x: x[1])
k = 0
for i in range(0, len(man)):
    man[i][1] = man[i][1].capitalize()
    if man[i][2] == 'c++' or man[i][2] == 'c':
        man[i][2] = man[i][2].capitalize()

for j in range(0, len(women)):
    women[j][1] = women[j][1].capitalize()
    if women[j][2] == 'c++' or women[j][2] == 'c':
        women[j][2] = women[j][2].capitalize()
k =0
for i in women:
    print(' '.join(women[k]))
    k += 1
k =0
for i in man:
    print(' '.join(man[k]))
    k += 1
