#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/2/7 3:07

import numpy as np
from utils import Utils
from plot import *
from font import *
import sys

# 读取命令行参数
csv_filename = sys.argv[1]  # csv文件名
platform = sys.argv[2]  # 平台
use_num = int(sys.argv[3])  # 需要使用的核心数目

# 读取数据
data = Utils.read_csv(csv_filename, without_header=True)
core_num = int(len(data[0])/4)
art = data[2][:core_num]
sail = data[2][core_num: core_num * 2]
poptrie = data[2][core_num * 2: core_num * 3]
dxr = data[2][core_num * 3:core_num * 4]

art_data = art[0:use_num]
sail_data = sail[0:use_num]
poptrie_data = poptrie[0:use_num]
dxr_data = dxr[0:use_num]

y_max = max(art_data + sail_data + poptrie_data + dxr_data)

Plot.create_figure((3, 2.))
Plot.plot_setting(111)
line1, = Plot.plot(np.arange(1, use_num + 1, 1), art_data, color=Color.red_color[0])
line2, = Plot.plot(np.arange(1, use_num + 1, 1), sail_data, linestyle='--', color=Color.dark_color[0])
line3, = Plot.plot(np.arange(1, use_num + 1, 1), poptrie_data, color=Color.green_color[0], marker='x', markersize=4,
                   linewidth=1.9)
line4, = Plot.plot(np.arange(1, use_num + 1, 1), dxr_data, color=Color.color[0], marker='o', markersize=3,
                   linewidth=1.9)
Plot.plot_xlable('core(#)', font_size=20)
Plot.plot_ylabel('speed(Mpps)', font_size=20)
# tick_gap = 1
# if use_num <= 10:
#     tick_gap = int(use_num/5)
# elif use_num <= 20 and use_num > 10:
#     tick_gap=2
# elif use_num <= 30 and use_num > 20:
#     tick_gap=5
Plot.plot_xticks(np.arange(1, use_num + int(use_num/5), int(use_num/5)))
Plot.plot_ylim(0, y_max * 6 / 5)
# Plot.plot_yticks(np.arange(200, 1000, 200))
Plot.plot_setYticksLabel(16)
Plot.plot_grid()
Plot.plot_legend([line1, line2, line3, line4], ['Art', 'Sail', 'Poptrie', 'DxR'], ncol=2, bbox_to_anchor=(-.06, 1.10),
                 loc='upper left',
                 font_size=15, labelspacing=0.2)
Save.save_to_pdf('exp4-1' + '-' + platform)
