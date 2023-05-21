if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #make a register
    register = student_marks[query_name]
    #compute the sum
    score_sum = 0.00
    for score in register:
        score_sum += score
    #divide sum by elements 
    #there is something wrong with hackerrank and not recognizing that 56.0 is the same as 56.00 (found "%.2f" the solution online have no idea what it means)      
    score_mean = score_sum / len(register)
    print("%.2f"%score_mean) 
#it worked
