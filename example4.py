#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/8 11:33

import matplotlib.pyplot as plt
from utils import Utils
import numpy as np
import matplotlib
from plot import Save
from plot import Plot

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
Plot.create_figure((3.2, 2))

Plot.plot_setting(111)
bar_width = 0.2
bar1 = Plot.plot_bar([1, 2], art_data, color='#e6550d')
bar2 = Plot.plot_bar([1 + bar_width, 2 + bar_width], sail_data, color='#fdae6b', hatch='/')
bar3 = Plot.plot_bar([1 + bar_width * 2, 2 + bar_width * 2], poptrie_data, color='#fee6ce', hatch='\\')
Plot.plot_xticks([1 + bar_width, 2 + bar_width], ['w/o comp', 'w comp'])
Plot.plot_show_barAboveText(bar1)
Plot.plot_show_barAboveText(bar2)
Plot.plot_show_barAboveText(bar3)
Plot.plot_ylim(10, 45)
Plot.plot_yticks(np.arange(10, 45, 10))
Plot.plot_grid()
Plot.plot_ylabel('CPU cycle\n per packet')
Plot.plot_legend([bar1, bar2, bar3], ['Art', 'Sail', 'Poptrie'], loc='upper left', bbox_to_anchor=(-0.03, 1.05), ncol=1,labelspacing=0.1)
Save.save('example4')



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
