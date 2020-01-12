#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/10 12:05

from plot import *
import numpy as np

# 生成数据集
# tss-insert
y1_num = [33, 94.24, 170.82, 264.37, 442.54, 0]
# tss-delete
y2_num = [3.5, 20.83, 162.25, 3132.24, 72041.52, 0]
# mg-insert
y3_num = [2.4, 3, 3.17, 4.066, 4.48, 6.42]
# mg-delete
y4_num = [1.7, 1.95, 1.813, 2.41, 3.41, 15.96]
x_type = ["1x10^2", "1x10^3", "1x10^4", "1x10^5", "1x10^6", "1x10^7"]

Plot.create_figure((5, 2.5))
Plot.plot_setting(111)
bar_width = 0.25
bar_gap = 0.06
x_tick = np.arange(1, 13, 2)
bar1 = Plot.plot_bar(x_tick, y1_num, color=Color.color[0], bar_width=bar_width)
x_tick = []
for i in np.arange(1, 13, 2):
    x_tick.append(i + bar_width + bar_gap)
bar2 = Plot.plot_bar(x_tick, y2_num, color=Color.color[1], bar_width=bar_width)
x_tick = []
for i in np.arange(1, 13, 2):
    x_tick.append(i + (bar_width + bar_gap) * 2)
bar3 = Plot.plot_bar(x_tick, y3_num, color=Color.color[2], bar_width=bar_width,hatch='oo')
x_tick = []
for i in np.arange(1, 13, 2):
    x_tick.append(i + (bar_width + bar_gap) * 3)
bar4 = Plot.plot_bar(x_tick, y4_num, color=Color.color[3], bar_width=bar_width,hatch='\\\\')
Plot.plot_setYscale()
x_tick = []
for i in np.arange(1, 12, 2):
    x_tick.append(i + 3 / 2 * (bar_width + bar_gap))
Plot.plot_xticks(x_tick, x_type, font_size=13,rotation=10)
Plot.plot_setYtickLabelSize(13)
Plot.plot_xlable('# of 2-filed rules', font_size=15)
Plot.plot_ylabel('# of memeory access', font_size=15)
Plot.plot_legend([bar1,bar2,bar3,bar4],['tess-insert','tess-delete','mg-insert','mg-delete'],ncol=2,bbox_to_anchor=(0,1.05),loc='upper left',columnspacing=0.3,font_size=13)
Plot.plot_grid()
Save.save('example9')
