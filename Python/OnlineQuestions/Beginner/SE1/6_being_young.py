'''
Programming Practice: Determining the user being young
by input age Write a program that receives a number of
inputs as the user ages and prints their age range.
If greater than zero and less than six years, khordsal output
If older than six years and less than ten years, koodak output
If older than 10 years and younger than 5 years nojavan output
If greater than 1 and less than 5 years javan output
Bozorgsal output if greater than 1 and less than 5 years
If older equals 1 year, miansal output

Please note that the output must have exactly the same
expressions. It is important to keep the words small.
Sample input
17
Sample output
javan

'''

value = int(input())
if 0 < value < 6:
    print("khordsal")
elif 6 <= value < 10:
    print("koodak")
elif 10<=value<14:
    print("nojavan")
elif 14<=value<24:
    print("javan")
elif 24<=value<40:
    print("bozorgsal")
elif 40<=value:
    print("miansal")
