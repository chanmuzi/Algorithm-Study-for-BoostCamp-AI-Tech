import sys

n = int(sys.stdin.readline())

weight = []
for i in range(n):
    weight.append(int(sys.stdin.readline().rstrip()))

weight.sort()
top = 0
for i in range(n):
    if weight[i] * (n-i) > top:
        top = weight[i] * (n-i)

print(top)