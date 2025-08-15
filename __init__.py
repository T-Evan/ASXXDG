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
    # 自动合成()
    while True:
        if 功能开关['集市拍卖'] == 1:
            re = TomatoOcrTap(495, 233, 585, 276, '购买', offsetX=5, offsetY=5, sleep1=0.3)
            # if re:
            #     Toast('刷新购买')
            isFind = False
            for k in range(10):
                re = CompareColors.compare("66,606,#E6DBC5|77,628,#E6E3D6|161,617,#E6DFCE|172,609,#E6E3D6")
                if re:
                    # Toast('进入购买页')
                    isFind = True
                    break
                sleep(0.1)
            if not isFind:
                Toast('未进入购买页')
                continue

            _, countAll = TomatoOcrText(427, 358, 550, 393, '商品数量')
            _, priceAll = TomatoOcrText(481, 400, 635, 433, '商品价格')
            count = safe_float_v2(countAll)
            priceAll = safe_float_v2(priceAll)
            price = round(priceAll / count, 2)
            # Toast(f'最低商品单价：{price}')
            lowPrice = float(功能开关['最低单价'])
            if lowPrice == 0:
                lowPrice = 2
            if price <= 0.0 or price > lowPrice:
                Toast(f'最低商品单价：{price}，价格 > {lowPrice}，等待刷新')
                continue

            Toast(f'最低商品单价：{price}，价格 <= {lowPrice}，开始购买')
            tapSleep(450, 400, 0.2)  # 点击购买
            tapSleep(487, 894, 0.2)  # 点击购买
            tapSleep(470, 774, 0.2)  # 点击购买
            # tapSleep(450, 400, 0.2)  # 点击购买
            # tapSleep(487, 894, 0.2)  # 点击购买
            # tapSleep(470, 774, 0.2)  # 点击购买

            tapSleep(634, 312, 0.2)
        Toast('开始战场任务')
        re = CompareColors.compare("614,1114,#844D31|618,1115,#8C593A|626,1115,#7B4531")
        if re:
            tapSleep(611, 1066)
            Toast('进入战场')
        re = CompareColors.compare("292,1254,#E6A6EF|355,1257,#8486A4|446,1224,#ADAAB5")
        if not re:
            re = CompareColors.compare(
                "604,173,#FFDB9C|625,176,#D67142|600,178,#EFA23A|626,195,#FFDB9C|636,187,#D67542")
            if re:
                tapSleep(628, 176)
                Toast('关闭弹窗')
            else:
                tapSleep(36, 669)

            re = CompareColors.compare("213,1276,#94EBF7|235,1276,#94EBF7")
            if re:
                tapSleep(211, 1275)

            Toast('未进入战场')
            continue

        failTimes = 0
        for k in range(600):
            re = CompareColors.compare("249,400,#FFFFEF|345,407,#FFEB6B|405,399,#FFFF84|468,392,#EFD75A")
            if re:
                tapSleep(631, 339)
                Toast('采集完成')

            re = FindColors.find("230,812,#CE593A|228,820,#CE593A|238,811,#D65D3A|238,819,#D65D3A",
                                 rect=[0, 301, 702, 1164], diff=0.9)
            if re:
                Toast('等待采集中')
                tapSleep(631, 339)
                sleep(5)
                continue

            re = FindColors.find("334,683,#84513A|344,683,#84513A|337,691,#7B513A", rect=[14, 291, 701, 1100],
                                 diff=0.95)

            if not re:
                re = FindColors.find("533,659,#F7D294|540,659,#F7D29C|542,664,#946D4A|530,662,#7B4D31",
                                     rect=[0, 301, 702, 1164], diff=0.9)
            if not re:
                re = FindColors.find("318,749,#63C28C|320,759,#63C28C|359,752,#63C284|359,759,#63BE84",
                                     rect=[0, 301, 702, 1164], diff=0.9)
            if not re:
                re = FindColors.find("402,743,#DEBE84|405,741,#F7D294|388,762,#FFFFFF|388,767,#FFFFFF",
                                     rect=[0, 301, 702, 1164], diff=0.9)
            if not re:
                failTimes = failTimes + 1
            if failTimes > 3:
                Toast('无可采集资源')
                sleep(1)
                break

            if re:
                Toast('开始采集')
                tapSleep(re.x, re.y + 5)
                re = FindColors.find(
                    "382,1025,#FFE352|298,1017,#FFE352|296,1028,#F7DB52|324,1013,#A45510|325,1025,#9C5108|369,1023,#FFE352|374,1022,#F7DB52",
                    rect=[4, 239, 702, 1139], diff=0.95)
                if not re:
                    re = CompareColors.compare("213,1276,#94EBF7|235,1276,#94EBF7")
                    if re:
                        tapSleep(211, 1275)
                    Toast('等待采集中')
                    tapSleep(631, 339)
                    sleep(5)
                    continue

                tapSleep(re.x, re.y)
                tapSleep(94, 708)  # 一键上阵
                tapSleep(528, 1275)  # 开始采集
            re = CompareColors.compare("213,1276,#94EBF7|235,1276,#94EBF7")
            if re:
                tapSleep(211, 1275)

        re = CompareColors.compare("249,400,#FFFFEF|345,407,#FFEB6B|405,399,#FFFF84|468,392,#EFD75A")
        if re:
            tapSleep(631, 339)
            Toast('采集完成')

        tapSleep(353, 1178)  # 打开刷新面板
        re = TomatoOcrTap(132, 1090, 251, 1130, '免费刷新', offsetX=50, offsetY=-80)
        if re:
            Toast('灵气免费刷新')
            tapSleep(356, 912)  # 点击刷新
            tapSleep(358, 907)  # 立即刷新

        re = TomatoOcrTap(298, 1025, 412, 1055, '免费刷新', offsetX=50, offsetY=-80)
        if re:
            Toast('道具免费刷新')
            tapSleep(356, 912)  # 点击刷新
            tapSleep(358, 907)  # 立即刷新

        re = CompareColors.compare("323,1276,#FFFFFF|323,1273,#EFBE8C|374,1276,#FFFFFF|366,1273,#E68629")
        if re:
            Toast('下方免费刷新')
            tapSleep(356, 1210)
            tapSleep(356, 912)  # 点击刷新
            tapSleep(358, 907)  # 立即刷新

        _, daoJuCt = TomatoOcrText(356, 1028, 424, 1054, '道具刷新卡')
        daoJuCt = safe_int_v2(daoJuCt.replace('x', '').replace('X', ''))
        needCt = safe_int_v2(功能开关['道具卡刷新数量'])
        if needCt == 0:
            needCt = 5
        if daoJuCt > 0:
            if daoJuCt > needCt:
                Toast(f'道具刷新卡数量：{daoJuCt} > {needCt}，无需处理')
                sleep(1)
            else:
                Toast(f'道具刷新卡数量：{daoJuCt} <= {needCt}，操作刷新')
                tapSleep(356, 946)
                tapSleep(356, 912)  # 点击刷新
                tapSleep(358, 907)  # 立即刷新
                for m in range(2):
                    re = CompareColors.compare(
                        "604,173,#FFDB9C|625,176,#D67142|600,178,#EFA23A|626,195,#FFDB9C|636,187,#D67542")
                    if re:
                        tapSleep(628, 176)
                        Toast('关闭弹窗')

        re = CompareColors.compare("312,1270,#CE593A|314,1275,#D65D3A|407,1273,#CE593A")
        if re:
            Toast('检查下方刷新')
            tapSleep(352, 1204, 1.2)
            _, daoJuCt = TomatoOcrText(364, 831, 467, 861, '道具刷新卡')
            daoJuCt = safe_int_v2(daoJuCt.replace('x', '').replace('X', ''))
            needCt = safe_int_v2(功能开关['下方卡刷新数量'])
            if needCt == 0:
                needCt = 5
            if daoJuCt > 0:
                if daoJuCt > needCt:
                    Toast(f'下方刷新卡数量：{daoJuCt} > {needCt}，无需处理')
                    sleep(1)
                    tapSleep(634, 172)
                else:
                    Toast(f'下方刷新卡数量：{daoJuCt} <= {needCt}，操作刷新')
                    tapSleep(356, 912)  # 点击刷新
                    tapSleep(358, 907)  # 立即刷新

        tapSleep(336, 293)  # 点击空白返回战场


