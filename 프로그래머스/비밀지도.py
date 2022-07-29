def solution(n, arr1, arr2):
    binary_list1 = [[] for _ in range(n)]
    binary_list2 = [[] for _ in range(n)]
    for i in range(n):
        temp = arr1[i]
        for j in range(n):
            left = temp%2
            binary_list1[i].append(left)
            temp = temp // 2

    for i in range(n):
        temp = arr2[i]
        for j in range(n):
            left = temp%2
            binary_list2[i].append(left)
            temp = temp // 2
                
    
    answer = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n-1,-1,-1):
            if binary_list1[i][j] == 0 and binary_list2[i][j] == 0:
                answer[i].append(' ')
            else: answer[i].append('#')
    
    result = []
    for i in answer:
        temp = ''.join(i)
        result.append(temp)
    return result