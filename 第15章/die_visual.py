from 第15章.die import Die

die = Die()

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

frequencies = []
# range(1,7)表示包括1在内，不包括7，的之间的整数数组
for value in range(1,7):
    frequencie = results.count(value)
    frequencies.append(frequencie)

import pygal

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg') #svg文件 右键选择 使用浏览器打开