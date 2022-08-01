s = input()

# 문자열을 변환할 딕셔너리 생성
cro_dict = {'c=':'0', 'c-':'1', 'dz=':'2', 'd-':'3',
            'lj':'4', 'nj':'5', 's=':'6', 'z=':'7' }

# 크로아티아 문자열을
for i in cro_dict:
    # 숫자로 대체
    s = s.replace(i,cro_dict[i])
# 문자열 길이 출력    
print(len(s))