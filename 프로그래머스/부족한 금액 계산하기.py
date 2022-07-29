def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        temp = i * price
        sum += temp
    if sum > money: return sum-money
    else: return 0
