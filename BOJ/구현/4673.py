test_list = [True]*10001

def solution(n):
    next_n = 0
    temp_n = str(n)
    for i in range(len(temp_n)):
        next_n += int(temp_n[i])
    next_n += n
    return next_n

for i in range(1,10001):
    if solution(i) <= 10000:
        test_list[solution(i)] = False

for i in range(1,10001):
    if test_list[i]: print(i)