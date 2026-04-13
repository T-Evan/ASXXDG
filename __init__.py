# __init__.py 为初始入口文件,工程代码的入口文件.

from ascript.android.action import click, slide, Touch, gesture
from ascript.android.node import Selector
from ascript.android.screen import capture, FindColors, FindImages, Ocr
from ascript.android import system
from ascript.android.system import R, Device
from .baseUtils import *
from ascript.android.system import ShellListener
from .res.ui.ui import 功能开关
from ascript.android import action
from ascript.android.action import Path
from .target_templates import *
from .target_utils import *

display = Device.display()
# 屏幕宽度
if display.widthPixels != 1280 or display.heightPixels != 720:
    Toast(
        f"分辨率为 {display.widthPixels} * {display.heightPixels}，请检查分辨率是否正确"
    )
    Dialog.confirm("屏幕分辨率不为横向 720 * 1280，请重新设置并进入游戏", "分辨率错误")
    # r = system.shell(f"wm size 720x1280")
    # r = system.shell(f"wm density 320")
    display = Device.display()
    if display.widthPixels == 1280 or display.heightPixels == 720:
        Dialog.confirm("屏幕分辨率已设置为 720 * 1280", "分辨率已调整")


def 清理干扰弹窗():
    re = TomatoOcrTap(613, 415, 668, 443, "确定", sleep1=2)
    if re:
        Toast("重新连接")
    re, _ = TomatoOcrText(470, 40, 780, 110, "获得物品", match_mode="fuzzy")
    if not re:
        re, _ = TomatoOcrText(560, 660, 720, 705, "点击关闭", match_mode="fuzzy")
    if re:
        Toast("关闭获得物品弹窗")
        tapSleep(640, 682, 1.5)
    re = CompareColors.compare("82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF")
    if re:
        Toast("返回")
        tapSleep(91, 42, 1.5)  # 空白

    re, _ = TomatoOcrText(537, 320, 737, 360, "是否前往", match_mode="fuzzy")
    if re:
        Toast("取消前往星系")
        tapSleep(894, 268, 1.5)
    re, _ = TomatoOcrText(18, 616, 151, 681, "管理", match_mode="fuzzy")
    if re:
        Toast("关闭坐标管理")
        tapSleep(285, 28, 1.5)
    re, _ = TomatoOcrText(654, 589, 696, 613, "建造", match_mode="fuzzy")
    if not re:
        re, _ = TomatoOcrText(0, 600, 160, 690, "建造", match_mode="fuzzy")
    if not re:
        re = CompareColors.compare(
            "1174,80,#AAA28A|1180,85,#8D856F|1188,77,#938D74|1205,54,#FDFDFE"
        )
    if re:
        Toast("取消恒星建造")
        tapSleep(1240, 325, 1.5)
    re, _ = TomatoOcrText(1171, 145, 1211, 171, "舰队")
    if re:
        Toast("取消舰队管理")
        tapSleep(328, 240, 1.5)
    re, _ = TomatoOcrText(343, 121, 444, 155, "坐标清单", match_mode="fuzzy")
    if not re:
        re, _ = TomatoOcrText(453, 366, 565, 395, "世界聊天", match_mode="fuzzy")
    if not re:
        re, _ = TomatoOcrText(714, 366, 828, 395, "联盟聊天", match_mode="fuzzy")
    if not re:
        re, _ = TomatoOcrText(712, 425, 827, 458, "组织聊天", match_mode="fuzzy")
    if re:
        Toast("关闭坐标分享页")
        tapSleep(117, 42, 1.5)


