
"""
Programming Practice: Standardizing Names
Mehdi is sending the final list of names to the
Fajr film closing ceremony for the executive committee
to print the entry cards. But there is a problem.
When registering, participants did not write their names
as standard. Standard means exactly the first letter of the
big name and the rest of the lowercase letters. Write a
program that reads 8 names from the input and prints them
standardized at the output.


Sample input:

BaHram
MaHnaZ
hooman
FaribORZ
barAN
HedieH
ALI
EZATOLLAH
MOHAMADALI
JAMSHID
Sample output:

Bahram
Mahnaz
Hooman
Fariborz
Baran
Hedieh
Ali
Ezatollah
Mohamadali
Jamshid
"""


def get_name():
    return input()


name_list = []
for i in range(0, 10):
    name = get_name()
    new_name = list(name.lower())
    first_word_new_name = str(new_name[0])
    new_name[0] = first_word_new_name.upper()
    separator = ''
    name_list.append(separator.join(new_name))

for i in range(0, 10):
    print(name_list[i])
