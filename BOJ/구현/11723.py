import sys 

s = set()
n = int(input())
sub = set(str(x) for x in range(1,21))
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    if ' ' in temp:
        oper,num = temp.split()
    else: oper = temp    
        
    if oper == 'add':
        if num in s: continue
        else: s.add (num)
    elif oper == 'remove':
        s.discard(num)
    elif oper == 'check':
        if num in s:
            print(1)
        else: print(0)
    elif oper == 'toggle':
        if num in s:
            s.remove(num)
        else: s.add(num)
    elif oper == 'all':
        s = sub
    else: s = set()
