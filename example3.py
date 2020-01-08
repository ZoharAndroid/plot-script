#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/8 0:08

import matplotlib.pyplot as plt
from utils import Utils
import matplotlib
import numpy as np

# 这是一个叠加的组装图例子

# 读取数据
# 这里从dates中读取的csv文件是：cache-1-w和
# cache-1-wo这两个文件
header, wo_data = Utils.read_csv('cache-1-wo.csv')
w_data = Utils.read_csv('cache-1-w.csv', only_data=True)
# 转换成各自算法的数据
wo_art = wo_data[1]
wo_sail = wo_data[2]
wo_poptrie = wo_data[3]
w_art = w_data[1]
w_sail = w_data[2]
w_poptrie = w_data[3]
wo_l1_data = [wo_art[0], wo_sail[0], wo_poptrie[0]]  # wo 数据
wo_l2_data = [wo_art[1], wo_sail[1], wo_poptrie[1]]
wo_l3_data = [wo_art[2], wo_sail[2], wo_poptrie[2]]
w_l1_data = [w_art[0], w_sail[0], w_poptrie[0]]  # w 数据
w_l2_data = [w_art[1], w_sail[1], w_poptrie[1]]
w_l3_data = [w_art[2], w_sail[2], w_poptrie[2]]

# 开始绘图
plt.figure(1, dpi=600, figsize=(5, 3))
plt.subplots_adjust(wspace=0.05)  # 两幅图片之间的间隔
plt.tight_layout()

ax = plt.subplot(121)  # 绘制第一个柱状图
ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
bar1 = plt.bar(header[1:], wo_l1_data, color='lightgrey', edgecolor='black', linewidth=1)
bar2 = plt.bar(header[1:], wo_l2_data, bottom=wo_l1_data, color='goldenrod', edgecolor='black', linewidth=1)
bar3 = plt.bar(header[1:], wo_l3_data, bottom=[wo_l2_data[i] + wo_l1_data[i] for i in range(len(wo_l2_data))],
               color='limegreen', edgecolor='black', linewidth=1)
plt.xticks(header[1:], fontproperties='Times New Roman', size=16)
plt.grid(axis='y', color='black', linewidth=0.5, linestyle='--')
font = {'family': 'Times New Roman', 'size': 20}
plt.ylabel('overall cache-miss \n overhead per packet(ns)', font)
plt.xlabel('w/o comp', font)
plt.ylim(0, 122)
plt.yticks(np.arange(0, 140, 20), fontproperties='Times New Roman', size=16)

matplotlib.rcParams['ytick.direction'] = 'in'  # 设置第2图片y轴刻度的方向
ax = plt.subplot(122)  # 绘制第二个柱状图
ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
bar1 = plt.bar(header[1:], w_l1_data, color='lightgrey', edgecolor='black', linewidth=1)
bar2 = plt.bar(header[1:], w_l2_data, bottom=w_l1_data, color='goldenrod', edgecolor='black', linewidth=1)
bar3 = plt.bar(header[1:], w_l3_data, bottom=[w_l2_data[i] + w_l1_data[i] for i in range(len(w_l2_data))],
               color='limegreen', edgecolor='black', linewidth=1)
plt.xticks(header[1:], fontproperties='Times New Roman', size=16)  # 设置横坐标
plt.grid(axis='y', color='black', linewidth=0.5, linestyle='--')  # 设置网格线
plt.xlabel('w comp', font)
plt.yticks(np.arange(0, 140, 20), ['', '', '', '', '', ''], fontproperties='Times New Roman', size=16)
plt.ylim(0, 122)

font = {'family': 'Times New Roman', 'size': 16}
plt.legend([bar1, bar2, bar3], ['L1 miss overhead', 'L2 miss overhead', 'L3 miss overhead'], loc='upper center', ncol=3,
           bbox_to_anchor=(-0.2, 1.30), prop=font, columnspacing=0.1, handlelength=1, handletextpad=0.1, frameon=False)

plt.savefig('result/example3.pdf', dpi=600, bbox_inches='tight')  # 保存为pdf文件
plt.savefig('example-picture/example3.png',dpi=600,bbox_inches='tight') # 保存为png文件

# plt.show()
