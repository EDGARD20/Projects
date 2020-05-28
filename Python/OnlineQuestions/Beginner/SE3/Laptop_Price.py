num_laptop = int(input())

compare_quality = []
for i in range(0, num_laptop):
    get_quality = input().split()
    get_quality = list(map(int, get_quality))
    compare_quality.append(get_quality)


def extract_first(lst):
    return [item[0] for item in lst]


def extract_second(lst):
    return [item[1] for item in lst]


laptops_price = extract_first(compare_quality)
laptops_quality = extract_second(compare_quality)
min_laptop_price = laptops_price.index(min(laptops_price))
max_laptop_quality = laptops_quality.index(max(laptops_quality))
if min_laptop_price <= max_laptop_quality:
    print('happy irsa')
else:
    print('poor irsa')

