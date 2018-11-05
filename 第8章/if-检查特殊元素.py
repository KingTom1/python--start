# for 循环
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print("Adding" + requested_topping + ".")

print("\nFinished making your pizza!")

# if确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding"+requested_topping+".")
    print("\nFinished making your pizza")
else:
    print("Are your sure you want a plain pizza")

# P79练习  以特殊方式跟管理员打招呼 :创建一个至少包含5个用户名的列表，且其中一个用户名为admin，想象你要编写代码，在每位用户登录网址后都打印一条问候消息。
customers = ['Tom','John','Jessie','Kelly','Admin']
customers = [item.lower() for item in customers]
customer = input("请输入用户名：")
if customer == 'admin':
    print("Hello admin,would you like to see a status report? ")
elif customer.lower() in customers:
    print("Hello\t"+customer+"!\twelcome YuQiCompany")
else:
    print("We not have this customer")

