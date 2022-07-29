n = int(input())
count = 0
for i in range(n):
    s = input()
    temp = sorted(s)
    str_list = []
    if len(s) == 1 or len(s) == 2: count+=1
    elif len(s) == 3:
        if s[0] != s[1] and s[0] == s[2]: continue
    else:
        for i in range(len(temp)-1):
            if temp[i] != temp[i+1]:
                str_list.append(temp[i])
        if temp[-1] != temp[-2]: str_list.append(temp[-1])
        if len(str_list) == len(set(s)): count+=1
        
print(count)
#     test = []
#     for i in range(len(s)-1):
#         if s[i] != s[i+1] and s[i] not in test:
#             test.append(s[i])
#         print(test)
#     if len(s) >= 2 and s[-1] != s[-2]: test.append(s[-1])
#     if len(test) != set(s): count += 1
# print(count)