with open('input.txt', 'r') as file:
    data = file.readlines()

list1 = []
list2 = []

for line in data:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

score = 0

for num in list1:
    appear = list2.count(num)
    score += num*appear

print(score)

