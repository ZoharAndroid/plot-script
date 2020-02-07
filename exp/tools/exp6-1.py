#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/2/7 7:44

import numpy as np
from utils import Utils
from plot import *
from font import *
import sys

# 读取命令行参数
csv_filename = sys.argv[1]  # csv文件名
rrc_count = int(sys.argv[2])  # rrc的个数
platform = sys.argv[3]  # 平台

# 柱形图
data = Utils.read_csv_row(csv_filename)
art_data = []
sail_data = []
poptrie_data = []
xtick_label = []
for i in np.arange(0, data.shape[0], 1):
    if data.loc[i, 0] == 'art':
        if data.loc[i, 1] == 'rrc02' or data.loc[i, 1] == 'rrc06':
            continue
        art_data.append(data.loc[i, 2])
    elif data.loc[i, 0] == 'sail':
        if data.loc[i, 1] == 'rrc02' or data.loc[i, 1] == 'rrc06':
            continue
        sail_data.append(data.loc[i, 2])
    elif data.loc[i, 0] == 'poptrie':
        if data.loc[i, 1] == 'rrc02' or data.loc[i, 1] == 'rrc06':
            continue
        poptrie_data.append(data.loc[i, 2])

    if data.loc[i, 1] not in xtick_label:
        xtick_label.append(data.loc[i, 1])

y_max = max(art_data + sail_data + poptrie_data)

Plot.create_figure((11, 1.9))
Plot.plot_setting(111)
bar_width = 0.3
bar_gap = 0.1

x_ticks = np.arange(0, len(art_data) * 2, 2)
bar1 = Plot.plot_bar(x_ticks, art_data, bar_width=bar_width, color=Color.dark_color[3])

x_ticks = []
for i in np.arange(0, len(sail_data) * 2, 2):
    x_ticks.append(i + bar_width + bar_gap)
bar2 = Plot.plot_bar(x_ticks, sail_data, bar_width=bar_width, hatch='//')

x_ticks = []
for i in np.arange(0, len(poptrie_data) * 2, 2):
    x_ticks.append(i + (bar_width + bar_gap) * 2)
bar3 = Plot.plot_bar(x_ticks, poptrie_data, bar_width=bar_width, color=Color.dark_color[4])

x_ticks = []
for i in np.arange(0, len((xtick_label) * 2), 2):
    x_ticks.append(i +  (bar_width + bar_gap))
Plot.plot_xticks(x_ticks, xtick_label, font_size=12, rotation=10)
Plot.plot_setYticksLabel(fontsize=13)
Plot.plot_xlable('FIB', font_size=13)
Plot.plot_ylabel('v6 lookup MLPS', font_size=13)
Plot.plot_ylim(0, y_max * 6 / 5)
Plot.plot_grid()

Plot.plot_legend([bar1, bar2, bar3], ['Art', 'Sail', 'Poptrie'], ncol=3, bbox_to_anchor=(0.5, 1.07),
                 loc='upper center', columnspacing=1, font_size=13)

Save.save_to_pdf('exp6-1' + '-' + platform)
