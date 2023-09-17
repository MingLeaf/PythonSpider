# -*- coding:utf-8 -*-
import os
import sys
import matplotlib
import matplotlib.pyplot as plt


path = sys.argv[0]
pos = path.rfind('/')
if pos >= 0:
    path = path[:pos]
    os.chdir(path)

matplotlib.rcParams['font.sans-serif'] = ['KaiTi'] 
# x_data=[]
# y_data=[]
# data = xlrd.open_workbook('C:\\Users\\86133\\Desktop\\Python\\例题文件py\\average.xlsx')
# table=data.sheets()[0]
# x_data = list(range(5))
# cap = table.row_values(1)



# plt.plot(x_data,y_data,c='red',alpha=0.6)
# filename='average.csv'
# with open(filename) as f:
#     reader=csv.reader(f)
#     header_row=next(reader)

#     years,prices=[],[]
#     for line in reader:
#         year=int(row[1])
#         years.append(year)

#         price=float(row[3])
#         prices.append(price)

x = [2017, 2018, 2019, 2020,2021]
y1 = [3449, 6160, 6060, 6100, 6020]
y2 = [4206, 6410, 6476, 5680, 6950]
y3 = [3047, 5900, 6655, 7100, 7700]
y4 = [3817, 3790, 3960, 5090, 5510]
y5 = [3783, 3823, 4046, 4847, 6230]
plt.plot(x, y1, marker='.', ms=10, label="H型钢")
plt.plot(x, y2, marker='.', ms=10, label="造船板")
plt.plot(x, y3, marker='.', ms=10, label="热轧带钢")
plt.plot(x, y4, marker='.', ms=10, label="花纹板")
plt.plot(x, y5, marker='.', ms=10, label="中厚板")

    # fig=plt.figure(dpi=128,figsize=(8,6))
    # plt.plot(years,prices,c='red',alpha=0.6)


plt.xticks(x,rotation=0)
plt.xlabel("年份")
plt.ylabel("该钢材价格（单位：千元)")
plt.title("上海钢材价格比较")
plt.legend(loc="upper left")
# plt.fill_between(x,y1,facecolor='blue',alpha=0.1)

for y in [y1, y2, y3, y4, y5]:
    for x1, yy in zip(x, y):
        plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=10, rotation=0)

plt.savefig("SH.jpg")
plt.show()
