#importing the module
from itertools import combinations
#getting the inputs
s , n  = input().split()
#using the input for 2 for loops to get all possible combinations
for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        #subsequences of elements from the input
        print(''.join(j))