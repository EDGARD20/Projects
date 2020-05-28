
"""
Marian Programming: Summary of Sepidrood Rasht's Points
In this program you will get the score that Sepidrood Rasht
has earned in the Premier League and you will be adding the
total score of Sepidrood Rasht along with the number of wins
this season at the outlet. Sepidrod will play 2 Premier League
matches so you will be awarded 5 team points. The team has zero
points per game or zero or one or three points. The team gains
zero points if it loses, draws one, and wins three.
Sample input:
3
3
3
3
3
0
0
0
0
0
1
1
1
1
1
3
3
3
3
3
0
0
0
0
0
1
1
1
1
1
Sample output:
40 10
He has won 1 game and finished 2 games in a draw, then gets 2 to 3 points and 2 to 1 point with 2 points.
Please note that at the output of the two prints exactly that are separated by space.
"""
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
