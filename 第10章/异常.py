# 处理ZeroDivisionError异常pring

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 处理FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
