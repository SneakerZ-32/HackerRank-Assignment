if __name__ == '__main__':
    #defining everything as integers
    n = int(input())
    #mapping every integer to it's value
    integer_list = map(int, input().split())

    my_tuple = tuple(integer_list)
    #using hash function to get a hash number
    print(hash(my_tuple))