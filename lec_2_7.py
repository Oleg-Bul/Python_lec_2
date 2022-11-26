# Словари

dictonary = {}
dictonary = \
    {
        'up': 'Вверх',
        'left': 'Влево',
        'down': 'Вниз',
        'right': 'Вправо'
    }
print(dictonary)  # полностью словарь
print(dictonary['left'])  # отдельно конкретная запись

# Типы ключей могут отличаться

for k in dictonary.keys():
    print(k)  # печать ключей(те что слева)

for k in dictonary.values():
    print(k)  # печать значений(те что справа)