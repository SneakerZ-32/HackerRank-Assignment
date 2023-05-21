from collections import Counter

int(input())
#initiating variables and extrating form input
shoesize = list(map(int,input().split()))
earned_money = 0
stock = Counter(shoesize)
#making the dictionary
for i in range(int(input())):
    x,y = list(map(int,input().split()))
    #updating the dictionary
    if stock[x]:
        earned_money+=y
        stock[x]-=1
print(earned_money)