#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/7 11:44
import pandas as pd
import numpy as np

data_base_dir = 'exp/csv/'  # 读取csv文件的地址


class Utils:

    @staticmethod
    def read_csv(filename, without_header=False, only_data=False):
        '''
        读取csv文件的数据
        :param filename: 文件名
        :return: header：返回头部信息
                data：返回数据
        '''
        if filename.startswith('exp/csv/'):
            absolute_add = filename
        else:
            absolute_add = data_base_dir + filename
        data = []
        if not without_header:  # csv文件包含header的处理方式
            data_frame = pd.read_csv(absolute_add, header=0)
            if not only_data:  # 返回全部数据
                header = list(data_frame.columns.values)
                for i in header:
                    column_data = data_frame[i].tolist()
                    data.append(column_data)
                return header, data
            else:  # csv文件虽然包含了header，但是只返回数据部分，其他部分不返回
                for i in data_frame.columns.values:
                    data.append(data_frame[i].tolist())
                return data
        else:  # csv文件不包含头部的处理方法
            data_frame = pd.read_csv(absolute_add, header=None, index_col=False)
            for i in np.arange(data_frame.columns.size):
                data.append(data_frame.iloc[:, i].tolist())
            return data

    @staticmethod
    def read_csv_index(filename, index):
        '''
        根据每列给出的index名称来获取该列的值。
        :param filename: 文件名
        :param index: 列索引名
        :return: 该列的数据
        '''
        if filename.startswith('exp/csv/'):
            absolute_add = filename
        else:
            absolute_add = data_base_dir + filename
        data_frame = pd.read_csv(absolute_add)
        return data_frame[index].tolist()

    @staticmethod
    def read_csv_row(filename):
        if filename.startswith('exp/csv/'):
            absolute_add = filename
        else:
            absolute_add = data_base_dir + filename
        data_frame = pd.read_csv(absolute_add, header=None, index_col=False)
        return data_frame

    @staticmethod
    def v4_rrcs_data():
        v4_rrcs_label = []
        v4_rrcs = []
        data = Utils.read_csv('exp/csv/rrcs.csv', without_header=True)
        count = 0
        for i in data[1]:
            count = count + 1
            if count % 2 != 0:
                v4_rrcs.append(i)

        count = 0
        for i in data[0]:
            count = count + 1
            if count % 2 != 0:
                v4_rrcs_label.append(i)

        return v4_rrcs,v4_rrcs_label

    @staticmethod
    def v6_rrcs_data():
        v6_rrcs_label = []
        v6_rrcs = []
        data = Utils.read_csv('exp/csv/rrcs.csv', without_header=True)
        count = 0
        for i in data[1]:
            count = count + 1
            if count % 2 != 0:
                v6_rrcs.append(i)

        count = 0
        for i in data[0]:
            count = count + 1
            if count % 2 != 0:
                v6_rrcs_label.append(i)

        return v6_rrcs, v6_rrcs_label
