#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/7 19:29

from utils import Utils
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 这是一个箱型图例子
name = ['art', 'sail', 'poptrie']

art_data = Utils.read_csv('art' + '_loc512_rand.csv', only_data=True)[1:]
header, sail_data = Utils.read_csv('sail' + '_loc512_rand.csv')
sail_data = sail_data[1:]
poptrie_data = Utils.read_csv('poptrie' + '_loc512_rand.csv', only_data=True)[1:]

plt.figure(1, figsize=(5, 2.5), dpi=600)
plt.tight_layout()
plt.subplots_adjust(wspace=0.1)
ax = plt.subplot(131)
ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
f = plt.boxplot(art_data, showfliers=False, widths=0.8)
for cap in f['caps']:  # 把箱型图中的错误符号进行设置
    cap.set(color='black', linewidth=1.5)
for median in f['medians']:  # 把箱型图中的中位数符号进行设置
    median.set(color='darkorange', linewidth=1)
plt.xlim(0,10.5)
plt.xticks(range(1, 11, 1), ['1', '', '', '8', '', '', '64', '', '', '512'], fontproperties='Times New Roman', size=14)
plt.ylim(0, 820)
plt.yticks(np.arange(0, 1000, 200), fontproperties='Times New Roman', size=16)
font = {'family': 'Times New Roman', 'size': 20}
plt.xlabel('locality', font)
plt.ylabel('speed(Mpps)', font)
plt.grid(axis='y', color='black', linewidth=0.5, linestyle='--')
ax.text(1, 700, name[0].capitalize(), fontsize=20)

matplotlib.rcParams['ytick.direction'] = 'in'  # 设置坐标轴刻度朝向
ax = plt.subplot(132)
ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
f=plt.boxplot(sail_data, showfliers=False, widths=0.8)
for cap in f['caps']:  # 把箱型图中的错误符号进行设置
    cap.set(color='black', linewidth=1.5)
for median in f['medians']:  # 把箱型图中的中位数符号进行设置
    median.set(color='darkorange', linewidth=1)
plt.xlim(0,10.5)
plt.xticks(range(1, 11, 1), ['1', '', '', '8', '', '', '64', '', '', '512'], fontproperties='Times New Roman', size=14)
plt.ylim(0, 820)
plt.yticks([200, 400, 600, 800], ['', '', '', ''], fontproperties='Times New Roman', size=16)
font = {'family': 'Times New Roman', 'size': 20}
plt.xlabel('locality', font)
plt.grid(axis='y', color='black', linewidth=0.5, linestyle='--')
ax.text(1, 700, name[1].capitalize(), fontsize=20)

matplotlib.rcParams['ytick.direction'] = 'in'  # 设置坐标轴朝向
ax = plt.subplot(133)
ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
ax.spines['bottom'].set_linewidth(2)  # 设置坐标轴宽度
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
f=plt.boxplot(poptrie_data, showfliers=False, widths=0.8)
for cap in f['caps']:  # 把箱型图中的错误符号进行设置
    cap.set(color='black', linewidth=1.5)
for median in f['medians']:  # 把箱型图中的中位数符号进行设置
    median.set(color='darkorange', linewidth=1)
plt.xlim(0,10.5)
plt.xticks(range(1, 11, 1), ['1', '', '', '8', '', '', '64', '', '', '512'], fontproperties='Times New Roman', size=14)
plt.ylim(0, 820)
plt.yticks([200, 400, 600, 800], ['', '', '', ''], fontproperties='Times New Roman', size=16)
font = {'family': 'Times New Roman', 'size': 20}
plt.xlabel('locality', font)
plt.grid(axis='y', color='black', linewidth=0.5, linestyle='--')
ax.text(1, 700, name[2].capitalize(), fontsize=20)

plt.savefig('result/example2.pdf', dpi=600, bbox_inches='tight')
plt.show()
