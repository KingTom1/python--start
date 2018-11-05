filename = 'programming.txt'

# open()文件时，如果文件不存在，open会报错，必须增加参数w,则会自动创建新文件
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
