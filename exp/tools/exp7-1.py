#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/8 11:33

from utils import Utils
import numpy as np
from plot import *
import sys

# 这是一个并行的柱形图例子
# 读取的文件为：cache-1-0.csv

# 读取文件
# header, data = Utils.read_csv('cache-1-0.csv')
# art_data = data[1]
# sail_data = data[2]
# poptrie_data = data[3]
# wo_data = [art_data[0], sail_data[0], poptrie_data[0]]
# w_data = [art_data[1], sail_data[1], poptrie_data[1]]

_64 = [11.90, 22.59, 31.50]
_256 = [49.25, 79.82, 84.02]
_512 = [74.20, 93.00, 93.37]

y_max = max(_64 + _256 + _512)
# 绘图
Plot.create_figure((3.2, 2))

Plot.plot_setting(111)
bar_width = 0.2
bar_gap=0.05
bar1 = Plot.plot_bar([1, 2, 3], _64, color=Color.dark_color[3])
bar2 = Plot.plot_bar([1 + bar_width+bar_gap, 2 + bar_width+bar_gap, 3 + bar_width+bar_gap], _256, color=Color.dark_color[4], hatch='//')
bar3 = Plot.plot_bar([1 + (bar_width+bar_gap) * 2, 2 + (bar_width+bar_gap) * 2, 3 + (bar_width+bar_gap) * 2], _512, color=Color.dark_color[4])
Plot.plot_xticks([1 + bar_width + 1/2 * bar_gap, 2 + bar_width+ 1/2 * bar_gap, 3 + bar_width+ 1/2 * bar_gap], ['2', '4', '6'])
Plot.plot_show_barAboveText(bar1,font_size=12)
Plot.plot_show_barAboveText(bar2,font_size=12)
Plot.plot_show_barAboveText(bar3,font_size=12)
Plot.plot_ylim(0, y_max * 4 / 3)
Plot.plot_setYticksLabel(15)
# Plot.plot_yticks(np.arange(10, 45, 10))
Plot.plot_grid(color=Color.dark_color[3])
Plot.plot_ylabel('throughput(Gbps)', font_size=15)
Plot.plot_xlable('#OF CORE', font_size=14)
Plot.plot_legend([bar1, bar2, bar3], ['64B', '256B', '512B'], loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=3,
                 labelspacing=0.1, font_size=14,columnspacing=0.2)
Save.save_to_pdf('exp7-1')

# plt.figure(1, figsize=(3.2, 2), dpi=600)
# bar1 = plt.bar([1, 2], art_data, width=bar_width, color=, edgecolor='black',linewidth=1)
# bar2 = plt.bar([1 + bar_width, 2 + bar_width], sail_data, width=bar_width, color='#fdae6b',edgecolor='black',
#                linewidth=1, hatch='/')
# bar3 = plt.bar([1 + bar_width * 2, 2 + bar_width * 2], poptrie_data, width = bar_width, color = '#fee6ce', edgecolor = 'black',
# plt.xticks([1 + bar_width, 2 + bar_width], ['w/o comp', 'w comp'], fontproperties='Times New Roman', size=16)
# plt.ylim(10, 42)
# plt.yticks(np.arange(10, 42, 10), fontproperties='Times New Roman', size=16)
# plt.ylabel('CPU cycle\n per packet', Font.font_13_label)
# plt.legend([bar1, bar2, bar3], ['Art', 'Sail', 'Poptrie'], loc='upper left', bbox_to_anchor=(0, 1), ncol=1,
#            frameon=False, prop=Font.font_12_label, columnspacing=0.1, handlelength=1, handletextpad=0.1)
