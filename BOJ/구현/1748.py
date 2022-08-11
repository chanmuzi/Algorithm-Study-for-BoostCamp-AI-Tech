n = int(input())
result = 0
# 리스트로 변환
num_list = list(str(n))
length = len(num_list)

# 길이가 1이면 그냥 곱하기
if length == 1:
    print(num_list[0])
else:
    # 최대 숫자
    large = int(''.join(num_list))
    # 10의 자릿수-1 제곱
    cnt = large - 10**(length-1) + 1
    
    # 결과에 최대 숫자 먼저 계산
    result = 0
    result += cnt * length

    # 나머지 자리 계산
    for i in range(length-1,0,-1):
        temp = 10**i - 10**(i-1)
        result += temp * i
    print(result)