#for input
arr = []
#change object type to use sort function
new_arr = list(set(arr))
#using the sort function and printing the highest score
new_arr.sort(reverse = True)
print (new_arr[1])