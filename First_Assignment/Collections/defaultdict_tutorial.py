#module import
from collections import defaultdict
#input values
d = defaultdict(list)
n, m = map(int, input().split())
#  line should containing the i-indexed positions of the occurrences of the word separated by spaces. 
for i in range(n):
    d[input()].append(str(i + 1))
#printing the relative output for m lines
for j in range(m):
    print(' '.join(d[input()]) or -1)