age = []
while 1:
    age_input = int(input())
    if age_input != -1:
       age.append(age_input)
    else:
        break
age_max = max(age)
age.remove(age_max)
print(age_max,max((age)))
