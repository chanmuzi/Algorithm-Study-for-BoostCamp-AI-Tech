def solution(left, right):
    return sum([x if x**0.5 != int(x**0.5) else -x for x in range(left,right+1)])