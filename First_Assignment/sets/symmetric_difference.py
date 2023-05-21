#using the imput
input()
#using split() to get the separate values in the form of a list. 
m = set(map(int,input().split()))
input()

n = set(map(int,input().split()))
#using sorted to print only values that are not present in both
print(*sorted(m^n), sep="\n")