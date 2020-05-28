
import numpy as np

world = input()
world = world.split(' ')

flag = False
tempFull = [[]]
m = 0
n = 0
for i in world:
    for j in i:
        if j == '.':
            flag = True
    if not flag:
        tempFull[n].append(i)
    if flag:
        tempFull[n].append(i.replace('.', ''))
        tempFull.append([])
        n += 1
        flag = False

start_sec = []
start_first = []
for i in tempFull:
    for j in range(1, len(i)):
        start_sec.append(i[j])

for i in tempFull:
    for j in range(0, len(i)):
        start_first.append(i[j])

upperCase_list = []
for i in start_sec:
    for j in i:
        if str(j).isupper():
            upperCase_list.append(i)
cnt = 1
cnt_lst = []
for i in start_first:
    for j in upperCase_list:
        if i == j:
            cnt_lst.append(cnt)
    cnt += 1
x = np.array(cnt_lst)
out_list = np.unique(x)
cnt = 0
for i in upperCase_list:
    print(str(out_list[cnt]) + ":" + str(i))
    cnt += 1


