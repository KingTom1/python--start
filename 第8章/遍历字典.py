user_0 = {'username':'efermi','first':'enrico','last':'fermi'}
# 字典属性key-value键值对，类似于java中的map
for key,value in user_0.items():
    print(key,value)
# 字典属性 keys()
for key in user_0.keys():
    print(key)

for value in user_0.values():
    print(value)

# 按顺序遍历字典中的所有键
for key in sorted(user_0.keys()):
    print(key)