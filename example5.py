#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/8 12:43

import matplotlib.pyplot as plt
import numpy as np
from utils import Utils
import matplotlib
from plot import Plot
from plot import Save

# 这是一幅包含了3个箱型图的绘图例子
# 读取的文件是：llc_25_box.csv llc_50_box.csv llc_75_box.csv
# 三个csv文件

# 读取文件
header, data_25 = Utils.read_csv('llc_25_box_res.csv')
data_50 = Utils.read_csv('llc_50_box_res.csv', only_data=True)
data_75 = Utils.read_csv('llc_75_box_res.csv', only_data=True)

Plot.create_figure((4.5, 2.5))
Plot.plot_setting(131)
Plot.plot_box(data_25)
Plot.plot_xticks(np.arange(1, 4, 1), ['Art', 'Sail', 'Poptrie'], font_size=16, rotation=20)
Plot.plot_yticks(np.arange(100, 350, 50), font_size=16)
Plot.plot_ylabel('lookup speed(Mpps)', font_size=20)
Plot.plot_ylim(100, 320)
Plot.plot_grid()
Plot.plot_text(0.4, 330, 'LLC=25%', fontsize=17)

Plot.plot_setting(132, ytick_dircetion='in')
Plot.plot_box(data_50)
Plot.plot_xticks(np.arange(1, 4, 1), ['Art', 'Sail', 'Poptrie'], font_size=16, rotation=20)
Plot.plot_yticks(np.arange(100, 350, 50), ['', '', '', '', ''], font_size=16)
Plot.plot_ylim(100, 320)
Plot.plot_grid()
Plot.plot_text(0.4, 330, 'LLC=50%', fontsize=17)

Plot.plot_setting(133, ytick_dircetion='in')
Plot.plot_box(data_75)
Plot.plot_xticks(np.arange(1, 4, 1), ['Art', 'Sail', 'Poptrie'], font_size=16, rotation=20)
Plot.plot_yticks(np.arange(100, 350, 50), ['', '', '', '', ''], font_size=16)
Plot.plot_ylim(100, 320)
Plot.plot_grid()
Plot.plot_text(0.4, 330, 'LLC=75%', fontsize=17)

Save.save('example5')

# plt.figure(1, figsize=(4.5, 2.5), dpi=600)
# plt.subplots_adjust(wspace=0.15)
# plt.tight_layout()
#
# # 绘制第一个箱型图
# ax = plt.subplot(131)
# ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
# ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
# ax.spines['right'].set_linewidth(2)
# ax.spines['top'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# plt.boxplot(data_25, widths=0.8, showfliers=False)
# plt.xticks([1, 2, 3], ['Art', 'Sail', 'Poptrie'], fontproperties='Times New Roman', size=16, rotation=20)
# plt.ylim(100, 320)
# plt.yticks(np.arange(100, 350, 50), fontproperties='Times New Roman', size=16)
# plt.grid(axis='y', linewidth=0.5, color='black', linestyle='--')
# font = {'family': 'Times New Roman', 'size': 20}
# plt.ylabel('lookup speed(Mpps)', font)
# plt.text(0.8, 325, 'LLC=25%', fontsize=15)
#
# # 绘制第2附图片
# matplotlib.rcParams['ytick.direction'] = 'in'  # 设置y轴刻度的方向
# ax = plt.subplot(132)
# ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
# ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
# ax.spines['right'].set_linewidth(2)
# ax.spines['top'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# plt.boxplot(data_50, widths=0.8, showfliers=False)
# plt.xticks([1, 2, 3], ['Art', 'Sail', 'Poptrie'], fontproperties='Times New Roman', size=16, rotation=20)
# plt.ylim(100, 320)
# plt.yticks(np.arange(100, 350, 50), ['', '', '', '', ''])
# plt.grid(axis='y', linewidth=0.5, color='black', linestyle='--')
# plt.text(0.8, 325, 'LLC=50%', fontsize=15)
#
# # 绘制第3幅图片
# matplotlib.rcParams['ytick.direction'] = 'in'  # 设置第2图片y轴刻度的方向
# ax = plt.subplot(133)
# ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
# ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
# ax.spines['right'].set_linewidth(2)
# ax.spines['top'].set_linewidth(2)
# ax.spines['left'].set_linewidth(2)
# plt.boxplot(data_75, widths=0.8, showfliers=False)
# plt.xticks([1, 2, 3], ['Art', 'Sail', 'Poptrie'], fontproperties='Times New Roman', size=16, rotation=20)
# plt.ylim(100, 320)
# plt.yticks(np.arange(100, 350, 50), ['', '', '', '', ''], fontproperties='Times New Roman', size=16)
# plt.grid(axis='y', linewidth=0.5, color='black', linestyle='--')
# plt.text(0.8, 325, 'LLC=75%', fontsize=15)
#
# plt.savefig('result/example5.pdf', dpi=600, bbox_inches='tight')  # 保存为pdf文件
# plt.savefig('example-picture/example5.png', dpi=600, bbox_inches='tight')  # 保存为png文件
