def solution(n):
    # 3진법 숫자를 담을 리스트 초기화
    three_list = list()
    # n이 0이 될 때까지
    while n:
        # n을 3으로 나눈 나머지를 리스트에 추가
        three_list.append(str(n%3))
        # n은 3으로 나눈 몫
        n //= 3
    # 리스트를 문자열로 변환    
    reverse_three = ''.join(three_list)
    # 문자열을 3진법으로 인식하여 10진법으로 반환
    return int(reverse_three, 3)
