#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/2/5 20:10

import numpy as np
from utils import Utils
from plot import *
from font import *
import sys

# 读取命令行参数
csv_filename = sys.argv[1]  # csv文件名
rrc_count = int(sys.argv[2])  # rrc的个数
platform = sys.argv[3]  # 平台

# 读取数据
data = Utils.read_csv_row(csv_filename)
# print(data)
index = ['rrc00', 'rrc01', 'rrc04', 'rrc05', 'rrc10', 'rrc11', 'rrc14', 'rrc15', 'rrc19', 'rrc20']
v4_art = []
v4_sail = []
v4_poptrie = []
v4_dxr = []
for i in np.arange(0,data.shape[0],1):
    if data.loc[i,0] == 'art' and data.loc[i,1] in index:
        v4_art.append(data.loc[i,2])
    if data.loc[i,0] == 'sail' and data.loc[i,1] in index:
        v4_sail.append(data.loc[i,2])
    if data.loc[i,0] == 'poptrie' and data.loc[i,1] in index:
        v4_poptrie.append(data.loc[i,2])
    if data.loc[i,0] == 'dxr' and data.loc[i,1] in index:
        v4_dxr.append(data.loc[i,2])
print(v4_art)
print(v4_dxr)
# v4_datas = Utils.read_csv(csv_filename, without_header=True)
# v4_art = v4_datas[-1][:rrc_count]
# v4_sail = []
# for i in v4_datas[-1][rrc_count:rrc_count * 2]:
#     v4_sail.append(i)
# v4_poptrie = v4_datas[-1][rrc_count * 2:rrc_count * 3]
# v4_dxr = v4_datas[-1][rrc_count * 3:rrc_count * 4]

xtick_label = []
for i in np.arange(0,len(index),1):
    xtick_label.append('fib'+'-'+str(i+1))
temp = v4_art + v4_sail + v4_poptrie + v4_dxr
y_max = max(temp)


# 读取rrcs相关的数据
# v4_rrcs,v4_rrcs_label = Utils.v4_rrcs_data()
# index = sorted(range(len(v4_rrcs)), key=lambda k: v4_rrcs[k])
# print(index)


def plotv4(art, sail, poptrie, dxr, ylabel, pdfname):
    Plot.create_figure((8, 2.1))
    Plot.plot_setting(111)
    bar_width = 0.3
    bar_gap = 0.09

    x_ticks = np.arange(0, len(art) * 2, 2)
    bar1 = Plot.plot_bar(x_ticks, art, bar_width=bar_width, color=Color.dark_color[3])

    x_ticks = []
    for i in np.arange(0, len(sail) * 2, 2):
        x_ticks.append(i + bar_width + bar_gap)
    bar2 = Plot.plot_bar(x_ticks, sail, bar_width=bar_width, hatch='//')

    x_ticks = []
    for i in np.arange(0, len(poptrie) * 2, 2):
        x_ticks.append(i + (bar_width + bar_gap) * 2)
    bar3 = Plot.plot_bar(x_ticks, poptrie, bar_width=bar_width, color=Color.dark_color[4])

    x_ticks = []
    for i in np.arange(0, len(dxr) * 2, 2):
        x_ticks.append(i + (bar_width + bar_gap) * 3)
    bar4 = Plot.plot_bar(x_ticks, dxr, bar_width=bar_width, hatch='\\\\\\')

    x_ticks = []
    for i in np.arange(0, len((xtick_label) * 2), 2):
        x_ticks.append(i + 3 / 2 * (bar_width + bar_gap))
    Plot.plot_xticks(x_ticks, xtick_label, font_size=16)
    Plot.plot_setYticksLabel(fontsize=15)
    # Plot.plot_xlable(xlabel, font_size=13)
    Plot.plot_ylabel(ylabel, font_size=16)
    Plot.plot_ylim(0, y_max * 6 / 5)
    Plot.plot_grid()

    # index = 0
    # for i in x_ticks:
    #     Plot.plot_text(i, -10, v4_rrcs[index],fontsize=12)
    #     index = index + 1;
    Plot.plot_legend([bar1, bar2, bar3, bar4], ['Art', 'Sail', 'Poptrie', 'DxR'], ncol=4, bbox_to_anchor=(0.5, 1.075),
                     loc='upper center', columnspacing=1, font_size=16,handlelength=2)

    Save.save_to_pdf(pdfname)


if __name__ == '__main__':
    plotv4(v4_art, v4_sail, v4_poptrie, v4_dxr, 'lookup speed(MLPS)', "exp1-v4" + "-" + platform)
