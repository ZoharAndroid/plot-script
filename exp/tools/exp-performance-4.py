#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/9 20:33
from plot import *
from utils import Utils
import sys

platform = sys.argv[1]  # 平台

# data = Utils.read_csv('example8.csv', only_data=True)
# max_min_data = Utils.read_csv('example8-2.csv', only_data=True)
# mem_data = [data[1][0], data[2][0], data[3][0], data[4][0]]
# req_data = [data[1][1], data[2][1], data[3][1], data[4][1]]
# m_max = [max_min_data[1][0], max_min_data[2][0], max_min_data[3][0], max_min_data[4][0]]
# m_min = [max_min_data[1][1], max_min_data[2][1], max_min_data[3][1], max_min_data[4][1]]
# r_max = [max_min_data[1][2], max_min_data[2][2], max_min_data[3][2], max_min_data[4][2]]
# r_min = [max_min_data[1][3], max_min_data[2][3], max_min_data[3][3], max_min_data[4][3]]
mem_data=[2,2,5,6]
req_data=[1,2,3,6]
m_max=[6,3,9,15]
m_min=[2,1,2,3]
r_max=[3,3,5,15]
r_min=[1,1,2,3]

Plot.create_figure((2.0, 2.0))
Plot.plot_setting(111,xtick_direction='in')
bar_width = 0.3
bar_gap=0.05
bar1=Plot.plot_bar([1, 2, 3, 4], mem_data, color=Color.dark_color[3], bar_width=bar_width)
bar2=Plot.plot_bar([1+bar_gap + bar_width, 2 +bar_gap + bar_width, 3+bar_gap + bar_width, 4+bar_gap + bar_width], req_data, color=Color.dark_color[4],
              bar_width=bar_width)
line1=Plot.plot_hlines(m_max,[1-bar_width/2,2-bar_width/2,3-bar_width/2,4-bar_width/2],[1+bar_width/2,2+bar_width/2,3+bar_width/2,4+bar_width/2],colors='red')
line2=Plot.plot_hlines(m_min,[1-bar_width/2,2-bar_width/2,3-bar_width/2,4-bar_width/2],[1+bar_width/2,2+bar_width/2,3+bar_width/2,4+bar_width/2],colors='#006d2c')
x_min_index=[1+bar_width/2+bar_gap,2+bar_width/2+bar_gap,3+bar_width/2+bar_gap,4+bar_width/2+bar_gap]
x_max_temp=1.5*bar_width+bar_gap
x_max_index=[1+x_max_temp,2+x_max_temp,3+x_max_temp,4+x_max_temp]
line1=Plot.plot_hlines(r_max,x_min_index,x_max_index,colors='red')
line2=Plot.plot_hlines(r_min,x_min_index,x_max_index,colors='#006d2c')
tick_temp=(bar_width+bar_gap)/2
Plot.plot_xticks([1+tick_temp,2+tick_temp,3+tick_temp,4+tick_temp],['Art','Sail','Poptrie','DXR'],rotation=30,font_size=12)
Plot.plot_ylim(0,19)
Plot.plot_grid()

Plot.plot_legend([bar1,bar2,line1,line2],['memory access','requested blocks','Max','Min'],ncol=1,bbox_to_anchor=(-0.05,1.05),loc="upper left",font_size=10,labelspacing=0.1)
Save.save_to_pdf('exp-performance-4'+'-'+platform)
