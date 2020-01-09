#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/9 12:01

import numpy as np

fontsize = {
    10: {'family': 'Times New Roman', 'size': 10},
    11: {'family': 'Times New Roman', 'size': 11},
    12: {'family': 'Times New Roman', 'size': 12},
    13: {'family': 'Times New Roman', 'size': 13},
    14: {'family': 'Times New Roman', 'size': 14},
    15: {'family': 'Times New Roman', 'size': 15},
    16: {'family': 'Times New Roman', 'size': 16},
    17: {'family': 'Times New Roman', 'size': 17},
    18: {'family': 'Times New Roman', 'size': 18},
    19: {'family': 'Times New Roman', 'size': 19},
    20: {'family': 'Times New Roman', 'size': 20},
    21: {'family': 'Times New Roman', 'size': 21},
}


class Font:

    @staticmethod
    def font(size):
        return fontsize[size]
