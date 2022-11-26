# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors)  # разделителей не будет
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()
# exit()  # код дальше этой команды не будет запускаться

# Еще вот тоже самое
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
# тут не нужно вызывать закрытие файла