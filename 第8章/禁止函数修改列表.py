# function_name(list_name[:])
# 切片表示法 [:] 创建列表的副本

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model:"+current_design)
        completed_models.append(current_design)

print_models(unprinted_designs[:],completed_models)

# 由于上面函数使用的是unprinted_designs的副本，所以pop之后自身然后有值。
print(unprinted_designs)