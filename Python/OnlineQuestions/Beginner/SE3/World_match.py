
"""
Programming Practice: Liver World Championships
The liver federation is preparing teams to participate in
the World Liverpool Championships. Under the rules of the
World Liverpool Competition, only one person can participate
in the World Liverpool Competition. The head of the federation
has brought together all the athletes in the field, with
each player taking part in a number of world championships to
date. Liver teams consist of exactly 4 people. Now, the
president of the federation, Shaygan Ariyamar, wants to form
teams that, if elected, can compete for at least three years
in a world tournament (ie, each team member has participated
in the world championship up to 5 times). )

The first line of input contains the number n, which means the
number of liver players. The next entry line contains n
numbers separated by space, indicating that each player has
participated in the World Championships several times.
In the output, print a number that represents the maximum number
of teams formed with the conditions stated.


Sample input:

6
5 0 4 2 1 0
Sample output:

1
At the given input, players who have played 5 and 4 games cannot be in the group as a question, so only 4 players who have played 0, 2, 1 and 0 can be in the group. With 4 people only one group of 3 can be formed. Note that you do not need to calculate the number of modes (permutations).
"""
number_player = int(input())
get_num_played = input().split()
get_num_played = list(map(int, get_num_played))

new_list_num_played =[]
if number_player == len(get_num_played):
    for x in get_num_played:
        if x+2 < 5:
            new_list_num_played.append(x)
    print(int(len(new_list_num_played)/3))
