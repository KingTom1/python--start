# 面向对象编程

class Dog():
    '一次模拟小狗的简单尝试'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        '模拟小狗被命令下蹲'
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        '模拟小狗被命令打滚'
        print(self.name.title()+' rolled over!')

# my_dog = Dog('willie',6)
# print("My dog's name is "+my_dog.name.title()+".")
# print("My dog is "+str(my_dog.age)+" years old.")
# my_dog.sit()
# my_dog.roll_over()


class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive(self):
        long_name = str(self.year+''+self.make+''+self.model)
        return long_name.title()


