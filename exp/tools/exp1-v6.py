#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/2/5 20:10


import numpy as np
from utils import Utils
from plot import *
from font import *

import sys

csv_filename = sys.argv[1]  # csv文件名
rrc_count = int(sys.argv[2])  # rrc的个数

# 读取数据
v6_datas = Utils.read_csv(csv_filename, without_header=True)

v6_art = v6_datas[-1][:rrc_count]
v6_sail = []
for i in v6_datas[-1][rrc_count:rrc_count * 2]:
    v6_sail.append(i)
v6_poptrie = v6_datas[-1][rrc_count * 2:rrc_count * 3]

xtick_label = v6_datas[1][:rrc_count]


def plotv6(art, sail, poptrie, xlabel, ylabel, pdfname):
    Plot.create_figure((3.2, 2.))
    Plot.plot_setting(111)
    bar_width = 0.28
    bar_gap = 0.085

    x_ticks = np.arange(0, len(art) * 2, 2)
    bar1 = Plot.plot_bar(x_ticks, art, bar_width=bar_width)

    x_ticks = []
    for i in np.arange(0, len(sail) * 2, 2):
        x_ticks.append(i + bar_width + bar_gap)
    bar2 = Plot.plot_bar(x_ticks, sail, bar_width=bar_width, hatch='//')

    x_ticks = []
    for i in np.arange(0, len(poptrie) * 2, 2):
        x_ticks.append(i + (bar_width + bar_gap) * 2)
    bar3 = Plot.plot_bar(x_ticks, poptrie, bar_width=bar_width, hatch='oo')

    x_ticks = []
    for i in np.arange(0, len((xtick_label) * 2), 2):
        x_ticks.append(i + (bar_width + bar_gap))
    Plot.plot_xticks(x_ticks, xtick_label, font_size=13, rotation=15)
    Plot.plot_setYticksLabel(fontsize=13)
    Plot.plot_xlable(xlabel, font_size=15)
    Plot.plot_ylabel(ylabel, font_size=15)
    Plot.plot_ylim(0, 49.8)
    Plot.plot_grid()

    Plot.plot_legend([bar1, bar2, bar3], ['Art', 'Sail', 'Poptrie', ], ncol=3, bbox_to_anchor=(0.5, 1.07),
                     loc='upper center', columnspacing=0.3, font_size=12)

    Save.save_to_pdf(pdfname)


if __name__ == '__main__':
    plotv6(v6_art, v6_sail, v6_poptrie, 'fib', 'v6 lookup MLPS', "exp1-v6")