def 进入星系并准备战场(h, failCt):
    if 功能开关["仅寻找当前位置"] == 0:
        re = TomatoOcrTap(1013, 648, 1063, 680, "星系", sleep1=6, offsetX=5, offsetY=5)
        if not re:
            re = TomatoOcrFindRangeClick(
                x1=923,
                y1=606,
                x2=1247,
                y2=712,
                keyword="星系",
                sleep1=6,
                offsetX=5,
                offsetY=5,
            )
        if re:
            Toast("进入星系")
        if not re:
            re = CompareColors.compare("82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF")
            if re:
                Toast("返回")
                tapSleep(91, 42, 1.5)  # 空白
            re = CompareColors.compare("1245,34,#FFFFFF|1248,34,#FFFFFF")
            if re:
                Toast("返回")
                tapSleep(377, 20, 1.5)  # 舰队管理页空白
            re = imageFindClick(
                "返回-2",
                confidence1=0.8,
                offsetX=5,
                offsetY=3,
                x1=105,
                y1=22,
                x2=1257,
                y2=351,
            )
            if re:
                Toast("关闭任务页面")
            re, _ = TomatoOcrText(0, 600, 160, 690, "建造", match_mode="fuzzy")
            if re:
                Toast("取消左侧建造")
                tapSleep(1240, 325, 1.5)
            Toast(f"重置星系页面，倒计时{5 - failCt}次")
            failCt = failCt + 1
            re = TomatoOcrTap(
                1180, 647, 1238, 684, "星系", sleep1=4, match_mode="fuzzy"
            )
            if not re:
                re = TomatoOcrTap(
                    1180,
                    647,
                    1238,
                    684,
                    "星云",
                    sleep1=4,
                    match_mode="fuzzy",
                )
            if not re:
                re = TomatoOcrFindRangeClick("星", x1=915, y1=595, x2=1249, y2=698)
            return False, failCt

    failCt = 0
    isFind = False
    for k in range(4):
        isFind, _ = TomatoOcrText(1001, 648, 1067, 681, "空间站")
        if not isFind:
            Toast(f"等待进入星系，倒计时{12 - k * 3}s")
            sleep(3)
    if not isFind:
        Toast("未进入星系")
        re = TomatoOcrTap(616, 417, 663, 440, "确定")
        re, _ = TomatoOcrText(905, 385, 974, 431, "召回")
        if re:
            Toast("关闭召回")
            tapSleep(74, 271)
        re, _ = TomatoOcrText(18, 616, 151, 681, "坐标管理", match_mode="fuzzy")
        if re:
            Toast("关闭坐标管理")
            tapSleep(285, 28, 1.5)
        re = CompareColors.compare("82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF")
        if re:
            Toast("返回")
            tapSleep(91, 42, 1.5)  # 空白
        re = CompareColors.compare("1245,34,#FFFFFF|1248,34,#FFFFFF")
        if re:
            Toast("返回")
            tapSleep(377, 20, 1.5)  # 舰队管理页空白
        re, _ = TomatoOcrText(1171, 145, 1211, 171, "舰队")
        if re:
            Toast("取消舰队管理")
            tapSleep(328, 240, 1.5)
        re = TomatoOcrTap(1189, 652, 1229, 676, "星系")
        if re:
            Toast("进入星系")
        sleep(2)
        return False, failCt

    Toast("开始战场任务")
    re = TomatoOcrTap(410, 50, 432, 66, "2D", sleep1=5)
    if re:
        Toast("切换2D视角")

    if h == 2:
        Toast("缩放视角")
        line1 = Path(0, 700)
        line1.moveTo(1105, 340)
        line1.lineTo(871, 425)
        # 模拟第二根手指
        line2 = Path(0, 700)
        line2.moveTo(774, 505)
        line2.lineTo(882, 420)
        action.gesture([line1, line2])
        sleep(1)
    if h == 3:
        Toast("放大视角")
        line1 = Path(0, 700)
        line1.moveTo(871, 425)
        line1.lineTo(1105, 340)
        # 模拟第二根手指
        line2 = Path(0, 700)
        line2.moveTo(882, 420)
        line2.lineTo(774, 505)
        action.gesture([line1, line2])
        sleep(1)

    # 定位空间站，优先寻找空间站附近目标
    re1 = imageFindClick(
        "空间站",
        confidence1=0.85,
        offsetX=2,
        offsetY=2,
        x1=97,
        y1=168,
        x2=1162,
        y2=634,
        rgb=True,
    )
    if not re1:
        re1 = imageFindClick(
            "空间站2",
            confidence1=0.85,
            offsetX=2,
            offsetY=2,
            x1=97,
            y1=168,
            x2=1162,
            y2=634,
            rgb=True,
        )
    if not re1:
        re1 = imageFindClick(
            "空间站3",
            confidence1=0.85,
            offsetX=2,
            offsetY=2,
            x1=97,
            y1=168,
            x2=1162,
            y2=634,
            rgb=True,
        )
    if re1:
        Toast("已找到空间站，优先寻找附近目标")
        tapSleep(488, 25)

    return True, failCt


