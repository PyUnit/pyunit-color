# **pyUnit-color** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 日志处理模块集合
[![](https://img.shields.io/badge/Python-3.7-green.svg)](https://pypi.org/project/pyunit-color/)

## 安装
    pip install pyunit-color

### 控制台打印颜色
```python
from pyunit_color import FontColor

def test():
    print(FontColor.red('打印红色'))
    print(FontColor.green('打印绿色'))
    print(FontColor.blue('打印蓝色'))
    print('不打印颜色')

if __name__ == '__main__':
    test()
```

***
[1]: https://blog.jtyoui.com
