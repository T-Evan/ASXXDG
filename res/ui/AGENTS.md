# UI 子域知识库

## 概览
- `res/ui` 负责 WebWindow 承载的配置界面，以及把页面设置传入运行时的 Python 桥接层。

## 结构
```text
res/ui/
├── ui.py        # Python WebWindow 宿主与桥接回调
├── ui.html      # 配置页面与页面侧交互逻辑
├── js/          # 本地 JS 资源
└── layui/       # vendored 前端库资源
```

## 去哪里看
| 任务 | 位置 | 说明 |
|---|---|---|
| 修改布局、控件、文案 | `ui.html` | 表单结构、开关文案、localStorage 持久化、提交时机 |
| 修改 Python 桥接逻辑 | `ui.py` | `WebWindow(...)`、回调绑定、配置传递、关闭/等待流程 |
| 新增一个 UI 开关 | `ui.html`、`ui.py` | 页面侧增加控件和提交字段，Python 侧把它映射进运行时配置 |
| 排查页面到 Python 的消息链路 | `ui.html`、`ui.py` | 页面通过 `airscript.call(...)` 发消息，Python 在桥接回调中接收 |
| 检查前端库或本地脚本资源 | `layui/`、`js/` | 只在明确升级 vendor 或排查 vendor 行为时修改 |

## 约定
- `ui.py` 使用 `WebWindow(R.ui('ui.html'))` 承载页面；保持 HTML 路径与桥接关系清晰稳定。
- 页面通过 `airscript.call(...)` 与 Python 通信，至少包含加载、提交、关闭等事件通道。
- `ui.html` 使用 localStorage 持久化设置；除非明确做迁移，否则应保持既有 key/value 行为兼容。
- `ui.py` 是把页面提交结果转成运行时 `功能开关` 配置的边界层。

## 反模式
- 不要把核心自动化运行逻辑塞进 `res/ui`；这里应只负责 UI 与桥接。
- 不要随意改 vendored 的 `layui` 文件；优先在 `ui.html` / `ui.py` 层解决问题。
- 不要假设这里存在前端构建步骤；当前 UI 直接以本地静态资源形式提供。
- 修改 `airscript.call(...)` 的消息契约时，不要只改一侧；页面和 Python 桥接必须同时更新。

## 备注
- 这里最重要的跨文件契约是：`ui.html` 收集状态 → `airscript.call(...)` 发送载荷 → `ui.py` 接收并处理 → 运行时消费 `功能开关`。
- 根级运行时、OCR、图片资源约定等内容见父级 `AGENTS.md`。
