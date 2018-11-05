## 一次性读取
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

## 逐行读取  restrip是去除读取末尾时返回的一个空字符串，避免显示时换行
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

