import math
number = int(input())
num_list = []
for i in range(0, number):
    num_list.append(math.sqrt(int(input())))

for i in num_list:
    print('{0:.4f}'.format(math.floor(i*10 ** 4) / 10 ** 4))

