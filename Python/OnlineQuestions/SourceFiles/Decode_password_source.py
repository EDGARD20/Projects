import hashlib
import csv


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
    with open(output_file_name, mode='w', newline='') as wfile:
        writer = csv.writer(wfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        for key, value in dict_list2.items():
            writer.writerow([key, value])


