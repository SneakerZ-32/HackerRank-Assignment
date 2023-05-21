#Ordered Dictionary 
from collections import OrderedDict
#initiating the dictionary
order = OrderedDict()
#for loop to insert input values
for _ in range(int(input())):
    item_name, space, net_price = input().rpartition(' ')
    order[item_name] = order.get(item_name, 0) + int(net_price)
#updating
for item_name, net_price in order.items():
#print final result for stdout
    print(item_name, net_price)