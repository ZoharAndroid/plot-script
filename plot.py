#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/8 21:48

import matplotlib.pyplot as plt
from font import Font
import matplotlib
from matplotlib.pyplot import MultipleLocator

pdf_base_dir = 'result/'  # pdf保存的目录
picture_base_dir = 'example-picture/'  # png格式保存的目录


class Plot:
    figure = None  # 调用create_figure之后生成的figure对象
    ax = None  # 调用Plot_setting之后生成的ax对象

    @staticmethod
    def create_figure(figsize, dpi=600, wspace=0.1):
        figure = plt.figure(1, figsize=figsize, dpi=dpi)
        plt.tight_layout()
        plt.subplots_adjust(wspace=wspace)
        Plot.figure = figure

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
        Plot.ax = ax
        return ax

    @staticmethod
    def plot_bar(x, height, color, bar_width=0.2, bottom=None, edgecolor='black', linewidth=1, hatch=None):
        return plt.bar(x, height, width=bar_width, color=color, edgecolor='black', linewidth=linewidth, hatch=hatch,
                       bottom=bottom)

    @staticmethod
    def plot(x, data, label, color='black', marker=None, linestyle='-', markersize=10, linewidth=2, ):
        return plt.plot(x, data, label=label, color=color, marker=marker, markersize=markersize, linewidth=linewidth,
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
    def plot_text(x, y, text, fontsize=20, rotation=None, wrap=False):
        plt.text(x, y, text, fontsize=fontsize, rotation=rotation, wrap=wrap)

    @staticmethod
    def plot_hlines(y_data, x_start, x_end, colors='black', lienstyles='-', label=None):
        return plt.hlines(y_data, x_start, x_end, colors=colors, linestyles=lienstyles, label=label)

    @staticmethod
    def plot_semilogy(x, y, basey=10, color='black', marker=None, linestyle='-', markersize=10, linewidth=2, ):
        return plt.semilogy(x, y, basey=basey, color=color, marker=marker, markersize=markersize,
                            linewidth=linewidth, linestyle=linestyle)

    @staticmethod
    def plot_semilogx(x, y, basex=10, color='black', marker=None, linestyle='-', markersize=10, linewidth=2, ):
        return plt.semilogx(x, y, basex=basex, color=color, marker=marker, markersize=markersize,
                            linewidth=linewidth, linestyle=linestyle)

    @staticmethod
    def plot_setXscale():
        Plot.ax.set_xscale('log')

    @staticmethod
    def plot_setYscale():
        Plot.ax.set_yscale('log')
        Plot.ax

    @staticmethod
    def plot_loglog(x, y, basex=10, basey=10, color='black', marker=None, linestyle='-', markersize=10, linewidth=2, ):
        return plt.loglog(x, y, basex=basex, basey=basey, color=color, marker=marker, markersize=markersize,
                          linewidth=linewidth, linestyle=linestyle)

    @staticmethod
    def plot_xlim(start, end):
        plt.xlim(start, end)

    @staticmethod
    def plot_xticks(ticks, label=None, font_size=16, rotation=None):
        plt.xticks(ticks=ticks, labels=label, fontproperties='Times New Roman', size=font_size, rotation=rotation)

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
                    handlelength=1, handletextpad=0.1, labelspacing=None):
        """
        绘制图例。
        参考链接：
        https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html?highlight=legend#matplotlib.pyplot.legend
        :param handle: 图例的句柄。
        :param labels: 显示的标签。这里显示标签的个数应该和句柄的格式是一样的。
        :param ncol: 显示的列数。
        :param bbox_to_anchor: 将图例定下锚点。也就是相对位置。传入(x,y)
        :param loc: 图例显示的大概位置。默认为'best',也就是自动选择。可以选择'upper right'/'upper left'/'lower right'等值。
        :param font_size: 图例字体大小。
        :param columnspacing: 每列间隔大小。 适用于多列的情况。
        :param handlelength: 句柄的长度大小。
        :param handletextpad: 句柄和标签之间的间隔大小。
        :param labelspacing: 每行间隔的大小。适用于多行的情况
        :return:
        """
        plt.legend(handle, labels, bbox_to_anchor=bbox_to_anchor, ncol=ncol, loc=loc, prop=Font.font(font_size),
                   frameon=False,
                   columnspacing=columnspacing, handlelength=handlelength, handletextpad=handletextpad,
                   labelspacing=labelspacing)

    @staticmethod
    def plot_grid(axis='y', color='black', linewidth=0.5, linestyle='--'):
        plt.grid(axis=axis, color=color, linewidth=linewidth, linestyle=linestyle)

    @staticmethod
    def plot_xaxis_invisible():
        """
        x轴坐标轴不可见。
        :return:
        """
        frame = plt.gca()
        frame.axes.get_xaxis().set_visible(False)

    @staticmethod
    def plot_yaxis_invisible():
        """
        y轴坐标轴不可见。
        :return:
        """
        frame = plt.gca()
        frame.axes.get_yaxis().set_visible(False)

    @staticmethod
    def plot_setXtickLabelSize(fontsize):
        """
        设置X轴刻度的大小值。这个可以单独设置X轴的大小值，不依赖于其他的方法。
        :param fontsize: 刻度大小值
        :return:
        """
        labels = Plot.ax.get_xticklabels()
        for label in labels:
            label.set_fontsize(fontsize)
            label.set_fontname('Times New Roman')

    @staticmethod
    def plot_setYtickLabelSize(fontsize):
        """
        设置Y轴刻度的大小值。这个可以单独设置Y轴的大小值，不依赖于其他的方法。
        :param fontsize: 刻度大小值
        :return:
        """
        labels = Plot.ax.get_yticklabels()
        for label in labels:
            label.set_fontsize(fontsize)
            label.set_fontname('Times New Roman')

    @staticmethod
    def plot_set_XtickLabelVisible(visible:bool):
        labels = Plot.ax.get_xticklabels()
        for label in labels:
            label.set_visible(visible)

    @staticmethod
    def plot_set_YtickLabelVisible(visible:bool):
        labels = Plot.ax.get_yticklabels()
        for label in labels:
            label.set_visible(visible)

