#importing the module
from itertools import combinations_with_replacement
# dividing the input with split command
s, n = input().split()
# one line to print the sorted combinations
print(*[''.join(i) for i in combinations_with_replacement(sorted(s), int(n))], sep="\n")