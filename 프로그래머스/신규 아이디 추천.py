def solution(new_id):
    special = ['-','_','.']
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    temp = ''
    for i in range(len(new_id)):
        if new_id[i].isdigit() or new_id[i].isalpha() or new_id[i] in special:
            temp += new_id[i]
        else: continue
    new_id = temp
    
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    # 4단계
    if new_id[0] == '.' and len(new_id) != 1:
        new_id = new_id[1:]
    if len(new_id) != 1 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if new_id[0] == '.' and len(new_id) == 1:
        new_id = ''
      
    # 5단계
    if new_id == "":
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:14]

    # 7단계
    if len(new_id) == 1:
        new_id = new_id * 3
    elif len(new_id) == 2:
        new_id = new_id + new_id[-1]
    
    return new_id