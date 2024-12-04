with open('input.txt', 'r') as file:
    data = file.readlines()

list1 = []
list2 = []

for line in data:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

sum = 0

while list1 and list2:
    min1 = min(list1)
    min2 = min(list2)

    diff = abs(min1 - min2)
    sum += diff

    list1.remove(min1)
    list2.remove(min2)

print(sum)
