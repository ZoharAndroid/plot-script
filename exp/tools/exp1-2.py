#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/2/6 20:59

import numpy as np
from utils import Utils
from plot import *
from font import *
import sys

# 读取命令行参数
csv_filename = sys.argv[1]  # csv文件名
rrc_count = int(sys.argv[2])  # rrc的个数

# 读取数据
data = Utils.read_csv_row(csv_filename)

# 每个rrcX分别保存4个算法的数据

xtick_label = data.iloc[0: rrc_count, 1]

art_data = []
for i in np.arange(0, len(xtick_label), 1):
    art_data.append(data.loc[i, 2:].tolist())
sail_data = []
for i in np.arange(len(xtick_label), len(xtick_label) * 2, 1):
    sail_data.append(data.loc[i, 2:].tolist())
poptrie_data = []
for i in np.arange(len(xtick_label) * 2, len(xtick_label) * 3, 1):
    poptrie_data.append(data.loc[i, 2:].tolist())
drx_data = []
for i in np.arange(len(xtick_label) * 3, len(xtick_label) * 4, 1):
    drx_data.append(data.loc[i, 2:].tolist())

Plot.create_figure((16, 2.5))
Plot.plot_setting(111)
box_width = 0.25

positions = []
for i in np.arange(1, len(xtick_label) + 1, 1):
    positions.append(i + 1 / 2 * box_width)
box1 = Plot.plot_box(art_data, median_color=Color.color[0], widths=box_width, positions=positions)
positions = []
for i in np.arange(1, len(xtick_label) + 1, 1):
    positions.append(i + box_width * 1.5)
box2 = Plot.plot_box(sail_data, median_color=Color.green_color[0], widths=box_width, positions=positions)
positions = []
for i in np.arange(1, len(xtick_label) + 1, 1):
    positions.append(i + box_width * 5 / 2)
box3 = Plot.plot_box(poptrie_data, median_color=Color.red_color[0], widths=box_width, positions=positions)
positions = []
for i in np.arange(1, len(xtick_label) + 1, 1):
    positions.append(i + box_width * 7 / 2)
box4 = Plot.plot_box(drx_data, median_color=Color.dark_color[0], widths=box_width, positions=positions)
xtick = []
for i in np.arange(1, len(xtick_label) + 1, 1):
    xtick.append(i + 2 * box_width)
Plot.plot_xticks(xtick, xtick_label, font_size=12)
Plot.plot_setYticksLabel(12)
# Plot.plot_yticks(np.arange(100, 350, 50), font_size=16)
# Plot.plot_ylabel('lookup speed(Mpps)', font_size=20)
# Plot.plot_ylim(100, 320)
Plot.plot_legend([box1["medians"][0], box2["medians"][0], box3["medians"][0], box4["medians"][0]],
                 ['Art', 'Sail', 'Poptrie', 'DxR'], ncol=4, bbox_to_anchor=(0.5, 1.07),
                 loc='upper center', columnspacing=0.8, font_size=15,handlelength=1.5)
Plot.plot_grid()
Plot.plot_ylim(0, 99)
Plot.plot_vlines(np.arange(1, 24, 1), np.zeros(24, dtype=int), np.array([99] * 24), lienstyles="--",
                 colors=Color.dark_color[3])

Save.save_to_pdf("exp1-2")
