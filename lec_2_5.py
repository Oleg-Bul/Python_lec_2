# Для работ со стоками

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# Для работ с числами

def concatenatio(*params):
    res: int = 0
    for item in params:
        res += item
    return res

# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1'))            # a1
print(concatenatio(1, 2, 3, 4))             # TypeError

