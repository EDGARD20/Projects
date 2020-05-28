
import csv, operator
from statistics import mean
# with open('writeData3.csv', mode='w', newline='') as file:
#     writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#
#     with open('writeData2.csv', mode='r') as filer:
#         reader = csv.reader(filer)
#         avg_list = []
#
#         for i in reader:
#             avg_list.append(float(i[1]))
#         print(avg_list)
#         print(min(avg_list))
#         print(max(avg_list))

with open('writeData3.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    with open('writeData2.csv', mode='r') as filer:
        reader = csv.reader(filer)
        sorted_list = sorted(reader, key=lambda x: float(x[1]), reverse=False)
        counter_end = len(sorted_list)-1
        counter = 0

        for i in range(0, counter_end):
            for j in range(1, counter_end):
                new_list = []
                if sorted_list[i][1] == sorted_list[j][1]:
                    new_list.append([sorted_list[i][0], sorted_list[j][0]])
                    new_list.sort()
                    sorted_list[i] = [new_list[0][1], sorted_list[i][1]]
                    sorted_list[j] = [new_list[0][0], sorted_list[j][1]]
        for row in sorted_list:
            print(row)
            writer.writerow(row)


