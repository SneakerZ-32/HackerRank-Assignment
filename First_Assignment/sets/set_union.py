#inputs
n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())
# defining the sets 
s1 = set(l)
s2 = set(k)
#printing results of only union between sets
print(len(s1.union(s2)))