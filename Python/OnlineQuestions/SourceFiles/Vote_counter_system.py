
import collections

number_of_vote = int(input())
vote = []

for i in range(0, number_of_vote):
    vote.append(input().lower())
vote.sort()

# print(vote)
counter = collections.OrderedDict()

for i in range(0, number_of_vote):
    # print(vote[i])
    counter[vote[i]] = counter.get(vote[i], 0) + 1

for this_one in list(counter.keys()):
    print('%s %s' % (this_one, counter[this_one]))
