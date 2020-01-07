#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/7 11:44
import pandas as pd
import numpy as py

data_base_dir = 'datas/'

class Utils:

    @staticmethod
    def read_csv(filename):
        data_frame = pd.read_csv(data_base_dir + filename)
        header = list(data_frame.columns.values)
        data = []
        for i in header:
            column_data = data_frame[i].tolist()
            data.append(column_data)

        return header, data

    @staticmethod
    def read_csv_index(filename, index):
        data_frame = pd.read_csv(data_base_dir + filename)
        return data_frame[index].tolist()
