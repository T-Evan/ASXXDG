# 项目知识库

## 概览
- `worldTalk` 是一个面向游戏“新星帝国”的 AScript Android 自动化项目。
- 运行时核心由 Python 入口（`__init__.py`）、OCR/交互辅助层（`baseUtils.py`、`tomato_ocr.py`、`特征库.py`）以及 `res/ui` 下的本地配置界面组成。

## 结构
```text
worldTalk/
├── __init__.py        # 主运行入口与整体编排循环
├── baseUtils.py       # OCR、点击、提示、解析与通用辅助方法
├── tomato_ocr.py      # TomatoOcr 插件初始化、授权与配置
├── 特征库.py           # 基于打包资源的图像/颜色/动作辅助层
├── build.as           # AScript 打包/运行时依赖清单
├── res/
│   ├── img/           # 通过 R.res(...) 引用的打包图片资源
│   └── ui/            # WebWindow UI 桥接层与前端资源
└── .cursor/mcp.json   # 本地 ascript MCP 配置
```

## 去哪里看
| 任务 | 位置 | 说明 |
|---|---|---|
| 追踪启动与主流程 | `__init__.py` | 真正入口文件；校验分辨率并运行自动化主循环 |
| 调整 OCR 行为 | `tomato_ocr.py`、`baseUtils.py` | 插件初始化在 `tomato_ocr.py`；大多数 OCR 包装方法在 `baseUtils.py` |
| 修改点击/找图/颜色逻辑 | `特征库.py`、`baseUtils.py` | `特征库.py` 封装底层资源与识别；`baseUtils.py` 组合出更高层交互能力 |
| 调整 UI 驱动的开关配置 | `res/ui/ui.py`、`res/ui/ui.html` | UI 提交配置后会进入全局 `功能开关` |
| 增删图片资源 | `res/img/` | 代码默认通过 `R.res('/img/{name}.png')` 读取打包资源 |
| 查看依赖与运行假设 | `build.as`、`tomato_ocr.py`、`__init__.py` | 仓库中没有 `requirements.txt`、`pyproject.toml`、CI 或 Makefile |

## 约定
- 把 `__init__.py` 视为真实运行入口，不要假设项目存在常规的 `main.py` 或命令行封装。
- 本仓库依赖 AScript Android 运行时（大量 `ascript.android.*` 导入）；不要按桌面 Python 项目思路理解它。
- OCR 不是通用抽象：TomatoOcr 的插件加载、授权和参数配置集中在 `tomato_ocr.py`。
- 屏幕识别与图片操作依赖 AScript API 与打包资源，不依赖普通本地文件路径。
- UI 状态由 `res/ui` 推送进运行时并形成 `功能开关`；新增开关时要保持这条契约稳定。

## 反模式（本项目）
- 不要补充依赖 `pytest`、`npm`、`Make`、GitHub Actions` 之类的说明；这些都不是当前项目工作流的一部分。
- 不要用临时本地路径读取图片资源；现有约定是 `R.res('/img/{name}.png')`。
- 不要把 `res/ui/layui` 当作一方业务代码随意修改；它是 vendored 前端库资源。
- 不要把 OCR 的授权与初始化逻辑拆散到多个辅助文件里；应继续集中在 `tomato_ocr.py`。
- 调整界面或屏幕逻辑时，不要忽略 `__init__.py` 中强依赖的 1280x720 横屏假设。

## 项目特征风格
- 大量运行时逻辑、按钮文案和游戏行为描述使用中文；已有术语应优先保持一致。
- `baseUtils.py` 是集成层，不只是窄工具集；很多高层交互辅助都集中在这里。
- `特征库.py` 是图像/动作特征层，应与 `res/img` 里的资源命名保持一致。

## 常用查看命令
```bash
# 查看项目依赖清单
read build.as

# 查看本地 AScript MCP 配置
read .cursor/mcp.json
```

## 备注
- `build.as` 是这个仓库最接近依赖清单的文件。
- 初始化前，仓库中不存在现成的 `AGENTS.md`/`CLAUDE.md`。
- `res/ui/AGENTS.md` 是 UI 子域的补充规则文件。
