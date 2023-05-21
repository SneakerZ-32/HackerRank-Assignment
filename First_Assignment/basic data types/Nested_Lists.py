if __name__ == '__main__':
    #initiate empty list
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score]) #append values
    #find the lowest value for score    
    lowest_score = min(score for name,score in records)
    
    for name,score in records:
        records.sort()
        for name,score in records: #remove the lowest score to find the second lowest
            if (score == lowest_score):   
                records.remove([name,score])
                
    #find the second lowest the sam eway as before        
    second_lowest = min(score for name,score in records)
    # find the corresponding names for the lowest score and print
    for name,score in records:
        if (score == second_lowest):
            print(name)