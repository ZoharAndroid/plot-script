#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/9 19:46

from plot import Plot
from plot import Save
from font import Font
from plot import Color
from utils import Utils
import numpy as np

header, data = Utils.read_csv('example7.csv')

Plot.create_figure((2.0, 2.1))
Plot.plot_setting(111)
bar_width = 0.4
Plot.plot_bar(1, data[0], color=Color.color[0], bar_width=bar_width)
Plot.plot_bar(2, data[1], color=Color.color[1], bar_width=bar_width)
Plot.plot_bar(3, data[2], color=Color.color[2], bar_width=bar_width, hatch='o')
Plot.plot_bar(4, data[3], color=Color.color[3], bar_width=bar_width, hatch='\\')
Plot.plot_grid()
Plot.plot_yticks(np.arange(0, 80, 20), font_size=14)
Plot.plot_xticks([1, 2, 3, 4], ['Art', 'Sail', 'Poptrie', 'DXR'], font_size=14, rotation=40)
line1, = Plot.plot([0.8, 1.2], [34, 34], 'Art active', linestyle='-')
Plot.plot_ylabel('memory(MB)', font_size=18)
Plot.plot_legend([line1], ['Art-active'], 1, bbox_to_anchor=(1.1, 1.08), loc='upper right', font_size=14)
Save.save('example7')
