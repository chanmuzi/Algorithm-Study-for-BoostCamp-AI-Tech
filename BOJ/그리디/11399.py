n = int(input())

time_list = sorted(list(map(int, input().split())))

sum = 0
temp = 0
for i in time_list:
    temp += i
    sum += temp

print(sum)