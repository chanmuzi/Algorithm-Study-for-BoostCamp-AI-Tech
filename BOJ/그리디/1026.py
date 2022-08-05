n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

c = sum([a[x]*b[x] for x in range(n)])
print(c)