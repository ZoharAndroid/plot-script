#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/7 12:21
from utils import Utils
import matplotlib.pyplot as plt

# 这是一个折线图

# 读取csv文件中的内容
header, data = Utils.read_csv('all_loc512_normal.csv')

# 从读取的csv文件中分别获取不同类别的数据
locality = data[0]
art = data[1]
sail = data[2]
poptrie = data[3]

plt.figure(num=1, figsize=(3, 2.5), dpi=600)
ax = plt.subplot(111)
ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

line1 = plt.plot(art, label=str(header[1]).capitalize(), color="black", linewidth=2)
line2 = plt.plot(sail, label=str(header[2]).capitalize(), color='black', linestyle='--', linewidth=2)
line3 = plt.plot(poptrie, label=str(header[3]).capitalize(), color='olive', marker='x', markersize=10, linewidth=2)

font = {'family': 'Times New Roman', 'size': 20}
plt.xlabel('locality', font)
plt.ylabel('speed(Mpps)', font)

plt.xticks([0, 3, 6, 9], [1, 8, 64, 512], fontproperties='Times New Roman', size=16)
plt.ylim(200, 820);
plt.yticks(range(200, 1000, 200), fontproperties='Times New Roman', size=16)

plt.grid(axis='y', color='black', linewidth=0.5, linestyle='--')

font = {'family': 'Times New Roman', 'size': 16}
plt.legend(loc='upper left', frameon=False, ncol=2, labelspacing=0.1, columnspacing=0.1, handlelength=2,
           handletextpad=0.5, borderaxespad=0.01, prop=font)

plt.savefig('result/example.pdf', dpi=600, bbox_inches='tight')
plt.savefig('example-picture/example.png',dpi=600,bbox_inches='tight') # 保存为png文件
# plt.show()
