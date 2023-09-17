import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)
mpl.rcParams["font.sans-serif"] = ["KaiTi"]
mpl.rcParams["axes.unicode_minus"] = False


x = np.arange(5)
y1 = [4206, 5103, 4808, 4594, 6019]
y2 = [5752, 5847, 5647, 5956, 7480]


total_width, n = 0.7, 5
width = total_width / n
x = x - (total_width - width) / 2
fig = plt.figure(figsize=(10, 6))

plt.bar(x, y1, width=width, color='#60ACFC', label='上海')
plt.bar(x + width, y2, width=width, color='#FF7C7C', label='北京')


plt.xticks((0,1, 2, 3, 4), ('2017', '2018', '2019', '2020', '2021'))

plt.xlabel("年份")

plt.ylabel("价格（单位：千元）")
plt.title("上海与北京造船板价格对比")
plt.legend()
fig.savefig('造船板价格比较.jpg', dpi=1000)

plt.show()

