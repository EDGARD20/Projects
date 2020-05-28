"""
Programming Practice: Meeting Nowruz
On the occasion of Eid Nowruz, three old friends want to meet.
 Azar Mehr, AzarGoon and Mehrain are going to meet at one point.
 The house of these three people is on the straight line (x axis).
  In general, they want to travel the shortest distance.
  Calculate x1 x2 x3 as the minimum distance these three
  have to travel to meet each other at one point.
  Please print it out without a decimal point if the integer is
  correct, as in the example below if you print 6.0 is false.

Notice that the distance is not the place they are going to meet.
Sample input:

6 9 10
Sample output:

4
"""

get_value = input().split()
get_value = list(map(int, get_value))
print(max(get_value)-min(get_value))
