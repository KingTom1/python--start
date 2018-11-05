import 类 as c

# pyhton中跟java有区别就是，一个文件中可以有多个class，在调用类时用import引用点类名
# python中继承是将java中extend 省略，将父类写入到子类class括号中
class Electric(c.Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

my_tesla = Electric('tesla','model','2016')
print(my_tesla.get_descriptive())


