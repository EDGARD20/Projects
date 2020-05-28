
num = int(input())
get_list = []
for i in range(0, num):
    p = input()
    words = p.split(' ')
    get_list.extend(words)

print("Action : ", get_list.count("Action"))
print("Comedy : ", get_list.count("Comedy"))
print("History : ", get_list.count("History"))
print("Horror : ", get_list.count("Horror"))
print("Romance : ", get_list.count("Romance"))
print("Adventure : ", get_list.count("Adventure"))