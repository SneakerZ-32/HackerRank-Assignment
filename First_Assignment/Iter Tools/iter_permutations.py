# importing module
from itertools import permutations
#inputting the values
s,n = input().split()
#using permutations of a for loop
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')