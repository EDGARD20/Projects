import csv
from statistics import mean


# def calculate_sorted_averages(input_file_name, output_file_name):
#     with open(output_file_name, mode='w', newline='') as file:
#         writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#
#         with open(input_file_name, mode='r') as filer:
#             reader = csv.reader(filer)
#             mean_list= []
#             for i in reader:
#                 Sum = []
#                 for num in range(1, len(i)):
#                     if i[num] == '':
#                         pass
#                     else:
#                         Sum.append(float(i[num]))
#                 mean_list.append(mean(Sum))
#         writer.writerow([mean(mean_list)])
#
#
# calculate_sorted_averages('writeData.csv', 'writeData2.csv')

import hashlib
import csv
import random
def hash_password_hack(input_file_name, output_file_name):
    dict_list = dict()
    dict_list2 = dict()
    with open(input_file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            encrypted = row[1]
            if encrypted in dict_list:
                dict_list2[row[0]] = dict_list.values()
            else:
                for i in range(0, 9999):
                    if hashlib.sha256(str(i).encode()).hexdigest() == encrypted:
                        dict_list[encrypted] = i
                        dict_list2[row[0]] = i
        for key, value in dict_list2.items():
            print(key, value)











hash_password_hack('Hash.csv', 'Password.csv')


#
# with open('randname.csv', mode='w',newline='') as  file:
#     writer =csv.writer(file)
#
#     pass_list = []
#     for i in range(0, 10):
#         num = random.randint(1000, 9999)
#         print(num)
#         writer.writerow([hashlib.sha256(str(num).encode()).hexdigest()])

'''2269
2458
5736
6586
4070
8176
6713
3024
4925
3509'''