# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['KaiTi'] 
x = [2017, 2018, 2019, 2020,2021]
y1 = [3773, 3883, 3656, 3651, 5047]
y2 = [3956, 4141, 3851, 3794, 5403]
y3 = [4209, 4352, 4021, 3900, 5570]
y4 = [5752, 5847, 5647, 5956, 7480]
y5 = [3908, 4247, 3848, 3738, 5126]
plt.plot(x, y1, marker='.', ms=10, label="H型钢")
plt.plot(x, y2, marker='.', ms=10, label="热轧板卷")
plt.plot(x, y3, marker='.', ms=10, label="花纹板")
plt.plot(x, y4, marker='.', ms=10, label="彩涂板卷")
plt.plot(x, y5, marker='.', ms=10, label="中厚板")
plt.xticks(x,rotation=0)
plt.xlabel("年份")
plt.ylabel("该钢材价格（单位：千元)")
plt.title("北京钢材价格比较")
plt.legend(loc="upper left")

for y in [y1, y2, y3, y4, y5]:
    for x1, yy in zip(x, y):
        plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=10, rotation=0)

plt.savefig("BJ.jpg", dpi=1000)
plt.show()
