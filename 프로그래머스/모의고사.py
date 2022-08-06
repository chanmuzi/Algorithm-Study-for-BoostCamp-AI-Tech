def solution(answers):
    a = len(answers)
    
    one = [1,2,3,4,5] * (a//5) + [1,2,3,4,5][:a%5]
    two = [2,1,2,3,2,4,2,5] * (a//8) + [2,1,2,3,2,4,2,5][:a%8]
    three = [3,3,1,1,2,2,4,4,5,5] * (a//10) + [3,3,1,1,2,2,4,4,5,5][:a%10]
    
    count = [0, 0, 0]
    for i in range(a):
        if one[i] == answers[i]: count[0] += 1
        if two[i] == answers[i]: count[1] += 1
        if three[i] == answers[i]: count[2] += 1
        
    answer = []
    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)
    return answer
    
        
        