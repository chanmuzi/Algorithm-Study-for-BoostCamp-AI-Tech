s = input()
my_list = list(s)
num_list = []
oper_list = []

temp = ''
for i in range(len(s)):
    if i == len(s)-1:
        temp += str(my_list[i])
        num_list.append(int(temp))
    elif my_list[i].isdigit():
        temp += str(my_list[i])    
    else:
        num_list.append(int(temp))
        temp = ''
        oper_list.append(my_list[i])

if '-' not in oper_list:
    print(sum(num_list))
else:            
    minus_point = oper_list.index('-')
    print(sum(num_list[:minus_point+1]) - sum(num_list[minus_point+1:]))