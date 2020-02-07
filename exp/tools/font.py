#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/9 12:01

import numpy as np

fontsize = {
    10: {'family': 'Arial', 'size': 10},
    11: {'family': 'Arial', 'size': 11},
    12: {'family': 'Arial', 'size': 12},
    13: {'family': 'Arial', 'size': 13},
    14: {'family': 'Arial', 'size': 14},
    15: {'family': 'Arial', 'size': 15},
    16: {'family': 'Arial', 'size': 16},
    17: {'family': 'Arial', 'size': 17},
    18: {'family': 'Arial', 'size': 18},
    19: {'family': 'Arial', 'size': 19},
    20: {'family': 'Arial', 'size': 20},
    21: {'family': 'Arial', 'size': 21},
}


class Font:

    @staticmethod
    def font(size):
        return fontsize[size]
