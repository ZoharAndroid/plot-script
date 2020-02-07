#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/2/7 1:36

import numpy as np
from utils import Utils
from plot import *
from font import *
import sys

# 读取命令行参数
csv_filename = sys.argv[1]  # csv文件名
platform = sys.argv[2]  # 平台

# 读取数据
data = Utils.read_csv_row(csv_filename)
name = ['Art', 'Sail', 'Poptrie', 'DxR']
xtick_label = data.iloc[0: 10, 1]

poptrie_data = []
y_max = 0
for i in np.arange(0, len(xtick_label), 1):
    poptrie_data.append(data.loc[i, 2:].tolist())
    temp = max(data.loc[i, 2:].tolist())
    if y_max < temp:
        y_max = temp
sail_data = []
for i in np.arange(len(xtick_label), len(xtick_label) * 2, 1):
    sail_data.append(data.loc[i, 2:].tolist())
    temp = max(data.loc[i, 2:].tolist())
    if y_max < temp:
        y_max = temp
art_data = []
for i in np.arange(len(xtick_label) * 2, len(xtick_label) * 3, 1):
    art_data.append(data.loc[i, 2:].tolist())
    temp = max(data.loc[i, 2:].tolist())
    if y_max < temp:
        y_max = temp
drx_data = []
for i in np.arange(len(xtick_label) * 3, len(xtick_label) * 4, 1):
    drx_data.append(data.loc[i, 2:].tolist())
    temp = max(data.loc[i, 2:].tolist())
    if y_max < temp:
        y_max = temp


box_width = 0.8
ytick_max = y_max * 6 / 5
ytick_gap = 50
if ytick_max / 4 <= 100:
    ytick_gap = 50
elif ytick_max / 4 > 100 and ytick_max / 4 <= 200:
    ytick_gap = 100
elif ytick_max / 4 > 200 and ytick_max / 4 <= 400:
    ytick_gap = 200

Plot.create_figure((10, 2.5))
Plot.plot_setting(141)
f = Plot.plot_box(art_data, widths=box_width, median_color=Color.red_color[0])
Plot.plot_xlim(0, 10.5)
Plot.plot_xticks(np.arange(1, 11, 1), ['1', '', '', '8', '', '', '64', '', '', '512'], font_size=14)
Plot.plot_ylim(0, y_max * 6 / 5)
Plot.plot_yticks(np.arange(0, ytick_max, ytick_gap), font_size=14)
Plot.plot_xlable('locality', font_size=15)
Plot.plot_ylabel('speed(Mpps)', font_size=20)
Plot.plot_grid()
Plot.plot_text(1, y_max, name[0])

Plot.plot_setting(142, ytick_dircetion='in')
f = Plot.plot_box(sail_data, widths=box_width, median_color=Color.green_color[0])
Plot.plot_xlim(0, 10.5)
Plot.plot_xticks(np.arange(1, 11, 1), ['1', '', '', '8', '', '', '64', '', '', '512'], font_size=14)
Plot.plot_ylim(0, y_max * 6 / 5)
Plot.plot_yticks(np.arange(0, ytick_max, ytick_gap), ['', '', '', ''], font_size=14)
Plot.plot_xlable('locality', font_size=15)
Plot.plot_grid()
Plot.plot_text(1, y_max , name[1], fontsize=20)

Plot.plot_setting(143, ytick_dircetion='in')
f = Plot.plot_box(poptrie_data, widths=box_width, median_color=Color.dark_color[0])
Plot.plot_xlim(0, 10.5)
Plot.plot_xticks(np.arange(1, 11, 1), ['1', '', '', '8', '', '', '64', '', '', '512'], font_size=14)
Plot.plot_ylim(0, y_max * 6 / 5)
Plot.plot_yticks(np.arange(0, ytick_max, ytick_gap), ['', '', '', ''], font_size=14)
Plot.plot_xlable('locality', font_size=15)
Plot.plot_grid()
Plot.plot_text(1, y_max , name[2], fontsize=20)

Plot.plot_setting(144, ytick_dircetion='in')
f = Plot.plot_box(drx_data, widths=box_width, median_color=Color.blue_color[0])
Plot.plot_xlim(0, 10.5)
Plot.plot_xticks(np.arange(1, 11, 1), ['1', '', '', '8', '', '', '64', '', '', '512'], font_size=14)
Plot.plot_ylim(0, y_max * 6 / 5)
Plot.plot_yticks(np.arange(0, ytick_max, ytick_gap), ['', '', '', ''], font_size=14)
Plot.plot_xlable('locality', font_size=15)
Plot.plot_grid()
Plot.plot_text(1, y_max , name[3], fontsize=20)

Save.save_to_pdf('exp2-2' + '-' + platform)
