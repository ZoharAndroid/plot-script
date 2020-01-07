#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zzh
# @Date: 2020/1/7 11:44
import pandas as pd
import numpy as np

data_base_dir = 'datas/'


class Utils:

    @staticmethod
    def read_csv(filename, without_header=False, only_data=False):
        '''
        读取csv文件的数据
        :param filename: 文件名
        :return: header：返回头部信息
                data：返回数据
        '''

        data = []
        if not without_header:  # csv文件包含header的处理方式
            data_frame = pd.read_csv(data_base_dir + filename, header=0)
            if not only_data:  # 返回全部数据
                header = list(data_frame.columns.values)
                for i in header:
                    column_data = data_frame[i].tolist()
                    data.append(column_data)
                return header, data
            else:  # csv文件虽然包含了header，但是只返回数据部分，其他部分不返回
                for i in np.arange(data_frame.columns.size):
                    data.append(data_frame.iloc[1:, i].tolist())
                return data
        else:  # csv文件不包含头部的处理方法
            data_frame = pd.read_csv(data_base_dir + filename, header=None, index_col=False)
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
        data_frame = pd.read_csv(data_base_dir + filename)
        return data_frame[index].tolist()