class Save:
    @staticmethod
    def save_to_pdf(filename, dpi=600):
        """
        保存为pdf。
        :param filename: 文件名。不需要带格式后缀，直接输入文件名即可。
        :param dpi: 显示的dpi，默认600.
        :return:
        """
        plt.savefig(pdf_base_dir + filename + '.pdf', dpi=dpi, bbox_inches='tight')  # 保存为pdf文件

    @staticmethod
    def save_to_picture(filename, dpi=600):
        """
        保存为png格式。
        :param filename: 文件名，不需要输入格式后缀。
        :param dpi: 显示的dpi，默认600.
        :return:
        """
        plt.savefig(picture_base_dir + filename + '.png', dpi=dpi, bbox_inches='tight')  # 保存为png文件

    @staticmethod
    def save(filename, dpi=600):
        """
        直接保存pdf和png两种格式的文件。如果只想保存pdf格式，那么直接使用save_to_pdf()方法；如果只想保存为png图片格式，那么直接使用save_to_picture()方法。
        :param filename: 文件名，不需要输入格式后缀。
        :param dpi: 显示的dpi，默认600.
        :return:
        """
        Save.save_to_pdf(filename, dpi=dpi)
        Save.save_to_picture(filename, dpi=dpi)

    @staticmethod
    def set_xtick_gap(x_gap):
        x_major_locator = MultipleLocator(x_gap)
        ax = plt.gca()
        # ax为两条坐标轴的实例
        ax.xaxis.set_major_locator(x_major_locator)

    @staticmethod
    def set_ytick_gap(y_gap):
        y_major_locator = MultipleLocator(y_gap)
        ax = plt.gca()
        # ax为两条坐标轴的实例
        ax.xaxis.set_major_locator(y_major_locator)

    @staticmethod
    def get_axis():
        """
        获取坐标轴实例。
        :return: 两条坐标轴实例。
        """
        return plt.gca()


class Color:
    color = ['#e6550d', '#fdae6b', '#fee6ce', '#fff5eb']
