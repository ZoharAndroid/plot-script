#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/8 15:16

import matplotlib.pyplot as plt
import numpy as np
from utils import Utils

# 这是一个多个柱子并行的柱状图

# 读取的数据文件为：tx-rx.csv

# 读取数据
header, data = Utils.read_csv('tx-rx.csv')
name = header[1:]
xtick_label = data[0]
base_data = data[1]
art_data = data[2]
sail_data = data[3]
poptrie_data = data[4]

# 开始绘图
plt.figure(1, figsize=(3, 2.5), dpi=600)
plt.tight_layout()

ax = plt.subplot(111)
ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
bar_width = 0.2
bar1 = plt.bar([1, 2, 3, 4, 5], base_data, width=bar_width, edgecolor='black', color='#0c2c84')
bar2 = plt.bar([1 + bar_width, 2 + bar_width, 3 + bar_width, 4 + bar_width, 5 + bar_width], \
               art_data, width=bar_width, edgecolor='black', color='#41b6c4', hatch='o')
bar3 = plt.bar([1 + bar_width * 2, 2 + bar_width * 2, 3 + bar_width * 2, 4 + bar_width * 2, 5 + bar_width * 2], \
               sail_data, width=bar_width, edgecolor='black', color='#c7e9b4', )
bar4 = plt.bar([1 + bar_width * 3, 2 + bar_width * 3, 3 + bar_width * 3, 4 + bar_width * 3, 5 + bar_width * 3], \
               poptrie_data, width=bar_width, edgecolor='black', color='#ffffd9', hatch='\\')
plt.xticks([1 + bar_width * 1.5, 2 + bar_width * 1.5, 3 + bar_width * 1.5, 4 + bar_width * 1.5, 5 + bar_width * 1.5],
           xtick_label, fontproperties='Times New Roman', size=16)
font = {'family': 'Times New Roman', 'size': 16}
plt.xlabel('packet size(Byte)', font)
plt.ylim(0,45)
plt.yticks(np.arange(0, 50, 10), np.arange(0, 50, 10), fontproperties='Times New Roman', size=16)
plt.ylabel('speed(Gbps)', font)
plt.grid(axis='y', color='black', linewidth=0.5, linestyle='--')
font = {'family': 'Times New Roman', 'size': 12}
plt.legend([bar1, bar2, bar3, bar4], ['Baseline', 'Art', 'Sail', 'Poptrie'], loc='upper center',
           bbox_to_anchor=(0.4, 1.2), ncol=4, prop=font, frameon=False, columnspacing=0.26, handlelength=1.5,
           handletextpad=0.1)

plt.savefig('result/example6.pdf', dpi=600, bbox_inches='tight')  # 保存为pdf文件
plt.savefig('example-picture/example6.png', dpi=600, bbox_inches='tight')  # 保存为png文件