def 清理战场内弹窗():
    re, _ = TomatoOcrText(470, 40, 780, 110, "获得物品", match_mode="fuzzy")
    if not re:
        re, _ = TomatoOcrText(560, 660, 720, 705, "点击关闭", match_mode="fuzzy")
    if re:
        Toast("关闭获得物品弹窗")
        tapSleep(640, 682, 1.5)
    re, _ = TomatoOcrText(1171, 145, 1211, 171, "舰队")
    if re:
        Toast("取消舰队管理")
        tapSleep(328, 240, 1.5)
    re, _ = TomatoOcrText(343, 121, 444, 155, "坐标清单", match_mode="fuzzy")
    if not re:
        re, _ = TomatoOcrText(453, 366, 565, 395, "世界聊天", match_mode="fuzzy")
    if not re:
        re, _ = TomatoOcrText(714, 366, 828, 395, "联盟聊天", match_mode="fuzzy")
    if not re:
        re, _ = TomatoOcrText(712, 425, 827, 458, "组织聊天", match_mode="fuzzy")
    if re:
        Toast("关闭坐标分享页")
        tapSleep(117, 42, 1.5)
    re, _ = TomatoOcrText(18, 616, 151, 681, "坐标管理", match_mode="fuzzy")
    if re:
        Toast("关闭坐标管理")
        tapSleep(285, 28, 1.5)
    re = CompareColors.compare("82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF")
    if re:
        Toast("取消活动页")
        tapSleep(80, 51, 1.5)


def 执行残骸采集(已处理残骸坐标):
    noCaiJi = False
    for b in range(2):
        if noCaiJi:
            break
        Toast("寻找舰队残骸")
        当前残骸模板 = list(残骸目标模板)
        if 功能开关["水晶残骸"] == 1:
            Toast("寻找水晶残骸")
            当前残骸模板.extend(水晶残骸目标模板)
        if 功能开关["合金残骸"] == 1:
            Toast("寻找合金残骸")
            当前残骸模板.extend(合金残骸目标模板)
        if 功能开关["天启残骸"] == 1:
            Toast("寻找天启残骸")
            当前残骸模板.extend(天启残骸目标模板)
        当前残骸目标 = 查找未处理目标("残骸", 当前残骸模板, 已处理残骸坐标)
        if 当前残骸目标:
            cx = 当前残骸目标["x"]
            cy = 当前残骸目标["y"]
            colors = f"{cx - 5},{cy - 9},#8CFF92|{cx - 8},{cy - 5},#8CFF92|{cx - 10},{cy - 2},#8CFF92"
            rect = [cx - 10, cy - 10, cx + 10, cy + 10]
            res = FindColors.find_all(colors, rect=rect, diff=0.95)
            if res and len(res) > 0:
                Toast("残骸正在采集中，跳过")
                记录已处理坐标("残骸", 当前残骸目标, 已处理残骸坐标)
                continue
            点击目标(当前残骸目标)
            # 异常处理
            re, _ = TomatoOcrText(1171, 145, 1211, 171, "舰队")
            if re:
                Toast("取消舰队管理")
                tapSleep(328, 240, 1.5)

            Toast("点击残骸")
            sleep(1)
            for m in range(3):
                ifFind = TomatoOcrTap(906, 379, 964, 410, "采集", offsetX=5, offsetY=5)
                re, _ = TomatoOcrText(906, 379, 964, 410, "召回")
                if re:
                    noCaiJi = True
                    break
                if ifFind:
                    re = TomatoOcrTap(616, 417, 663, 440, "确定")
                    if re:
                        # tapSleep(17,414)  # 返回主页
                        noCaiJi = True
                        Toast("没有可用的采集船")
                    else:
                        记录已处理坐标("残骸", 当前残骸目标, 已处理残骸坐标)
                    break
                sleep(1)
            re = CompareColors.compare("82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF")
            if re:
                Toast("返回")
                tapSleep(91, 42, 1.5)  # 空白
        if noCaiJi:
            break
        sleep(0.3)
    return noCaiJi


