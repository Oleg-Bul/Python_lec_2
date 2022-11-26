list1 = [1, 2, 3, 4, 5]
list2 = list1
for e in list1:
    print(e)
print()

for e in list2:
    print(e)
print()

list1[0] = 123  # Значения поменяются в обоих списках
list2[1] = 333  # Тоже поменяет оба значения
for e in list1:
    print(e)
print()

for e in list2:
    print(e)