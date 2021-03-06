#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/2/7 2:25

import numpy as np
from utils import Utils
from plot import *
from font import *
import sys

# 读取命令行参数
csv_filename = sys.argv[1]  # csv文件名
platform = sys.argv[2]  # 平台类型

# 读取csv文件中的内容
data = Utils.read_csv_row(csv_filename)

# 从读取的csv文件中分别获取不同类别的数据
art = data.loc[0, 2:].tolist()[1:]
sail = data.loc[1, 2:].tolist()[1:]
poptrie = data.loc[2, 2:].tolist()[1:]
dxr = data.loc[3, 2:].tolist()[1:]

y_max = max(art + sail + poptrie + dxr)
Plot.create_figure((2.5, 2.))
Plot.plot_setting(111)
ticks=['2','','8','','','64','','','512']
line1, = Plot.plot(np.arange(0, len(art), 1), art, label=ticks, color=Color.red_color[0])
line2, = Plot.plot(np.arange(0, len(sail), 1), sail,label=ticks, linestyle='--', color=Color.dark_color[0])
line3, = Plot.plot(np.arange(0, len(poptrie), 1), poptrie, label=ticks,color=Color.green_color[0], marker='x', markersize=6)
line4, = Plot.plot(np.arange(0, len(dxr), 1), dxr,label=ticks, color=Color.color[0], marker='o', markersize=6)
Plot.plot_xlable('locality', font_size=13)
Plot.plot_ylabel('speed(MLPS)', font_size=13)
Plot.plot_ylim(0, y_max * 5 / 4)
Plot.plot_setYticksLabel(12)
Plot.plot_xticks(np.arange(0, len(art), 1), ticks, font_size=12)
Plot.plot_grid()
Plot.plot_legend([line1, line2, line3, line4], ['Art', 'Sail', 'Poptrie', 'DxR'], ncol=2, bbox_to_anchor=(0.38, 1.08),
                 loc='upper center', columnspacing=0.5,
                 font_size=12, labelspacing=0.1)
Save.save_to_pdf('exp2-1' + '-' + platform)
