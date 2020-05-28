
Iran = [0, 0, 0, 0, 0, 'Iran']
Spain = [0, 0, 0, 0, 0, 'Spain']
Portugal = [0, 0, 0, 0, 0, 'Portugal']
Morocco = [0, 0, 0, 0, 0, 'Morocco']

GameList = [Iran, Spain, Iran, Portugal, Iran, Morocco, Spain, Portugal, Spain, Morocco, Portugal, Morocco]

gamePlayed = [3, 2, 1]
num = []
List_num = -1

for j in range(0, 6):
    for i in str(input()):
        if i.isdigit():
            num.append(int(i))
            List_num += 1
    if num[0] == num[1]:
        GameList[List_num-1][2] = GameList[List_num-1][2] + 1
        GameList[List_num][2] = GameList[List_num][2] + 1

        GameList[List_num-1][3] = GameList[List_num-1][2] - GameList[List_num-1][1]
        GameList[List_num][3] = GameList[List_num][2] - GameList[List_num][1]

        GameList[List_num-1][4] = GameList[List_num-1][0] * 5 - GameList[List_num-1][1]
        GameList[List_num][4] = GameList[List_num][0] * 5 - GameList[List_num][1]

        num = []

    elif num[0] > num[1]:
        GameList[List_num-1][0] = GameList[List_num-1][0] + 1
        GameList[List_num][1] = GameList[List_num][1] + 1

        GameList[List_num-1][3] = GameList[List_num-1][2] - GameList[List_num-1][1]
        GameList[List_num][3] = GameList[List_num][2] - GameList[List_num][1]

        GameList[List_num-1][4] = GameList[List_num-1][0] * 5 - GameList[List_num-1][1]
        GameList[List_num][4] = GameList[List_num][0] * 5 - GameList[List_num][1]
        num = []

    elif num[0] < num[1]:
        GameList[List_num-1][1] = GameList[List_num-1][1] + 1
        GameList[List_num][0] = GameList[List_num][0] + 1

        GameList[List_num-1][3] = GameList[List_num-1][2] - GameList[List_num-1][1]
        GameList[List_num][3] = GameList[List_num][2] - GameList[List_num][1]

        GameList[List_num-1][4] = GameList[List_num-1][0] * 5 - GameList[List_num-1][1]
        GameList[List_num][4] = GameList[List_num][0] * 5 - GameList[List_num][1]

        num = []

GameResult = [Iran, Spain, Portugal, Morocco]
temp_list = 0
temp_list2 = 0
j = -1
k = 0
for i in range(0,len(GameResult)-1):
    for j in range(0, len(GameResult)-i-1):
        if GameResult[j][4] < GameResult[j+1][4]:
            GameResult[j], GameResult[j+1] = GameResult[j+1], GameResult[j]
        elif GameResult[j][4] == GameResult[j+1][4]:
            if GameResult[j][1] < GameResult[j+1][1]:
                GameResult[j], GameResult[j + 1] = GameResult[j + 1], GameResult[j]
            else:
                pass
    else:
        pass

for i in GameResult:
    print("{name}  wins:{win} , loses:{lose} , draws:{dr} , goal difference:{gd} ,"
          " points:{pn}".format(name=i[5], win=i[0], lose=i[1], dr=i[2], gd=i[3], pn=i[4]))
