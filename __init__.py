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
if display.widthPixels != 720 or display.heightPixels != 1280:
    Toast(f'分辨率为 {display.widthPixels} * {display.heightPixels}，请检查分辨率是否正确')
    Dialog.confirm("屏幕分辨率不为 720 * 1280，请重新设置", "分辨率错误")
    r = system.shell(f"wm size 720x1280")
    r = system.shell(f"wm density 320")
    display = Device.display()
    if display.widthPixels == 720 or display.heightPixels == 1280:
        Dialog.confirm("屏幕分辨率已设置为 1080 * 1280", "分辨率已调整")


def main():
    startTime = time.time()
    自动合成()
    while True:
        system.open("hb.menghuan.jizhang")

        re = TomatoOcrTap(keyword='战场', x1=33, y1=1224, x2=112, y2=1259, sleep1=2, offsetX=20, offsetY=-30)
        if re:
            Toast('进入战场')

        re = FindColors.find("600,1147,#F7D7C5|607,1150,#F7A26B|591,1174,#A56963|587,1193,#9C5D52|612,1195,#BDDBD6",
                             rect=[475, 907, 674, 1270], diff=0.95)  # 抢夺按钮
        if not re:
            re, _, _ = imageFind('前往', 0.9, 82, 222, 674, 1112)
            if not re:
                Toast('未进入战场')
                tapSleep(639, 108, 1.5)  # 空白
                tapSleep(637, 225, 1.5)  # 空白
                re = TomatoOcrTap(keyword='重试', x1=322, y1=757, x2=397, y2=804, match_mode='fuzzy')
                if re:
                    Toast('网络重连')
                continue

        Toast('准备抢夺')
        tapSleep(580, 1174, 2)  # 抢夺
        re, tmpPoints = imageFindAll('前往', 0.9, 82, 222, 674, 1112)
        for p in tmpPoints:
            tapSleep(580, 1174, 2)  # 抢夺
            Toast('进入抢夺')
            tapSleep(p['center_x'], p['center_y'], 3.5)
            for k in range(10):
                Toast('寻找异兽蛋')
                re = FindColors.find(
                    "394,607,#E6B26B|404,609,#FFEB9C|393,617,#C57D42|399,617,#DE9E5A|396,654,#8CAEAD|410,654,#7B928C",
                    diff=0.9)
                if not re:
                    re = FindColors.find(
                        "505,640,#AD5D31|511,632,#EFBA73|513,640,#C58642|522,642,#C58242|521,626,#FFEFD6",
                        diff=0.9)
                if re:
                    Toast('点击异兽蛋')
                    tapSleep(re.x, re.y, 1.5)
                    re = imageFindClick('掠夺', sleep1=2)
                    if re:
                        re, _ = TomatoOcrText(keyword='取', x1=181, y1=1160, x2=232, y2=1210)
                        if not re:
                            Toast("无可抢夺资源，跳过")
                            break

                        Toast('一键上阵')
                        tapSleep(593, 590, 1.5)
                        Toast('开始掠夺')
                        tapSleep(484, 1185, 1.5)  # 开始
                re = TomatoOcrTap(keyword='取', x1=181, y1=1160, x2=232, y2=1210, sleep1=1)
                if re:
                    Toast('无可上阵异兽，等待中')
                    sleep(10)

        if len(tmpPoints) == 0:
            Toast('界面异常，返回首页')
            tapSleep(639, 108, 1.5)  # 空白
            tapSleep(19, 91, 1.5)  # 返回

        re = FindColors.find("600,1147,#F7D7C5|607,1150,#F7A26B|591,1174,#A56963|587,1193,#9C5D52|612,1195,#BDDBD6",
                             rect=[475, 907, 674, 1270], diff=0.95)  # 抢夺按钮
        if re:
            Toast('刷新抢夺')
            tapSleep(580, 1174, 2)  # 抢夺
        re = TomatoOcrTap(keyword='免费', x1=508, y1=310, x2=595, y2=344, match_mode='fuzzy')
        if re:
            Toast('免费刷新')

        currTime = time.time()
        waitTIme = currTime - startTime
        waitTImeMin = round(waitTIme / 60, 2)

        # 开始一键合成
        if waitTIme > 30:
            startTime = currTime
            Toast(f'已运行{waitTImeMin}/30分，前往一键合成')
            自动合成()

        Toast(f'已运行{waitTImeMin}/30分，等待前往一键合成')
        sleep(2)


def 自动合成():
    for k in range(5):
        re = FindColors.find("12,48,#CE7D73|42,50,#DE9284|22,66,#F7EBB5|28,77,#E6BE94|52,78,#DE968C",
                             rect=[3, 4, 270, 255], diff=0.93)
        if re:
            Toast('返回主页')
            tapSleep(re.x, re.y, 2)
        re, _ = TomatoOcrText(keyword='战场', x1=33, y1=1224, x2=112, y2=1259)
        if re:
            Toast('已返回主页')
            break
    re = TomatoOcrTap(keyword='自动合成', x1=23, y1=839, x2=121, y2=868, sleep1=2, offsetX=10, offsetY=-20)
    if re:
        re = TomatoOcrTap(keyword='合成', match_mode='fuzzy', x1=525, y1=935, x2=622, y2=965, sleep1=2, offsetX=5)
        if not re:
            Toast('未找到一键合成按钮')
        if re:
            for k in range(60):
                re, _ = TomatoOcrText(555, 37, 609, 71, '反馈')
                if re:
                    Toast('广告结束')
                    action.Key.back()
                    break
                re = TomatoOcrTap(251, 893, 454, 937, '继续', match_mode='fuzzy')
                Toast('等待广告结束')
                action.Key.back()
                sleep(1)
                re, _ = TomatoOcrText(keyword='合成', match_mode='fuzzy', x1=525, y1=935, x2=622, y2=965)
                if re:
                    Toast('无可合成异兽')
                    break
        tapSleep(666, 53, 1.5)
        tapSleep(637, 225, 1.5)  # 空白
        return True
    return False


main()
