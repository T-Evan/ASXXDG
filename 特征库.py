from ascript.android import plug
from ascript.android.ui import Dialog
from ascript.android.screen import FindImages

# 导入上下文环境包,方便导入图片地址
from ascript.android.system import R
from ascript.android import action
from ascript.android.screen import CompareColors
import time


def swipe(x1, y1, x2, y2, dur=500):
    # print(x1, y1, x2, y2)
    action.slide(x1, y1, x2, y2, dur)
    # action.Touch.down(x1, y1, dur)
    # action.Touch.move(x2, y2, dur)
    # action.Touch.up(x2, y2, dur)


def click(x, y, dur=200):
    action.click(x, y, dur)


def clickV2(x, y, dur=200):
    action.Touch.down(x, y, dur)
    action.Touch.up(x, y, dur)


def sleep(s):
    time.sleep(s)


def compareColors(colorStr, diff=0.9):
    res = CompareColors.compare(colorStr, diff)
    if res:
        return True
    else:
        return False


def imageFind(
    name, confidence1=0.9, x1=0, y1=0, x2=720, y2=1280, timeLock=10, rgb=False
):
    try:
        try:
            # with TimeoutLock(timeLock):
            path = R.res(f"/img/{name}.png")
            res = FindImages.find_template(
                path, [x1, y1, x2, y2], confidence=confidence1, rgb=rgb
            )
        except RuntimeError as e:
            print(f"imageFind获取锁超时")
            return False, 0, 0
        if res:
            # 检查 res 中是否有 center_x 和 center_y 键
            if "center_x" in res and "center_y" in res:
                x, y = res["center_x"], res["center_y"]
                print(f"imageFind识别成功: {name}")
                return True, x, y
            else:
                # 如果缺少键，返回默认值
                print(f"imageFind识别失败: {name}")
                return False, 0, 0
        else:
            print(f"imageFind未识别: {name}")
            return False, 0, 0
    except Exception as e:
        print(f"imageFind发生异常: {e}")
        return False, 0, 0


def imageFindAll(name, confidence1=0.9, x1=0, y1=0, x2=720, y2=1280, timeLock=10):
    try:
        try:
            # with TimeoutLock(timeLock):
            path = R.res(f"/img/{name}.png")
            res = FindImages.find_all_template(
                path, [x1, y1, x2, y2], confidence=confidence1
            )
        except RuntimeError as e:
            print(f"imageFind获取锁超时")
            return False, []
        if len(res) > 0:
            print(f"imageFind识别成功: {name}")
            return True, res
        else:
            # 如果缺少键，返回默认值
            print(f"imageFind识别失败: {name}")
            return False, []
    except Exception as e:
        print(f"imageFind发生异常: {e}")
        return False, []


def imageFindClick(
    name,
    sleep1=1,
    confidence1=0.7,
    x1=0,
    y1=0,
    x2=720,
    y2=1280,
    offsetX=0,
    offsetY=0,
    rgb=False,
):
    try:
        try:
            # with TimeoutLock():
            path = R.res(f"/img/{name}.png")
            res = FindImages.find_template(
                path, [x1, y1, x2, y2], confidence=confidence1, rgb=rgb
            )
        except RuntimeError as e:
            print(f"imageFindClick获取锁超时")
            return False
        if res:
            # 检查 res 中是否有 center_x 和 center_y 键
            if "center_x" in res and "center_y" in res:
                x, y = res["center_x"], res["center_y"]
                click(x + offsetX, y + offsetY)
                sleep(sleep1)
                print(f"imageFindClick识别成功: {name},{x + offsetX},{y + offsetY}")
                return True
            else:
                print(f"imageFindClick识别失败: {name}")
                return False
        else:
            print(f"imageFindClick识别错误: {name}")
            return False
    except Exception as e:
        print(f"imageFindClick发生异常: {e}")
        return False
