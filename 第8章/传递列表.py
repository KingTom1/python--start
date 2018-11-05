def greet_users(names):
    "向列表中的每位用户都发出简单的问候"
    for name in names:
        msg = "Hello,"+name.title()+"!"
        print(msg)

usernames =  ['hannah','tY','margot']
greet_users(usernames)

# str.title() 意思是将字符串转成'标题化'类型 即 首字母都是大写开始，小写结束


## 在函数中修改列表
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
### 模拟打印每个设计，直到没有未打印的设计为止
### 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # print('Printing model:'+current_design)
    completed_models.append(current_design)
### 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# 此时unprinted_designs被pop取完了值，为空。。在‘禁止函数修改列表中’可解决不让其为空的问题
print(unprinted_designs)

