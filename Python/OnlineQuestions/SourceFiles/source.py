import csv

# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(output_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        with open(input_file_name, mode='r') as filer:
            reader = csv.reader(filer)
            for i in reader:
                Sum = []
                for num in range(1, len(i)):
                    if i[num] == '':
                        pass
                    else:
                        Sum.append(float(i[num]))
                meanSum = mean(Sum)
                writer.writerow([i[0], meanSum])



def calculate_sorted_averages(input_file_name, output_file_name):
    avg_list = []
    with open(input_file_name, mode='r') as filer:
        reader = csv.reader(filer)
        for i in reader:
            Sum = []
            for num in range(1, len(i)):
                if i[num] == '':
                    pass
                else:
                    Sum.append(float(i[num]))
            meanSum = mean(Sum)
            avg_list.append([i[0], meanSum])

        sorted_list = sorted(avg_list, key=lambda x: float(x[1]), reverse=False)
        counter_end = len(sorted_list) - 1

        for i in range(0, counter_end):
            for j in range(1, counter_end):
                new_list = []
                if sorted_list[i][1] == sorted_list[j][1]:
                    new_list.append([sorted_list[i][0], sorted_list[j][0]])
                    new_list.sort()
                    sorted_list[i] = [new_list[0][1], sorted_list[i][1]]
                    sorted_list[j] = [new_list[0][0], sorted_list[j][1]]

        with open(output_file_name, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for row in sorted_list:
                writer.writerow(row)


def calculate_three_best(input_file_name, output_file_name):
    avg_list = []
    with open(input_file_name, mode='r') as filer:
        reader = csv.reader(filer)
        for i in reader:
            Sum = []
            for num in range(1, len(i)):
                if i[num] == '':
                    pass
                else:
                    Sum.append(float(i[num]))
            meanSum = mean(Sum)
            avg_list.append([i[0], meanSum])

        sorted_list = sorted(avg_list, key=lambda x: float(x[1]), reverse=True)
        counter_end = len(sorted_list) - 1

        for i in range(0, counter_end):
            for j in range(1, counter_end):
                new_list = []
                if sorted_list[i][1] == sorted_list[j][1]:
                    new_list.append([sorted_list[i][0], sorted_list[j][0]])
                    new_list.sort()
                    sorted_list[i] = [new_list[0][1], sorted_list[i][1]]
                    sorted_list[j] = [new_list[0][0], sorted_list[j][1]]
    with open(output_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in range(0, 3, 1):
            writer.writerow(sorted_list[row])


def calculate_three_worst(input_file_name, output_file_name):
    avg_list = []
    with open(input_file_name, mode='r') as filer:
        reader = csv.reader(filer)
        for i in reader:
            Sum = []
            for num in range(1, len(i)):
                if i[num] == '':
                    pass
                else:
                    Sum.append(float(i[num]))
            meanSum = mean(Sum)
            avg_list.append([i[0], meanSum])

        sorted_list = sorted(avg_list, key=lambda x: float(x[1]), reverse=False)
        counter_end = len(sorted_list) - 1

        for i in range(0, counter_end):
            for j in range(1, counter_end):
                new_list = []
                if sorted_list[i][1] == sorted_list[j][1]:
                    new_list.append([sorted_list[i][0], sorted_list[j][0]])
                    new_list.sort()
                    sorted_list[i] = [new_list[0][1], sorted_list[i][1]]
                    sorted_list[j] = [new_list[0][0], sorted_list[j][1]]
    with open(output_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in range(0, 3, 1):
            writer.writerow([sorted_list[row][1]])


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(output_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        with open(input_file_name, mode='r') as filer:
            reader = csv.reader(filer)
            mean_list = []
            for i in reader:
                Sum = []
                for num in range(1, len(i)):
                    if i[num] == '':
                        pass
                    else:
                        Sum.append(float(i[num]))
                mean_list.append(mean(Sum))
        writer.writerow([mean(mean_list)])

#
# try:
#     calculate_averages('writeData.csv', 'writeData1.csv')
#     calculate_sorted_averages('writeData.csv', 'writeData2.csv')
#     calculate_three_best('writeData.csv', 'writeData3.csv')
#     calculate_three_worst('writeData.csv', 'writeData4.csv')
#     calculate_average_of_averages('writeData.csv', 'writeData5.csv')
# except KeyboardInterrupt:
#     print('End')
