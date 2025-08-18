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
if (display.widthPixels != 720 or display.heightPixels != 1280) and (
        display.widthPixels != 1280 or display.heightPixels != 720):
    Toast(f'分辨率为 {display.widthPixels} * {display.heightPixels}，请检查分辨率是否正确')
    Dialog.confirm("屏幕分辨率不为 720 * 1280，请重新设置", "分辨率错误")
    r = system.shell(f"wm size 720x1280")
    r = system.shell(f"wm density 320")
    display = Device.display()
    if (display.widthPixels == 720 or display.heightPixels == 1280) and (
            display.widthPixels == 1280 or display.heightPixels == 720):
        Dialog.confirm("屏幕分辨率已设置为 1080 * 1280", "分辨率已调整")


def main():
    startTime = time.time()
    # 自动合成()
    while True:
        if 功能开关['攻击舰队'] == 1:
            for h in range(3):
                re = TomatoOcrTap(613, 415, 668, 443, '确定', sleep1=2)
                if re:
                    Toast('重新连接')
                re = CompareColors.compare("82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF")
                if re:
                    Toast('返回')
                    tapSleep(91, 42, 1.5)  # 空白

                re = TomatoOcrTap(1017, 651, 1065, 677, '星系', sleep1=3)
                if not re:
                    re = TomatoOcrTap(1185, 651, 1228, 680, '星系', sleep1=3)
                if re:
                    Toast('进入星系')
                if not re:
                    Toast('重置星系页面')
                    re = TomatoOcrTap(1186, 650, 1223, 674, '星云', sleep1=3)
                    continue

                re, _ = TomatoOcrText(1186, 650, 1223, 674, '星云')
                if not re:
                    Toast('未进入星系')
                    re = TomatoOcrTap(616, 417, 663, 440, '确定')
                    re, _ = TomatoOcrText(905, 385, 974, 431, '召回')
                    if re:
                        Toast('关闭召回')
                        tapSleep(74, 271)
                    re = CompareColors.compare("82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF")
                    if re:
                        Toast('返回')
                        tapSleep(91, 42, 1.5)  # 空白
                    sleep(2)
                    continue

                Toast('开始战场任务')
                re = TomatoOcrTap(410, 50, 432, 66, '2D', sleep1=3)
                if re:
                    Toast('切换2D视角')
                isFind = False
                for k in range(16):
                    isFind = imageFindClick('舰队4级', confidence1=0.85, offsetX=5, offsetY=3, x1=82, y1=148, x2=1151,
                                            y2=628)
                    # re = FindColors.find(
                    #     "363,203,#F7954A|370,195,#FA974B|370,206,#FA974B|371,205,#FA974B|370,217,#FA974B|377,218,#FA974B|387,215,#F7954A",
                    #     diff=0.9)
                    # if not re:
                    #     re = FindColors.find(
                    #         "440,268,#FA974B|441,277,#FA974B|435,276,#F19248|441,286,#FA974B|448,286,#FA974B|458,286,#F7954A",
                    #         diff=0.9)
                    # if not re:
                    #     re = FindColors.find(
                    #         "346,649,#F9974B|345,658,#F9974B|339,661,#F9974B|344,669,#F9974B|350,670,#F9974B|359,668,#F29349",
                    #         diff=0.9)
                    if not isFind:
                        isFind = imageFindClick('舰队4级-2', confidence1=0.8, offsetX=5, offsetY=3, x1=82, y1=148,
                                                x2=1151,
                                                y2=628)
                    if not isFind:
                        isFind = imageFindClick('舰队4级-3', confidence1=0.85, offsetX=5, offsetY=3, x1=82, y1=148,
                                                x2=1151,
                                                y2=628)
                    if not isFind:
                        isFind = imageFindClick('舰队4级-4', confidence1=0.8, offsetX=5, offsetY=3, x1=82, y1=148,
                                                x2=1151,
                                                y2=628)
                    if not isFind:
                        isFind = imageFindClick('舰队', confidence1=0.7, offsetX=5, offsetY=3, x1=82, y1=148,
                                                x2=1151,
                                                y2=628)
                    if not isFind:
                        Toast('未找到舰队')
                        if k < 2:
                            swipe(591, 522, 585, 197)
                            sleep(1.7)
                        if 4 > k >= 2:
                            swipe(585, 197, 591, 522)
                            sleep(1.7)
                        if 6 > k >= 4:
                            swipe(585, 197, 591, 522)
                            # swipe(834, 422, 245, 374)
                            sleep(1.7)
                        if 8 > k >= 6:
                            swipe(591, 522, 585, 197)
                            # swipe(245, 374, 834, 422)
                            sleep(1.7)
                        if 10 > k >= 8:
                            swipe(245, 374, 834, 422)
                            sleep(1.7)
                        if 12 > k >= 10:
                            swipe(834, 422, 245, 374)
                            sleep(1.7)
                        if 14 > k >= 12:
                            swipe(834, 422, 245, 374)
                            sleep(1.7)
                        if 16 > k >= 14:
                            swipe(245, 374, 834, 422)
                            sleep(1.7)
                        continue
                    if isFind:
                        # 判断是否在星系
                        re = CompareColors.compare("82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF")
                        if re:
                            Toast('返回')
                            tapSleep(91, 42, 1.5)  # 空白
                        else:
                            break
                if not isFind:
                    Toast('未找到舰队')
                    continue
                # tapSleep(re.x, re.y, 1)
                ifFind = False
                for k in range(3):
                    ifFind = TomatoOcrTap(897, 388, 962, 428, '攻击')
                    if ifFind:
                        break
                    sleep(1)
                if not ifFind:
                    Toast('未找到攻击按钮')
                    continue
                re = TomatoOcrTap(1117, 114, 1197, 145, '快速维修')
                if re:
                    Toast('快速维修')
                Toast('选择舰队')
                # re = TomatoOcrTap(788, 621, 863, 648, '选择全部')
                # if not re:
                #     Toast('未找到舰队选择入口')
                #     continue
                tapSleep(1008, 140, 1.2)  # 点击第一舰队
                re = TomatoOcrTap(1025, 617, 1082, 651, '确定', offsetX=5, offsetY=8)
                if not re:
                    re = TomatoOcrTap(874, 621, 920, 647, '确定', offsetX=5, offsetY=8)
                if not re:
                    re = TomatoOcrFindRangeClick('确定', x1=651, y1=459, x2=1117, y2=702, offsetX=5, offsetY=8)
                if not re:
                    Toast('未找到舰队确认入口')
                    continue

                failTimes = 0
                for k in range(225):
                    re, _, _ = imageFind('00计时', confidence1=0.8)
                    if not re:
                        Toast(f'跃迁状态识别失败-{failTimes}/5')
                        re, _, _ = imageFind('战斗中', confidence1=0.9, x1=1097, y1=314, x2=1266, y2=616)
                        if re:
                            Toast(f'进入战斗状态')
                            break
                        failTimes += 1
                        sleep(0.5)
                    if failTimes > 5:
                        Toast('跃迁结束')
                        break
                    wait = 2 * k
                    Toast(f'等待跃迁{wait}/450s')
                    sleep(2)

                failTimes = 0
                isDone = False
                for k in range(200):
                    re = FindColors.find(
                        "1200,456,#A2070A|1198,463,#FFC9C9|1209,462,#FFC9C9|1210,478,#BC5D44|1198,476,#FFC9C9",
                        rect=[1097, 314, 1266, 616], diff=0.95)
                    if not re:
                        re, _, _ = imageFind('战斗中', confidence1=0.9, x1=1097, y1=314, x2=1266, y2=616)
                    if not re:
                        Toast(f'战斗状态识别失败-{failTimes}/3')
                        failTimes += 1
                    if failTimes > 3:
                        isDone = True
                        Toast('战斗结束')
                        break
                    Toast('战斗中')
                    sleep(2)
                if isDone:
                    break
        if 功能开关['采集残骸'] == 1:
            for k in range(5):
                noCaiJi = False
                re = imageFindClick('舰队残骸', confidence1=0.7, offsetX=2, x1=80, y1=177, x2=1245,
                                    y2=662)
                if not re:
                    re = imageFindClick('舰队残骸-2', confidence1=0.7, offsetX=2, x1=80, y1=177, x2=1245,
                                        y2=662)
                if re:
                    Toast('点击残骸')
                    sleep(1)
                    for m in range(3):
                        ifFind = TomatoOcrTap(906, 379, 964, 410, '采集', offsetX=5, offsetY=5)
                        re, _ = TomatoOcrText(906, 379, 964, 410, '召回')
                        if re:
                            break
                        if ifFind:
                            re = TomatoOcrTap(616, 417, 663, 440, '确定')
                            if re:
                                tapSleep(165, 385)  # 返回主页
                                noCaiJi = True
                                Toast('没有可用的采集船')
                            break
                        sleep(1)
                    re = CompareColors.compare("82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF")
                    if re:
                        Toast('返回')
                        tapSleep(91, 42, 1.5)  # 空白
                    tapSleep(34, 374)  # 空白
                if noCaiJi:
                    break
                sleep(1)

        if 功能开关['快速维修'] == 1:
            re = imageFindClick('右侧菜单-2', confidence1=0.7, offsetX=2, x1=1114, y1=271, x2=1274,
                                y2=640)
            if not re:
                re = FindColors.find("1200,457,#C3ECF8|1197,491,#B2B3B4|1200,457,#C3ECF8", diff=0.95)
                if re:
                    tapSleep(re.x, re.y)
            if re:
                re = TomatoOcrTap(1171, 145, 1211, 171, '舰队')
                if re:
                    re = TomatoOcrFindRangeClick('悬停召回', x1=792, y1=85, x2=1094, y2=145)
                    if re:
                        Toast('悬停召回')
                    for k in range(30):
                        re, _, _ = TomatoOcrFindRange('加速', x1=957, y1=142, x2=1085, y2=462)
                        if not re:
                            Toast('已召回')
                            break
                        re = TomatoOcrTap(1171, 145, 1211, 171, '舰队')
                        if not re:
                            Toast('非召回状态')
                            break
                        wait = k * 2
                        Toast(f'等待召回{wait}/60s')
                        sleep(2)
                    re = TomatoOcrFindRangeClick('快速维修', x1=959, y1=79, x2=1082, y2=274)
                    if re:
                        Toast('快速维修')
                    tapSleep(165, 385)  # 返回主页


main()
