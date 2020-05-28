
i = 0
win = 0
lost = 0
draw = 0

while i != 30:
    points = int(input())
    if points == 3:
        win += 1
    elif points == 1:
        draw += 1
    else:
        lost += 1

    i += 1
print(win*3 + draw, win)