def 执行搜索滑动(k):
    if 功能开关["仅寻找当前位置"] == 0:
        if k < 2:
            swipe(591, 522, 585, 197)  # 上划
            sleep(1.7)
        elif 3 > k >= 2:
            swipe(245, 374, 834, 422)  # 左到右划
            sleep(1.7)
        elif 5 > k >= 3:
            swipe(934, 422, 245, 374)  # 右到左划
            sleep(1.7)
        elif 6 > k >= 5:
            swipe(245, 374, 934, 422)  # 左到右划
            sleep(1.7)
        # 下划配合左右滑动
        elif 8 > k >= 6:
            swipe(585, 197, 591, 522)  # 下划
            sleep(1.7)
        elif 9 > k >= 8:
            swipe(245, 374, 834, 422)  # 左到右划
            sleep(1.7)
        elif 11 > k >= 9:
            swipe(934, 422, 245, 374)  # 右到左划
            sleep(1.7)
        elif 12 > k >= 11:
            swipe(245, 374, 934, 422)  # 左到右划
            sleep(1.7)
        # 下划配合左右滑动
        elif 14 > k >= 12:
            swipe(585, 197, 591, 522)  # 下划
            sleep(1.7)
        elif 15 > k >= 14:
            swipe(245, 374, 834, 422)  # 左到右划
            sleep(1.7)
        elif 17 > k >= 15:
            swipe(934, 422, 245, 374)  # 右到左划
            sleep(1.7)
        elif 18 > k >= 17:
            swipe(245, 374, 934, 422)  # 左到右划
            sleep(1.7)


def 等待战斗完成(fightType, 已处理清道夫战斗群坐标):
    # 等待跃迁和战斗完成
    failTimes = 0
    for k in range(225):
        if fightType == "清道夫舰队":
            re = 寻找清道夫战斗群(已处理清道夫战斗群坐标)
            if re == 1:
                fightType = "清道夫战斗群"
        re, _, _ = imageFind("00计时", confidence1=0.8)
        if not re:
            re, _, _ = imageFind("00计时-2", confidence1=0.75)
        if not re:
            Toast(f"跃迁状态识别失败，倒计时{5 - failTimes}次")
            re, _, _ = imageFind(
                "战斗中",
                confidence1=0.8,
                x1=1097,
                y1=314,
                x2=1266,
                y2=616,
            )
            if re:
                Toast(f"进入战斗状态")
                break
            failTimes += 1
            sleep(0.5)
        if failTimes > 5:
            Toast("跃迁结束")
            break
        wait = 2 * k
        Toast(f"等待跃迁，倒计时{450 - wait}s")
        sleep(2)

    failTimes = 0
    isDone = False
    for k in range(200):
        if fightType == "清道夫舰队":
            re = 寻找清道夫战斗群(已处理清道夫战斗群坐标)
            if re == 1:
                fightType = "清道夫战斗群"
        re = FindColors.find(
            "1200,456,#A2070A|1198,463,#FFC9C9|1209,462,#FFC9C9|1210,478,#BC5D44|1198,476,#FFC9C9",
            rect=[1097, 314, 1266, 616],
            diff=0.95,
        )
        if not re:
            re, _, _ = imageFind(
                "战斗中",
                confidence1=0.8,
                x1=1097,
                y1=314,
                x2=1266,
                y2=616,
            )
        if not re:
            Toast(f"战斗状态识别失败，倒计时{5 - failTimes}次")
            failTimes += 1
        if failTimes > 5:
            isDone = True
            Toast("战斗结束")
            break
        Toast(f"战斗中，倒计时{400 - k * 2}s")
        sleep(2)
    return fightType


