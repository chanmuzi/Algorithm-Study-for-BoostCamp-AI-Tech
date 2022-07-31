from itertools import combinations
def solution(numbers):
    cases = list(combinations(numbers,2))
    answer = set()
    for i in cases:
        answer.add(sum(i))
    return sorted(list(answer))