n,k = map(int,input().split())
num = k-1
queue = [x for x in range(1,n+1)]

answer = []
while queue:
    target = queue[num]
    queue.remove(target)
    answer.append(target)
    if len(queue) == 0: break
    
    num = (num + k - 1) % len(queue)

print('<',end='')
for i in range(n-1):
    print(f'{answer[i]}, ', end='')
print(answer[n-1],end='')
print('>')