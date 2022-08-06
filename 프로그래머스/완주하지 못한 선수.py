def solution(array, commands):
    answer = []
    for x in commands:
        a,b,c = x
        temp = sorted(array[a-1:b])[c-1]
        answer.append(temp)
    return answer