def 执行战后快速维修():
    if 功能开关["快速维修"] != 1:
        return
    re = imageFindClick(
        "右侧菜单-2",
        confidence1=0.7,
        offsetX=2,
        x1=1114,
        y1=271,
        x2=1274,
        y2=640,
    )
    if not re:
        re = FindColors.find(
            "1200,457,#C3ECF8|1197,491,#B2B3B4|1200,457,#C3ECF8",
            diff=0.95,
        )
        if re:
            tapSleep(re.x, re.y)
    if not re:
        re = True
        tapSleep(1180, 449)
    if re:
        re = TomatoOcrTap(1171, 145, 1211, 171, "舰队")
        if re:
            re = TomatoOcrFindRangeClick("悬停召回", x1=792, y1=85, x2=1094, y2=145)
            if re:
                Toast("悬停召回")
            for k in range(30):
                re, _, _ = TomatoOcrFindRange("加速", x1=957, y1=142, x2=1085, y2=462)
                if not re:
                    Toast("已召回")
                    break
                re = TomatoOcrTap(1171, 145, 1211, 171, "舰队")
                if not re:
                    Toast("非召回状态")
                    break
                wait = k * 2
                Toast(f"等待召回，倒计时{60 - wait}s")
                sleep(2)
            if 功能开关["快速维修"] == 1:
                re = TomatoOcrFindRangeClick("快速维修", x1=959, y1=79, x2=1082, y2=274)
                if re:
                    Toast("快速维修")
                    TomatoOcrTap(611, 414, 671, 445, "确定")
        tapSleep(165, 385)  # 返回主页


def main():
    startTime = time.time()
    已处理残骸坐标 = {}
    已处理清道夫战斗群坐标 = {}
    已处理清道夫舰队坐标 = {}
    attack_failed = False
    fightType = ""
    # 自动合成()
    while True:
        failCt = 0
        if 功能开关["攻击舰队"] == 1 or 功能开关["采集残骸"] == 1:
            isFind = False
            noCaiJi = False
            attack_failed = False
            fightType = ""
            for h in range(3):
                清理干扰弹窗()

                if failCt > 4:
                    tapSleep(328, 240, 1.5)
                    tapSleep(362, 8, 1.5)

                ready, failCt = 进入星系并准备战场(h, failCt)
                if not ready:
                    continue

                isFind = False
                noCaiJi = False
                attack_failed = False
                fightType = ""
                for k in range(18):
                    清理战场内弹窗()

                    if 功能开关["采集残骸"] == 1:
                        noCaiJi = 执行残骸采集(已处理残骸坐标)

                    fightType = ""
                    if 功能开关["攻击舰队"] == 1 and 功能开关["清道夫战斗群"] == 1:
                        isFind = False
                        Toast("寻找清道夫战斗群")
                        re = 寻找清道夫战斗群(已处理清道夫战斗群坐标)
                        if re == 1:
                            isFind = True
                            fightType = "清道夫战斗群"
                        if re == -1:
                            attack_failed = True
                            continue

                    if (
                        功能开关["攻击舰队"] == 1
                        and not isFind
                        and 功能开关["清道夫舰队"] == 1
                    ):
                        isFind = False
                        Toast("寻找清道夫舰队")
                        当前清道夫舰队目标 = 查找未处理目标(
                            "清道夫舰队", 清道夫舰队目标模板, 已处理清道夫舰队坐标
                        )
                        if 当前清道夫舰队目标:
                            点击目标(当前清道夫舰队目标)
                            Toast("目标获取-清道夫舰队")
                            fightType = "清道夫舰队"
                            attack_result = 选择舰队攻击(fightType)
                            if not attack_result:
                                attack_failed = True
                                continue
                            记录已处理坐标(
                                "清道夫舰队", 当前清道夫舰队目标, 已处理清道夫舰队坐标
                            )
                            isFind = True

                    if not isFind:
                        Toast("未找到舰队")
                        执行搜索滑动(k)
                        continue

                    if isFind:
                        re = CompareColors.compare(
                            "82,37,#FFFFFF|77,45,#FDFDFD|82,51,#FFFFFF"
                        )
                        if re:
                            Toast("返回")
                            tapSleep(91, 42, 1.5)

                if not isFind and 功能开关["采集残骸"] != 1:
                    Toast("未找到目标舰队")
                    continue

                should_wait_for_battle = noCaiJi or attack_failed
                if should_wait_for_battle:
                    fightType = 等待战斗完成(fightType, 已处理清道夫战斗群坐标)
                    attack_failed = False

                执行战后快速维修()
                continue


