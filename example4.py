#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/8 11:33

import matplotlib.pyplot as plt
from utils import Utils
import numpy as np
import matplotlib

# 这是一个并行的柱形图例子
# 读取的文件为：cache-1-0.csv

# 读取文件
header, data = Utils.read_csv('cache-1-0.csv')
art_data = data[1]
sail_data = data[2]
poptrie_data = data[3]
wo_data = [art_data[0], sail_data[0], poptrie_data[0]]
w_data = [art_data[1], sail_data[1], poptrie_data[1]]

# 绘图
plt.figure(1, figsize=(3.2, 2), dpi=600)
ax = plt.subplot(111)
ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
bar_width = 0.2
bar1 = plt.bar([1, 2], art_data, width=bar_width, color='#fee6ce', edgecolor='black',linewidth=1)
bar2 = plt.bar([1 + bar_width, 2 + bar_width], sail_data, width=bar_width, color='#fdae6b',edgecolor='black',
               linewidth=1, hatch='/')
bar3 = plt.bar([1 + bar_width * 2, 2 + bar_width * 2], poptrie_data, width=bar_width, color='#e6550d',edgecolor='black',
               linewidth=1, hatch='\\')
plt.xticks([1 + bar_width, 2 + bar_width], ['w/o comp', 'w comp'], fontproperties='Times New Roman', size=16)
plt.ylim(10, 42)
plt.yticks(np.arange(10, 42, 10), fontproperties='Times New Roman', size=16)
plt.grid(axis='y', color='black', linewidth=0.5, linestyle='--')
font = {'family': 'Times New Roman', 'size': 13}
plt.ylabel('CPU cycle\n per packet', font)

font = {'family': 'Times New Roman', 'size': 12}
plt.legend([bar1, bar2, bar3], ['Art', 'Sail', 'Poptrie'], loc='upper left', bbox_to_anchor=(0, 1), ncol=1,
           frameon=False, prop=font, columnspacing=0.1, handlelength=1, handletextpad=0.1)
plt.savefig('result/example4.pdf', dpi=600, bbox_inches='tight')  # 保存为pdf文件
plt.savefig('example-picture/example4.png', dpi=600, bbox_inches='tight')  # 保存为png文件
