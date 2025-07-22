# __init__.py 为初始入口文件,工程代码的入口文件.

from ascript.android.action import click, slide, Touch, gesture
from ascript.android.node import Selector
from ascript.android.screen import capture, FindColors, FindImages, Ocr
from ascript.android import system
from ascript.android.system import R, Device
from .baseUtils import *
from ascript.android.system import ShellListener
from .res.ui.ui import 功能开关

display = Device.display()
# 屏幕宽度
if display.widthPixels != 1080 or display.heightPixels != 1920:
    Toast(f'分辨率为 {display.widthPixels} * {display.heightPixels}，请检查分辨率是否正确')
    Dialog.confirm("屏幕分辨率不为 1080 * 1920，请重新设置", "分辨率错误")
    r = system.shell(f"wm size 1080x1920")
    r = system.shell(f"wm density 480")
    display = Device.display()
    if display.widthPixels != 720 or display.heightPixels != 1280:
        Dialog.confirm("屏幕分辨率已设置为 1080 * 1920", "分辨率已调整")

while True:
    system.open("com.zerophil.worldtalk")
    reAll = FindColors.find_all(
        "577,828,#F9AA23|585,823,#EA5726|589,833,#D72B0B|599,830,#DE2A13|589,849,#E4261A|587,840,#EF822D", diff=0.9)
    print(reAll)
    if reAll:
        for re in reAll:
            print(re)
            online, x, y = imageFind('状态-在线', x1=re.x - 100, y1=re.y - 200, x2=re.x + 80, y2=re.y, confidence1=0.6)
            if not online:
                Toast('用户未在线')
                continue
            if re.y - 150 < 240:
                continue  # 避免点击其他分类

            Toast('点击在线用户')
            tapSleep(re.x - 80, re.y - 150)
            isClick = False
            for k in range(5):
                re = FindColors.find(
                    "362,1624,#26EBD7|326,1654,#26EBD7|393,1661,#26EBD7|362,1687,#26EBD7|355,1664,#26EBD7",
                    rect=[23, 1486, 542, 1903], diff=0.94)
                if re:
                    Toast('进入个人主页')
                    isClick = True
                    break
                sleep(0.3)
            if not isClick:
                Toast('未进入个人主页/未识别到聊天入口')
                action.Key.back()  # 模拟返回键确认输入
                continue

            contentArr = []
            if 功能开关['聊天内容'] != "":
                contentArr.append(功能开关['聊天内容'])
            if 功能开关['聊天内容2'] != "":
                contentArr.append(功能开关['聊天内容2'])
            if 功能开关['聊天内容3'] != "":
                contentArr.append(功能开关['聊天内容3'])
            if 功能开关['聊天内容4'] != "":
                contentArr.append(功能开关['聊天内容4'])
            if 功能开关['聊天内容5'] != "":
                contentArr.append(功能开关['聊天内容5'])
            if len(contentArr) == 0:
                Toast('未配置聊天内容')
                contentArr = ["你好"]

            content = random.choice(contentArr)
            print(content)
            re = FindColors.find(
                "362,1624,#26EBD7|326,1654,#26EBD7|393,1661,#26EBD7|362,1687,#26EBD7|355,1664,#26EBD7",
                rect=[23, 1486, 542, 1903], diff=0.94)
            if re:
                tapSleep(re.x, re.y)
            re = FindColors.find("994,899,#333333|1027,883,#333333|1030,918,#333333|997,937,#333333|1013,909,#353535",
                                 rect=[556, 660, 1056, 1908], diff=0.95)
            if re:
                action.input(content)
                sleep(0.5)
                tapSleep(re.x + 10, re.y + 10)
                Toast('发送聊天')
            for m in range(10):
                re = FindColors.find(
                    "91,1693,#91F6EB|92,1700,#4AEFDE|103,1701,#40EEDC|121,1700,#4AEFDE|111,1693,#333333")
                if re:
                    break
                Toast('返回首页1')
                action.Key.back()  # 模拟返回键确认输入
                system.open("com.zerophil.worldtalk")
                if m > 8:
                    Toast('重启应用')
                    r = system.shell(f"am force-stop com.zerophil.worldtalk")
                if m > 2:
                    system.open("com.zerophil.worldtalk")
                    sleep(2)
                sleep(0.5)

    for m in range(10):
        re = FindColors.find("91,1693,#91F6EB|92,1700,#4AEFDE|103,1701,#40EEDC|121,1700,#4AEFDE|111,1693,#333333")
        if re:
            break
        Toast('返回首页2')
        system.open("com.zerophil.worldtalk")
        action.Key.back()  # 模拟返回键确认输入
        if m > 8:
            Toast('重启应用')
            r = system.shell(f"am force-stop com.zerophil.worldtalk")
        if m > 2:
            system.open("com.zerophil.worldtalk")
            sleep(3)
        sleep(0.5)

    Toast('翻页下一屏')
    tapSleep(267, 149)  # 点击推荐
    swipe(551, 1287, 490, 347)
    swipe(551, 1287, 490, 347)
    sleep(2.5)
