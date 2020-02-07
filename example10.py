#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/12 11:21

from exp.tools.plot import *
import numpy as np


Plot.create_figure((3.5, 3.5))
Plot.plot_setting(111)
x = np.arange(1, 10**6, 1)
Plot.plot(x, x)
Plot.plot_setXscale()
Plot.plot_setYscale()
Plot.plot_setXticksLabel(rotation=20)
Plot.plot_setYticksLabel()
Plot.plot_grid()
Save.save('example10')