def 自动合成():
    for k in range(5):
        返回首页()
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
            failTimes = 0
            for k in range(60):
                re, _ = TomatoOcrText(555, 37, 609, 71, '反馈')
                if not re:
                    re = FindColors.find(
                        "667,36,#EFEFEF|675,44,#FEFEFE|682,51,#FDFDFD|682,36,#CCCCCC|668,50,#CCCCCC|694,44,#999999",
                        rect=[641, 11, 702, 74], diff=0.9)
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
                    failTimes = failTimes + 1
                    break
                if failTimes > 4:
                    Toast('无可合成异兽')
                    break
        tapSleep(666, 53, 1.5)
        tapSleep(637, 225, 1.5)  # 空白
        return True
    return False


def 返回首页():
    tapSleep(639, 108, 1.5)  # 空白
    re = CompareColors.compare("611,222,#D68E84|636,235,#DE968C|648,217,#D6867B")
    if re:
        tapSleep(609, 219, 1.5)  # 空白
    re = CompareColors.compare("626,113,#D68A84|645,113,#FFF3B5|661,108,#D68A7B|644,123,#DE9684")
    if re:
        tapSleep(609, 219, 1.5)  # 关闭
    re = CompareColors.compare("180,1178,#F7AA8C|240,1180,#EF9A84|296,1178,#F7AA8C|232,1213,#EF6D5A")
    if re:
        tapSleep(232, 1186, 1.5)  # 战场-取消
    re = TomatoOcrTap(keyword='重试', x1=322, y1=757, x2=397, y2=804, match_mode='fuzzy')
    if re:
        Toast('网络重连')


main()