def 选择舰队攻击(fightType=""):
    ifFind = False
    sleep(1)
    for k in range(3):
        ifFind = TomatoOcrTap(897, 388, 962, 428, "攻击")
        if ifFind:
            break
        sleep(1)
    if not ifFind:
        ifFind = TomatoOcrFindRangeClick(
            "攻击",
            x1=785,
            y1=148,
            x2=1085,
            y2=605,
            offsetX=5,
            offsetY=8,
            match_mode="fuzzy",
            sleep1=1,
        )
    if not ifFind:
        Toast("未找到攻击按钮")
        return False
    sleep(1)
    if 功能开关["快速维修"] == 1:
        re = TomatoOcrTap(1117, 114, 1197, 145, "快速维修", sleep1=1.5)
        if not re:
            re = TomatoOcrTap(1117, 115, 1199, 142, "快速维修", sleep1=1.5)
        if not re:
            re = TomatoOcrTap(1114, 117, 1208, 145, "快速维修", sleep1=1.5)
        if not re:
            re = TomatoOcrFindRangeClick(
                "维修",
                x1=1077,
                y1=25,
                x2=1254,
                y2=600,
                offsetX=1,
                offsetY=1,
                match_mode="fuzzy",
                sleep1=1.5,
            )
        if re:
            Toast("快速维修")
            TomatoOcrTap(611, 414, 671, 445, "确定")
    Toast("选择舰队")
    if 功能开关["智能分配"] == 1:
        if fightType == "清道夫舰队":
            count = TomatoOcrCountRange(
                "悬停", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy"
            )
            if count < 2:
                count = TomatoOcrCountRange(
                    "母港", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy"
                )
                if count < 2:
                    Toast("无可用舰队")
                    sleep(0.5)
                    tapSleep(511, 62)
                    return False
        else:
            re, _, _ = TomatoOcrFindRange(
                "母港", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy"
            )
            if not re:
                re, _, _ = TomatoOcrFindRange(
                    "悬停", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy"
                )
            if not re:
                Toast("无可用舰队")
                sleep(0.5)
                tapSleep(511, 62)
                return False

        if fightType == "清道夫战斗群":
            Toast("精英，第一舰队攻击")
            tapSleep(1008, 140, 1.2)  # 点击第一舰队
        if fightType == "清道夫舰队":
            Toast("普通，其余舰队攻击")
            re = imageFindClick(
                "选择全部",
                confidence1=0.8,
                offsetX=5,
                offsetY=3,
                x1=750,
                y1=268,
                x2=1270,
                y2=708,
            )
            re = CompareColors.compare("794,137,#C5E6FF|797,140,#C4E5FE")
            if re:
                tapSleep(1008, 140, 1)  # 点击第一舰队取消
    elif 功能开关["全部舰队"] == 1:
        Toast("全部舰队")
        re, _, _ = TomatoOcrFindRange(
            "母港", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy"
        )
        if not re:
            re, _, _ = TomatoOcrFindRange(
                "悬停", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy"
            )
        if not re:
            Toast("无可用舰队")
            tapSleep(511, 62)
            return False
        re = TomatoOcrTap(662, 620, 748, 651, "选择全部", offsetX=5, offsetY=8)
        if not re:
            re = TomatoOcrFindRangeClick(
                "全部",
                x1=768,
                y1=348,
                x2=1237,
                y2=711,
                offsetX=5,
                offsetY=3,
                match_mode="fuzzy",
                sleep1=1,
            )
    elif 功能开关["单独派遣"] == 1:
        Toast("单独派遣")
        re, _, _ = TomatoOcrFindRange(
            "母港", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy"
        )
        if not re:
            re, _, _ = TomatoOcrFindRange(
                "悬停", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy"
            )
        if not re:
            Toast("无可用舰队")
            tapSleep(511, 62)
            return False

        re = TomatoOcrFindRangeClick(
            "母港",
            x1=994,
            y1=37,
            x2=1262,
            y2=677,
            offsetX=5,
            offsetY=8,
            match_mode="fuzzy",
            sleep1=1,
        )
        if not re:
            re = TomatoOcrFindRangeClick(
                "悬停",
                x1=994,
                y1=37,
                x2=1262,
                y2=677,
                offsetX=5,
                offsetY=8,
                match_mode="fuzzy",
                sleep1=1,
            )
        if not re:
            Toast("单独派遣失败，选择默认舰队")
            re = TomatoOcrFindRangeClick(
                "全部",
                x1=768,
                y1=348,
                x2=1237,
                y2=711,
                offsetX=5,
                offsetY=8,
                match_mode="fuzzy",
                sleep1=1,
            )
    else:
        Toast("选择默认舰队")
        re = TomatoOcrFindRangeClick(
            "母港", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy", sleep1=1
        )
        if not re:
            re = TomatoOcrFindRangeClick(
                "悬停", x1=994, y1=37, x2=1262, y2=677, match_mode="fuzzy", sleep1=1
            )
        if not re:
            tapSleep(1008, 140, 1.2)  # 点击第一舰队
    re = TomatoOcrTap(1025, 617, 1082, 651, "确定", offsetX=5, offsetY=8)
    if not re:
        re = TomatoOcrTap(874, 621, 920, 647, "确定", offsetX=5, offsetY=8)
    if not re:
        re = TomatoOcrTap(868, 617, 928, 654, "确定", offsetX=5, offsetY=8)
    if not re:
        re = TomatoOcrFindRangeClick(
            "确定", x1=651, y1=459, x2=1117, y2=702, offsetX=5, offsetY=8
        )
    if not re:
        Toast("未找到舰队确认入口")
        return False

    re, _, _ = TomatoOcrFindRange("确定", x1=651, y1=459, x2=1117, y2=702)
    if re:
        Toast("无可用舰队")
        tapSleep(365, 620, 1.2)  # 取消
        return False
    return True


def 寻找清道夫战斗群(已处理清道夫战斗群坐标):
    当前清道夫战斗群目标 = 查找未处理目标(
        "清道夫战斗群", 清道夫战斗群目标模板, 已处理清道夫战斗群坐标
    )
    if 当前清道夫战斗群目标:
        点击目标(当前清道夫战斗群目标)
        Toast("目标获取-清道夫战斗群")
        fightType = "清道夫战斗群"
        re = 选择舰队攻击(fightType)
        if not re:
            Toast("清道夫战斗群-寻找失败")
            return -1
        记录已处理坐标("清道夫战斗群", 当前清道夫战斗群目标, 已处理清道夫战斗群坐标)
        Toast("清道夫战斗群-寻找成功")
        return 1
    return 0


main()
