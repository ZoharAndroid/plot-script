#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/2/7 7:08

import numpy as np
from utils import Utils
from plot import *
from font import *
import sys

# 读取命令行参数
csv_filename = sys.argv[1]  # csv文件名
platform = sys.argv[2]  # 平台

# 插入删除时间

data = Utils.read_csv(csv_filename, without_header=True)
art_data = [data[1][0], data[2][0]]
sail_data = [data[1][1], data[2][1]]
poptrie_data = [data[1][2], data[2][2]]
dxr_data = [data[1][3], data[2][3]]

y_max = max(art_data + sail_data + poptrie_data + dxr_data)

# 绘图
Plot.create_figure((3.2, 2))

Plot.plot_setting(111)
bar_width = 0.2
bar1 = Plot.plot_bar([1, 2], art_data, color=Color.dark_color[3])
bar2 = Plot.plot_bar([1 + bar_width, 2 + bar_width], sail_data, hatch='//')
bar3 = Plot.plot_bar([1 + bar_width * 2, 2 + bar_width * 2], poptrie_data, color=Color.dark_color[4])
bar4 = Plot.plot_bar([1 + bar_width * 3, 2 + bar_width * 3], dxr_data, hatch='\\\\\\')
Plot.plot_xticks([1 + bar_width * 1.5, 2 + bar_width * 1.5], ['insert', 'delete'])
# Plot.plot_show_barAboveText(bar1)
# Plot.plot_show_barAboveText(bar2)
# Plot.plot_show_barAboveText(bar3)
Plot.plot_ylim(0, y_max*6/5)
# Plot.plot_yticks(np.arange(10, 45, 10))
Plot.plot_grid()
Plot.plot_setYticksLabel(15)
Plot.plot_ylabel('update overhead('+r'$\mu$s)', font_size=16)
Plot.plot_legend([bar1, bar2, bar3, bar4], ['Art', 'Sail', 'Poptrie', 'DxR'], loc='upper right',
                 bbox_to_anchor=(1.05, 1.05), ncol=1, font_size=13,
                 labelspacing=0.1)
Save.save_to_pdf('exp5-1' + "-" + platform)
