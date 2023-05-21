#using set methods as inputs
number_of_inputs = int(input())
string = set(map(int, input().split())) # Set of n elements
#for loop to check if input is a known 
for i in range(int(input())): # Iterate in range of the input num
    new_string = input().split()
    if new_string[0] == 'pop':
        string.pop()
    elif new_string[0] == 'remove':
        string.remove(int(new_string[1]))
    elif new_string[0] == 'discard':
        string.discard(int(new_string[1]))
#printing the  new string
print(sum(string))