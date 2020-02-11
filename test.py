#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/2/11 13:30
# @Author: Jtyoui@qq.com
from pyunit_color import FontColor


def test():
    print(FontColor.red('打印红色'))
    print(FontColor.green('打印绿色'))
    print(FontColor.blue('打印蓝色'))
    print('不打印颜色')


if __name__ == '__main__':
    test()
