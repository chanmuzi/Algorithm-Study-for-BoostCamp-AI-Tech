k = int(input())

queue= list()
for i in range(k):
    temp = int(input())
    if temp == 0:
        queue.pop()
    else: queue.append(temp)

print(sum(queue))