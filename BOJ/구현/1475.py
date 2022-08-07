n = list(input())
numbers = [0]*10

for i in n:
    numbers[int(i)] += 1

six_nine = numbers[6] + numbers[9]
if six_nine % 2 == 0:
    six_nine = six_nine // 2
else:
    six_nine = six_nine // 2 + 1

numbers[6] = 0
numbers[9] = 0
if max(numbers) > six_nine:
    print(max(numbers))
else: print(six_nine)
