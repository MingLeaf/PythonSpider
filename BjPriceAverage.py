#-*-coding:utf-8-*-
import os
import sys
import xlrd

path = sys.argv[0]
pos = path.rfind('/')
if pos >= 0:
    path = path[:pos]
    os.chdir(path)

def mean(list):
    sum = 0
    j = len(list)
    for i in list:
        sum = sum + int(i)
    return sum/j

list1 = []

worksheet = xlrd.open_workbook('C:\\Users\\86133\\Desktop\\Python\\例题文件py\\Bj21.xlsx')
sheet_names= worksheet.sheet_names()

for sheet_name in sheet_names:
    sheet = worksheet.sheet_by_name(sheet_name)
    cols = sheet.ncols 
    all_content = []
    for k in range(0,5):
        cols = sheet.col_values(k) 
        cols.pop(0)
        list1.append("{:.2f}".format(mean(cols)))
        

output = open('BJ average21.xlsx','w',encoding='gbk') 
output.write('H型钢\t热轧板卷\t花纹板\t彩涂板卷\t中厚板\n')
for i in range(len(list1)):  
    for j in range(len(list1[i])):   
        output.write(str(list1[i][j])) 
    output.write('\t') 
output.close()