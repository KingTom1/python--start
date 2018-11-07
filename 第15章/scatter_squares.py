import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# 传参c表示 添加线条颜色； edgecolors表示去边轮廓
plt.scatter(x_values,y_values,c = 'red',edgecolors='none',s=200)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis='both',which = 'major',labelsize = 14)
plt.axis([0,1100,0,1100000])
plt.show()
