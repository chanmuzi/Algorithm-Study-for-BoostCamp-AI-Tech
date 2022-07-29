def solution(dartResult):
    converted = dartResult.replace('10','a')
    bonus = {'S':1,'D':2,'T':3}
    
    num_list = list()
    bonus_list = list()
    option_list = [0]*3
    for i in converted:
        if i.isdigit(): num_list.append(int(i))
        elif i == 'a': num_list.append(10)
        elif i in bonus: bonus_list.append(i)
        else:
            if len(num_list) == 1: option_list[0]=i
            elif len(num_list) == 2: option_list[1]=i
            else: option_list[2]=i
    num1 = num_list[0]**bonus[bonus_list[0]]
    num2 = num_list[1]**bonus[bonus_list[1]]
    num3 = num_list[2]**bonus[bonus_list[2]]
    num_answer = [num1,num2,num3]
    print(option_list)
    print(num_answer)
    for i in range(3):
        if option_list[i] == '#':
            num_answer[i] = -(num_answer[i])
        elif i==0 and option_list[i] == '*' :
            num_answer[i] = 2*num_answer[i]
        elif option_list[i] == '*':
            num_answer[i-1] = 2*num_answer[i-1]
            num_answer[i] = 2*num_answer[i]
        
    return sum(num_answer)