#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/8 21:48

import matplotlib.pyplot as plt
from font import Font
import matplotlib

pdf_base_dir = 'result/'  # pdf保存的目录
picture_base_dir = 'example-picture/'  # png格式保存的目录

color = ['#e6550d', '#fdae6b', '#fee6ce']


class Plot:

    @staticmethod
    def create_figure(figsize, dpi=600, wspace=0.1):
        plt.figure(1, figsize=figsize, dpi=600)
        plt.tight_layout()
        plt.subplots_adjust(wspace=wspace)

    @staticmethod
    def plot_setting(loc, axis_width=2, xtick_direction='out', ytick_dircetion='out'):
        matplotlib.rcParams['xtick.direction'] = xtick_direction
        matplotlib.rcParams['ytick.direction'] = ytick_dircetion  # 设置坐标轴刻度朝向
        ax = plt.subplot(loc)
        ax.set_axisbelow(True)  # 设置网格线和坐标轴是在figure的上面还是在下面
        ax.spines['bottom'].set_linewidth(axis_width)  # 设置坐标轴宽度
        ax.spines['right'].set_linewidth(axis_width)
        ax.spines['top'].set_linewidth(axis_width)
        ax.spines['left'].set_linewidth(axis_width)
        return ax

    @staticmethod
    def plot_bar(x, height, color, bar_width=0.2, bottom=None, edgecolor='black', linewidth=1, hatch=None):
        return plt.bar(x, height, width=bar_width, color=color, edgecolor='black', linewidth=linewidth, hatch=hatch,
                       bottom=bottom)

    @staticmethod
    def plot(data, label, color='black', marker=None, linestyle='-', markersize=10, linewidth=2, ):
        return plt.plot(data, label=label, color=color, marker=marker, markersize=markersize, linewidth=linewidth,
                        linestyle=linestyle)

    @staticmethod
    def plot_box(data, showfilers=False, widths=0.8, cap_color='black', cap_linewidth=1, median_color='darkorange',
                 median_linewidth=1):
        f = plt.boxplot(data, showfliers=showfilers, widths=widths)
        for cap in f['caps']:  # 把箱型图中的错误符号进行设置
            cap.set(color=cap_color, linewidth=cap_linewidth)
        for median in f['medians']:  # 把箱型图中的中位数符号进行设置
            median.set(color=median_color, linewidth=median_linewidth)
        return f

    @staticmethod
    def plot_text(x, y, text, fontsize=20):
        plt.text(x, y, text, fontsize=fontsize)

    @staticmethod
    def plot_xlim(start, end):
        plt.xlim(start, end)

    @staticmethod
    def plot_xticks(ticks, label=None, font_size=16):
        plt.xticks(ticks=ticks, labels=label, fontproperties='Times New Roman', size=font_size)

    @staticmethod
    def plot_xlable(label, font_size=13):
        plt.xlabel(label, Font.font(font_size))

    @staticmethod
    def plot_ylabel(label, font_size=13):
        plt.ylabel(label, Font.font(font_size))

    @staticmethod
    def plot_ylim(start, end):
        plt.ylim(start, end)

    @staticmethod
    def plot_yticks(ticks, label=None, font_size=16):
        plt.yticks(ticks=ticks, labels=label, fontproperties='Times New Roman', size=font_size)

    @staticmethod
    def plot_legend(handle, labels, ncol, bbox_to_anchor, loc='best', font_size=12, columnspacing=0.1,
                    handlelength=1, handletextpad=0.1):
        plt.legend(handle, labels, bbox_to_anchor=bbox_to_anchor, ncol=ncol, loc=loc, prop=Font.font(font_size),
                   frameon=False,
                   columnspacing=columnspacing, handlelength=handlelength, handletextpad=handletextpad)

    @staticmethod
    def plot_grid(axis='y', color='black', linewidth=0.5, linestyle='--'):
        plt.grid(axis=axis, color=color, linewidth=linewidth, linestyle=linestyle)


class Save:
    @staticmethod
    def save_to_pdf(filename, dpi=600):
        plt.savefig(pdf_base_dir + filename + '.pdf', dpi=dpi, bbox_inches='tight')  # 保存为pdf文件

    @staticmethod
    def save_to_picture(filename, dpi=600):
        plt.savefig(picture_base_dir + filename + '.png', dpi=dpi, bbox_inches='tight')  # 保存为png文件

    @staticmethod
    def save(filename, dpi=600):
        Save.save_to_pdf(filename, dpi=dpi)
        Save.save_to_picture(filename, dpi=dpi)
