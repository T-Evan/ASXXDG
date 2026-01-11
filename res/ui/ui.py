# __init__.py 为初始化加载文件
# 导入-节点检索库
import json
import time
import pymysql

from ascript.android.system import R
# 导入-屏幕检索库
from ascript.android.ui import WebWindow
from ascript.android.ui import Dialog
import threading
import sys
from ascript.android import system
# 向悬浮菜单中新增按钮
from ascript.android.ui import FloatWindow
from ascript.android.system import R
# 导入-屏幕检索库
from ascript.android.ui import WebWindow
# from ascript.android.ui import Loger
from datetime import datetime, timedelta
from time import sleep

config = None


def tunner(k, v):
    global config
    print(k, v)
    # print(k)
    # print(v)

    if k == "guan" and v == "关闭":
        config = "exit"
    if k == "submit":
        res = json.loads(v)
        config = res
        # print(type(config))
    if k == "加载" and v == "成功":
        print('加载成功')


formW = WebWindow(R.ui("ui.html"))
formW.size('100vw', '100vh')
formW.tunner(tunner)  # 在这里设置消息通道
formW.background("#FFFFFF")
formW.show()

while True:
    # print("循环等待中")
    time.sleep(1)
    if config == "exit":
        Dialog.toast('取消执行', 5, 3 | 48, 200, 0)
        system.exit()
    if config:
        Dialog.toast('资源加载中 - 请等待30s', 5, 3 | 48, 200, 0)
        # time.sleep(2)
        break

功能开关 = {}
功能开关 = config


def tunner(k, v):
    print(k, v)


# 调整悬浮窗位置
from ascript.android.ui import FloatWindow

FloatWindow.show(0.01, 0.01, 0.25)
