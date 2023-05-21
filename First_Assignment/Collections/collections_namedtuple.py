#making tuples into containers
N, headers, total = int(input()), list(input().split()), 0
#for loop for _ separated values 
for _ in range(N):
    total += int(list(input().split())[headers.index('Mark')])
#printing the mean
print(total/N)