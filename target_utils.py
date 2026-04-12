import time

from .baseUtils import imageFind, tapSleep, Toast
from .target_templates import 坐标去重网格大小, 禁点区域列表, 已处理坐标有效时长


def 生成坐标去重键(流程类型, x, y):
    return f"{流程类型}:{x // 坐标去重网格大小}:{y // 坐标去重网格大小}"


def 坐标在禁点区域内(x, y):
    for 禁点区域 in 禁点区域列表:
        x1, y1, x2, y2 = 禁点区域
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
    return False


def 查找未处理目标(流程类型, 模板列表, 已处理坐标):
    当前时间 = time.time()
    过期坐标 = []
    for 去重键, 记录时间 in 已处理坐标.items():
        if 当前时间 - 记录时间 >= 已处理坐标有效时长:
            过期坐标.append(去重键)
    for 去重键 in 过期坐标:
        del 已处理坐标[去重键]

    for 模板 in 模板列表:
        is_find, x, y = imageFind(
            模板["name"],
            confidence1=模板.get("confidence1", 0.9),
            x1=模板.get("x1", 0),
            y1=模板.get("y1", 0),
            x2=模板.get("x2", 720),
            y2=模板.get("y2", 1280),
            rgb=模板.get("rgb", False),
        )
        if not is_find:
            continue
        if 坐标在禁点区域内(x, y):
            Toast(f"跳过禁点区域{流程类型}")
            continue
        去重键 = 生成坐标去重键(流程类型, x, y)
        if 去重键 in 已处理坐标:
            Toast(f"跳过已处理{流程类型}")
            continue
        return {
            "name": 模板["name"],
            "x": x,
            "y": y,
            "offsetX": 模板.get("offsetX", 0),
            "offsetY": 模板.get("offsetY", 0),
            "去重键": 去重键,
        }
    return None


def 点击目标(目标信息, sleep1=1):
    if 坐标在禁点区域内(目标信息["x"], 目标信息["y"]):
        Toast("跳过禁点区域点击")
        return False
    tapSleep(
        目标信息["x"] + 目标信息["offsetX"], 目标信息["y"] + 目标信息["offsetY"], sleep1
    )
    return True


def 记录已处理坐标(流程类型, 目标信息, 已处理坐标):
    已处理坐标[目标信息["去重键"]] = time.time()
    Toast(f"记录已处理{流程类型}")
