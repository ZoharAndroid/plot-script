#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/7 12:21
from utils import Utils
from plot import Plot
from plot import Save
import numpy as np

# 这是一个折线图

# 读取csv文件中的内容
header, data = Utils.read_csv('all_loc512_normal.csv')

# 从读取的csv文件中分别获取不同类别的数据
locality = data[0]
art = data[1]
sail = data[2]
poptrie = data[3]

Plot.create_figure((3, 2.5))
Plot.plot_setting(111)
line1, = Plot.plot(np.arange(0,10,1),art, label=str(header[1]).capitalize(),color='#e6550d')
line2, = Plot.plot(np.arange(0,10,1),sail, label=str(header[2]).capitalize(), linestyle='--',color='#fdae6b')
line3, = Plot.plot(np.arange(0,10,1),poptrie, label=str(header[3]).capitalize(), color='#fee6ce', marker='o')
Plot.plot_xlable('locality', font_size=20)
Plot.plot_ylabel('speed(Mpps)', font_size=20)
Plot.plot_xticks(np.arange(0, 10, 3), ['1', '8', '64', '512'])
Plot.plot_yticks(np.arange(200, 1000, 200))
Plot.plot_ylim(200, 820)
Plot.plot_grid()
Plot.plot_legend([line1, line2, line3], ['Art', 'Sail', 'Poptrie'], ncol=2,bbox_to_anchor=(0,1.05),loc='upper left',font_size=16)

# plt.figure(num=1, figsize=(3, 2.5), dpi=600)
# ax = plt.subplot(111)
# ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
# ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
# ax.spines['right'].set_linewidth(2)
# ax.spines['top'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# line1 = plt.plot(art, label=str(header[1]).capitalize(), color="black", linewidth=2)
# line2 = plt.plot(sail, label=str(header[2]).capitalize(), color='black', linestyle='--', linewidth=2)
# line3 = plt.plot(poptrie, label=str(header[3]).capitalize(), color='olive', marker='x', markersize=10, linewidth=2)
# font = {'family': 'Times New Roman', 'size': 20}
# plt.xlabel('locality', font)
# plt.ylabel('speed(Mpps)', font)
# plt.xticks([0, 3, 6, 9], [1, 8, 64, 512], fontproperties='Times New Roman', size=16)
# plt.ylim(200, 820);
# plt.yticks(range(200, 1000, 200), fontproperties='Times New Roman', size=16)
#
# plt.grid(axis='y', color='black', linewidth=0.5, linestyle='--')
#
# font = {'family': 'Times New Roman', 'size': 16}
# plt.legend(loc='upper left', frameon=False, ncol=2, labelspacing=0.1, columnspacing=0.1, handlelength=2,
#            handletextpad=0.5, borderaxespad=0.01, prop=font)


Save.save('example1')
