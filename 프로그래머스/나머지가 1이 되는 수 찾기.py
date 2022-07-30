def solution(n):
    return min([x for x in range(1,n) if n % x == 1])