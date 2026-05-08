# Trae Solo 使用教程：手机联动与自动化任务

> 🎯 目标读者：有基本电脑基础，想通过 Trae Solo 实现手机与电脑的智能联动
> 
> ⏱️ 预计学习时间：30 分钟（实战部分可根据需要选择性阅读）
> 
> 📱 核心功能：飞书推送 + 定时任务 + 事件触发 + 远程控制

---

## 📋 目录

1. [认识 Trae Solo](#1-认识-trae-solo)
2. [飞书机器人配置（核心重点）](#2-飞书机器人配置核心重点)
3. [Schedule 定时任务详解](#3-schedule-定时任务详解)
4. [定时提醒实战案例](#4-定时提醒实战案例)
5. [事件触发型自动化](#5-事件触发型自动化)
6. [最佳实践与常见问题](#6-最佳实践与常见问题)

---

## 1. 认识 Trae Solo

### 1.1 什么是 Trae Solo？

Trae Solo 是字节跳动推出的 AI 编程助手，专为开发者设计。它不仅能帮助你写代码、调试程序，还能实现**自动化任务**和**手机联动**。

### 1.2 Trae Solo 能做什么？

#### 💻 **编程辅助**
- 代码自动补全
- 代码解释与审查
- Bug 修复建议
- 多语言支持（Python、JavaScript、Java、Go 等）

#### 📱 **手机联动**（本教程重点）
- 定时任务提醒
- 事件触发通知
- 远程控制电脑
- 飞书/钉钉/企业微信消息推送

#### ⚡ **自动化任务**
- 定时生成报告
- 文件监控与同步
- CI/CD 流水线集成
- 自定义工作流

### 1.3 为什么选择飞书作为联动渠道？

| 对比项 | 飞书 | 钉钉 | 企业微信 |
|--------|------|------|----------|
| 消息到达率 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 配置难度 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| API 灵活性 | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 免费额度 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

**推荐理由**：飞书的 Webhook 机器人配置简单，消息格式丰富，免费额度充足，适合个人和小型团队使用。

### 1.4 安装 Trae Solo

#### Windows 系统
1. 访问 [Trae 官网](https://trae.ai)
2. 点击「下载 Windows 版本」
3. 运行安装包，一路「下一步」即可
4. 启动后使用手机号注册/登录

#### Mac 系统
1. 访问 [Trae 官网](https://trae.ai)
2. 点击「下载 Mac 版本」
3. 将应用拖入「应用程序」文件夹
4. 启动后使用手机号注册/登录

#### 手机端（iOS/Android）
1. 在 App Store（iOS）或应用商店（Android）搜索「Trae」
2. 下载并安装
3. 使用与电脑端相同的账号登录
4. 开启通知权限

### 1.5 界面初览

```
┌─────────────────────────────────────────────────┐
│  侧边栏      │         主工作区                  │
│             │                                   │
│ 📁 项目      │  ┌─────────────────────────────┐ │
│ 💬 对话      │  │      AI 对话窗口              │ │
│ 📅 定时任务  │  │                             │ │
│ ⚙️ 设置      │  │  输入框                       │ │
│             │  └─────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

**核心区域说明**：
- **侧边栏**：导航菜单，包含项目、对话、定时任务、设置
- **对话窗口**：与 AI 对话的界面
- **定时任务**：管理自动化任务的核心入口

---

## 2. 飞书机器人配置（核心重点）

> ⚠️ **重要**：完成这步配置后，你的电脑才能向手机飞书推送消息！

### 2.1 什么是飞书机器人？

飞书机器人是一个自动化的「消息转发员」。配置好后，Trae Solo 可以通过这个机器人向你的飞书账号推送消息，就像有人给你发消息一样。

### 2.2 创建飞书自定义机器人（步骤详解）

#### 第一步：进入飞书群聊设置

1. 打开飞书电脑端或手机端
2. 创建一个新群聊（或选择已有群聊）
3. 点击群聊右上角的「···」设置图标
4. 选择「群设置」

#### 第二步：添加自定义机器人

1. 在群设置中找到「群机器人」选项
2. 点击「添加机器人」
3. 选择「自定义机器人」
4. 给机器人起个名字，比如「Trae助手」
5. 点击「添加」

#### 第三步：获取 Webhook 地址

添加机器人后，你会看到一个 **Webhook 地址**，格式如下：

```
https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

⚠️ **重要**：
- 这个地址是**私密信息**，不要泄露给他人
- 复制并保存好，后面会用到
- 每个机器人的 Webhook 都是唯一的

### 2.3 在 Trae Solo 中配置飞书

#### 配置步骤

1. 打开 Trae Solo 客户端
2. 点击左下角「设置」图标
3. 找到「通知」或「集成」选项
4. 选择「飞书」
5. 粘贴刚才复制的 Webhook 地址
6. 点击「保存」或「测试连接」

#### 测试连接

配置完成后，点击「发送测试消息」按钮。
- ✅ 如果飞书收到消息，说明配置成功！
- ❌ 如果没收到，检查 Webhook 地址是否正确，网络是否正常。

### 2.4 消息格式详解

飞书机器人支持多种消息格式，我们可以发送：

#### 纯文本消息
```json
{
  "msg_type": "text",
  "content": {
    "text": "这是一条测试消息 🎉"
  }
}
```

#### 富文本消息（推荐）
```json
{
  "msg_type": "post",
  "content": {
    "post": {
      "zh_cn": {
        "title": "📢 每日提醒",
        "content": [
          [
            {
              "tag": "text",
              "text": "今天是周一，记得参加 10:00 的周会！"
            },
            {
              "tag": "at",
              "user_id": "all"
            }
          ]
        ]
      }
    }
  }
}
```

#### 卡片消息（最炫酷）
```json
{
  "msg_type": "interactive",
  "card": {
    "header": {
      "title": {
        "tag": "plain_text",
        "text": "🚀 代码编译完成"
      },
      "template": "green"
    },
    "elements": [
      {
        "tag": "div",
        "text": {
          "tag": "lark_md",
          "content": "**项目名称**：我的网站\n**编译状态**：✅ 成功\n**耗时**：3分24秒"
        }
      },
      {
        "tag": "action",
        "actions": [
          {
            "tag": "button",
            "text": {
              "tag": "plain_text",
              "text": "查看详情"
            },
            "type": "primary"
          }
        ]
      }
    ]
  }
}
```

### 2.5 实战：创建你的第一个飞书通知

**目标**：在 Trae Solo 中发送一条自定义消息到飞书

**步骤**：

1. 在 Trae Solo 中打开「定时任务」或「自定义脚本」功能
2. 编写以下代码（以 Python 为例）：

```python
import requests
import json

def send_feishu_message(webhook_url, message):
    """发送飞书消息"""
    headers = {'Content-Type': 'application/json'}
    data = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }
    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    return response.json()

# 配置你的 Webhook 地址
WEBHOOK_URL = "你的飞书Webhook地址"

# 发送测试消息
result = send_feishu_message(
    WEBHOOK_URL,
    "🎉 Trae Solo 配置成功！你的手机现在可以接收通知了！"
)
print(result)
```

3. 运行脚本
4. 查看手机飞书，是否收到消息 ✅

---

## 3. Schedule 定时任务详解

### 3.1 什么是 Schedule 功能？

Schedule 是 Trae Solo 的**定时任务管理器**，相当于一个「智能闹钟」。你可以设置：
- 每天早上 9 点提醒开会
- 每周五下午 5 点生成周报
- 每月 1 号推送数据报表
- 重要代码提交时自动通知

### 3.2 Schedule 核心概念

#### Cron 表达式（定时规则）

Schedule 使用标准 Cron 表达式来定义时间，格式为：

```
┌───────────── 分钟（0-59）
│ ┌─────────── 小时（0-23）
│ │ ┌───────── 日（1-31）
│ │ │ ┌─────── 月（1-12）
│ │ │ │ ┌───── 星期（0-6，0=周日）
│ │ │ │ │
* * * * *
```

#### 常用 Cron 示例

| Cron 表达式 | 含义 | 说明 |
|-------------|------|------|
| `0 9 * * *` | 每天 9:00 | 适合每日提醒 |
| `0 9 * * 1-5` | 工作日 9:00 | 周一到周五 |
| `30 8 * * *` | 每天 8:30 | 适合早会提醒 |
| `0 17 * * 5` | 每周五 17:00 | 适合周报生成 |
| `0 10 1 * *` | 每月 1 号 10:00 | 月度报告 |
| `*/15 * * * *` | 每 15 分钟 | 实时监控 |

### 3.3 在 Trae Solo 中创建定时任务

#### 基本步骤

1. 打开 Trae Solo
2. 点击侧边栏「定时任务」
3. 点击「创建任务」或「+」按钮
4. 填写任务信息：
   - **任务名称**：`每日早会提醒`
   - **执行时间**：选择 Cron 表达式或图形界面
   - **执行内容**：选择要执行的操作
   - **通知渠道**：选择「飞书」

#### 任务类型

1. **发送通知**：定时推送消息
2. **执行脚本**：运行 Python/Shell 脚本
3. **生成报告**：自动生成周报/月报
4. **触发构建**：启动项目编译
5. **自定义**：组合多种操作

### 3.4 任务管理

#### 查看任务列表
- 所有定时任务都会显示在「定时任务」页面
- 状态指示：🟢 运行中、⏸️ 已暂停、❌ 已失败

#### 任务操作
- **立即执行**：点击「运行」按钮可立即触发
- **暂停任务**：点击暂停按钮，任务将不再执行
- **编辑任务**：修改时间、内容等
- **删除任务**：不再需要的任务可以删除

#### 执行历史
每个任务都有执行记录，显示：
- 最后执行时间
- 执行状态（成功/失败）
- 执行结果或错误信息

---

## 4. 定时提醒实战案例

### 案例一：每日早会提醒 ⏰

#### 场景
每天早上 9:00，通过飞书提醒你参加 9:30 的早会。

#### 实现步骤

1. **创建飞书机器人**（参考第二章）
2. **在 Trae Solo 中创建定时任务**：
   - 任务名称：`每日早会提醒`
   - Cron 表达式：`0 9 * * 1-5`（工作日 9:00）
   - 操作：发送飞书通知

3. **编写消息内容**：

```json
{
  "msg_type": "interactive",
  "card": {
    "header": {
      "title": {
        "tag": "plain_text",
        "text": "⏰ 早会提醒"
      },
      "template": "blue"
    },
    "elements": [
      {
        "tag": "div",
        "text": {
          "tag": "lark_md",
          "content": "**会议**：每日站会\n**时间**：9:30 - 9:45\n**地点**：腾讯会议\n\n📋 **今日 agenda**：\n1. 昨日完成\n2. 今日计划\n3. 遇到的问题"
        }
      },
      {
        "tag": "action",
        "actions": [
          {
            "tag": "button",
            "text": {"tag": "plain_text", "text": "加入会议"},
            "type": "primary",
            "url": "https://meeting.qq.com"
          }
        ]
      }
    ]
  }
}
```

#### 效果预览
手机飞书收到卡片消息，点击按钮可直接加入会议 ✅

---

### 案例二：代码编译完成通知 🔥

#### 场景
当你提交代码到 Git 后，Trae Solo 自动编译，编译完成后推送结果到飞书。

#### 实现步骤

1. **配置 Git Hook**（可选，推荐使用 CI/CD）

2. **创建编译监控脚本**：

```python
import requests
import subprocess
import json
from datetime import datetime

# 配置
WEBHOOK_URL = "你的飞书Webhook地址"
PROJECT_PATH = "/path/to/your/project"

def send_notification(title, message, status="info"):
    """发送飞书通知"""
    colors = {
        "success": "green",
        "error": "red",
        "info": "blue",
        "warning": "yellow"
    }
    
    card = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "text": title},
                "template": colors.get(status, "blue")
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {"tag": "lark_md", "content": message}
                },
                {
                    "tag": "note",
                    "elements": [
                        {"tag": "plain_text", "text": f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"}
                    ]
                }
            ]
        }
    }
    
    requests.post(WEBHOOK_URL, json=card)

def build_project():
    """执行编译"""
    try:
        result = subprocess.run(
            ["npm", "run", "build"],
            cwd=PROJECT_PATH,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            send_notification(
                "✅ 编译成功",
                f"**项目**：我的网站\n**状态**：编译完成\n**耗时**：3分24秒",
                "success"
            )
        else:
            send_notification(
                "❌ 编译失败",
                f"**项目**：我的网站\n**状态**：编译出错\n\n```\n{result.stderr[:500]}\n```",
                "error"
            )
    except Exception as e:
        send_notification(
            "⚠️ 编译异常",
            f"**错误信息**：{str(e)}",
            "warning"
        )

if __name__ == "__main__":
    build_project()
```

3. **配置为 Git Hook**（可选）：

在 `.git/hooks` 目录创建 `post-commit` 文件：

```bash
#!/bin/bash
# 提交代码后自动触发编译通知
python /path/to/build_notify.py
```

---

### 案例三：一键生成周报 📊

#### 场景
每周五下午 5:00，自动收集 Git 提交记录，生成周报并发送到飞书。

#### 实现步骤

1. **创建周报生成脚本**：

```python
import requests
import json
import subprocess
from datetime import datetime, timedelta

# 配置
WEBHOOK_URL = "你的飞书Webhook地址"
GIT_PROJECT_PATH = "/path/to/your/project"

def get_git_commits():
    """获取本周的 Git 提交记录"""
    # 获取本周一和今天的日期
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    
    # 执行 git log 命令获取本周提交
    result = subprocess.run(
        ["git", "log", 
         f"--since={week_start.strftime('%Y-%m-%d')}",
         "--pretty=format:%h %s - %an %ad",
         "--date=short"],
        cwd=GIT_PROJECT_PATH,
        capture_output=True,
        text=True
    )
    
    commits = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return commits

def generate_weekly_report():
    """生成周报"""
    commits = get_git_commits()
    
    # 统计
    total_commits = len(commits)
    
    # 生成 Markdown 格式的周报
    report_lines = [
        f"## 📊 本周工作总结\n",
        f"**统计**：共 {total_commits} 次提交\n",
        "### 提交记录\n"
    ]
    
    for commit in commits:
        if commit:
            report_lines.append(f"- {commit}")
    
    report_lines.append("\n---\n*报告自动生成于 " + datetime.now().strftime('%Y-%m-%d %H:%M') + "*")
    
    return '\n'.join(report_lines)

def send_weekly_report():
    """发送周报到飞书"""
    report = generate_weekly_report()
    
    card = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "text": "📊 周报 - " + datetime.now().strftime('%Y-%m-%d')},
                "template": "purple"
            },
            "elements": [
                {
                    "tag": "markdown",
                    "content": report
                },
                {
                    "tag": "action",
                    "actions": [
                        {
                            "tag": "button",
                            "text": {"tag": "plain_text", "text": "查看详情"},
                            "type": "primary"
                        }
                    ]
                }
            ]
        }
    }
    
    requests.post(WEBHOOK_URL, json=card)

if __name__ == "__main__":
    send_weekly_report()
```

2. **在 Trae Solo 中配置定时任务**：
   - 任务名称：`周报生成`
   - Cron 表达式：`0 17 * * 5`（每周五 17:00）
   - 操作：执行 `weekly_report.py` 脚本

3. **效果**：
   - 每周五 17:00，飞书自动收到周报
   - 包含本周提交记录统计
   - 点击可查看详细记录 ✅

---

## 5. 事件触发型自动化

### 5.1 什么是事件触发？

事件触发是指**当某个特定事件发生时**，自动执行预设的操作。比如：
- 代码推送到 GitHub 后，自动通知
- 文件被修改后，自动备份
- 服务器出现错误日志，自动告警
- 项目编译失败，自动通知负责人

### 5.2 常用事件类型

| 事件类型 | 触发条件 | 典型场景 |
|---------|---------|---------|
| Git Hooks | 代码提交/推送/合并 | 自动编译、代码检查 |
| 文件监控 | 文件创建/修改/删除 | 自动备份、日志分析 |
| 错误监控 | 日志关键词匹配 | 实时告警、快速响应 |
| API 调用 | 收到特定请求 | 消息转发、命令执行 |
| 定时检查 | 定时轮询状态 | 健康检查、定时报表 |

### 5.3 实战案例：Git 提交自动通知

#### 场景
当你向 Git 仓库推送代码时，自动在飞书群中通知团队成员。

#### 实现方案

**方案 A：使用 Git Hooks（推荐）**

1. **创建 Webhook 脚本**（保存为 `git_notify.py`）：

```python
#!/usr/bin/env python3
import requests
import json
import sys
import os
from datetime import datetime

# 配置
WEBHOOK_URL = "你的飞书Webhook地址"
PROJECT_NAME = "我的项目"
GITLAB_WEB_URL = "https://your-gitlab.com/your/project"

def send_git_notification(commit_info):
    """发送 Git 提交通知"""
    
    commit_id = commit_info.get('id', '')[:8]
    message = commit_info.get('message', '')
    author = commit_info.get('author_name', '')
    branch = commit_info.get('ref', '').replace('refs/heads/', '')
    repo_url = commit_info.get('repository', {}).get('homepage', GITLAB_WEB_URL)
    
    card = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "text": "🚀 代码已推送"},
                "template": "green"
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"**项目**：{PROJECT_NAME}\n**分支**：{branch}\n**作者**：{author}"
                    }
                },
                {
                    "tag": "hr"
                },
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"**提交信息**：{message}"
                    }
                },
                {
                    "tag": "action",
                    "actions": [
                        {
                            "tag": "button",
                            "text": {"tag": "plain_text", "text": "查看提交"},
                            "type": "primary",
                            "url": f"{repo_url}/commit/{commit_id}"
                        },
                        {
                            "tag": "button",
                            "text": {"tag": "plain_text", "text": "查看变更"},
                            "type": "default",
                            "url": f"{repo_url}/compare/{commit_id}"
                        }
                    ]
                }
            ]
        }
    }
    
    requests.post(WEBHOOK_URL, json=card)

def main():
    """主函数 - 从 Git 接收数据"""
    try:
        # 从 stdin 读取 Git 传递的数据
        commit_info = json.load(sys.stdin)
        send_git_notification(commit_info)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```

2. **配置 Git Hook**：

```bash
# 在项目 .git/hooks 目录创建 post-push 文件
cat > .git/hooks/post-push << 'EOF'
#!/bin/bash

while read local_ref local_sha remote_ref remote_sha; do
    if [ "$remote_sha" != "0000000000000000000000000000000000000000" ]; then
        # 获取提交信息
        git log --pretty=format:'{"id":"%H","message":"%s","author_name":"%an","author_email":"%ae","ref":"%D"}' \
            "$remote_sha" ^"$local_sha" | python3 git_notify.py
    fi
done
EOF

# 设置执行权限
chmod +x .git/hooks/post-push
```

3. **配置 GitLab/GitHub Webhook（可选）**：

如果你使用 GitLab/GitHub，可以在仓库设置中添加 Webhook：
- URL：`https://your-server.com/git-webhook`
- Events：Push events
- 然后在你的服务器上接收并处理

**方案 B：使用 GitLab/GitHub 内置 Webhook**

1. 在 GitLab 仓库 → Settings → Webhooks
2. 添加 Webhook URL
3. 选择 Push events
4. 服务器端接收并转发到飞书

---

### 5.4 实战案例：文件监控与告警

#### 场景
监控日志文件，当出现 ERROR 关键词时，立即在飞书告警。

#### 实现代码

```python
import time
import requests
import json
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 配置
WEBHOOK_URL = "你的飞书Webhook地址"
LOG_FILE = "/var/log/myapp/error.log"
ERROR_KEYWORDS = ["ERROR", "FATAL", "CRITICAL"]

class LogFileHandler(FileSystemEventHandler):
    """日志文件监控处理器"""
    
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.file_position = 0
        
        # 初始化文件位置
        if self.file_path.exists():
            self.file_position = self.file_path.stat().st_size
    
    def on_modified(self, event):
        """文件被修改时触发"""
        if event.src_path != str(self.file_path):
            return
        
        self.check_new_errors()
    
    def check_new_errors(self):
        """检查新增的错误日志"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                # 跳转到上次读取位置
                f.seek(self.file_position)
                
                # 读取新增内容
                new_content = f.read()
                self.file_position = f.tell()
                
                # 检查错误关键词
                for keyword in ERROR_KEYWORDS:
                    if keyword in new_content:
                        self.send_alert(new_content, keyword)
                        break
                        
        except Exception as e:
            print(f"读取日志失败: {e}")
    
    def send_alert(self, content, keyword):
        """发送告警到飞书"""
        # 提取错误信息（最多显示最后 500 字符）
        error_lines = [line for line in content.split('\n') if keyword in line]
        error_summary = '\n'.join(error_lines[-5:])
        
        if len(error_summary) > 500:
            error_summary = error_summary[:500] + "..."
        
        card = {
            "msg_type": "interactive",
            "card": {
                "header": {
                    "title": {"tag": "plain_text", "text": "🚨 错误告警"},
                    "template": "red"
                },
                "elements": [
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": f"**文件**：{self.file_path.name}\n**关键词**：{keyword}\n\n**错误信息**：\n```\n{error_summary}\n```"
                        }
                    },
                    {
                        "tag": "action",
                        "actions": [
                            {
                                "tag": "button",
                                "text": {"tag": "plain_text", "text": "立即查看"},
                                "type": "danger"
                            }
                        ]
                    }
                ]
            }
        }
        
        requests.post(WEBHOOK_URL, json=card)

def start_monitoring():
    """启动文件监控"""
    log_dir = str(Path(LOG_FILE).parent)
    handler = LogFileHandler(LOG_FILE)
    
    observer = Observer()
    observer.schedule(handler, log_dir, recursive=False)
    observer.start()
    
    print(f"✅ 开始监控: {LOG_FILE}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

if __name__ == "__main__":
    start_monitoring()
```

#### 运行方式

```bash
# 安装依赖
pip install watchdog requests

# 后台运行
nohup python3 log_monitor.py > log_monitor.log 2>&1 &

# 查看日志
tail -f log_monitor.log
```

#### 效果
当日志文件中出现 ERROR/FATAL/CRITICAL 关键词时，飞书立即收到告警通知 ✅

---

### 5.5 实战案例：CI/CD 流水线状态推送

#### 场景
GitLab CI/GitHub Actions 流水线执行完成后，自动推送结果到飞书。

#### GitLab CI 配置

在 `.gitlab-ci.yml` 中添加：

```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - echo "Building..."
    - npm run build
  after_script:
    - python3 notify.py "build" "success"

test:
  stage: test
  script:
    - echo "Testing..."
    - npm test
  after_script:
    - python3 notify.py "test" "success" "失败" "error"

deploy:
  stage: deploy
  script:
    - echo "Deploying..."
    - ./deploy.sh
  after_script:
    - python3 notify.py "deploy" "success"
  only:
    - main

notify:
  stage: .post
  script:
    - echo "Notification sent"
  when: always  # 即使前面的 job 失败也会执行
```

#### 通知脚本 `notify.py`

```python
#!/usr/bin/env python3
import requests
import json
import sys
import os
from datetime import datetime

# 配置
WEBHOOK_URL = os.environ.get('FEISHU_WEBHOOK_URL')
CI_PROJECT = os.environ.get('CI_PROJECT_NAME', '我的项目')
CI_PIPELINE_URL = os.environ.get('CI_PIPELINE_URL', '')
CI_JOB_NAME = sys.argv[1] if len(sys.argv) > 1 else 'unknown'
CI_JOB_STATUS = sys.argv[2] if len(sys.argv) > 2 else 'success'
CI_COMMIT_MSG = os.environ.get('CI_COMMIT_MESSAGE', '')
CI_COMMIT_AUTHOR = os.environ.get('CI_COMMIT_AUTHOR', '')

def get_status_emoji(status):
    """根据状态返回 emoji"""
    status_map = {
        'success': ('✅', 'green', '成功'),
        'failed': ('❌', 'red', '失败'),
        'canceled': ('⚪', 'grey', '已取消'),
        'running': ('🔄', 'blue', '运行中'),
        'pending': ('⏳', 'yellow', '等待中')
    }
    return status_map.get(status, ('📌', 'blue', status))

def send_notification():
    """发送 CI/CD 状态通知"""
    if not WEBHOOK_URL:
        print("❌ 未配置飞书 Webhook URL")
        return
    
    emoji, color, status_text = get_status_emoji(CI_JOB_STATUS)
    
    card = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "text": f"{emoji} CI/CD 流水线 {status_text}"},
                "template": color
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"**项目**：{CI_PROJECT}\n**阶段**：{CI_JOB_NAME}\n**状态**：{status_text}\n**触发者**：{CI_COMMIT_AUTHOR}"
                    }
                },
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"**提交**：{CI_COMMIT_MSG}"
                    }
                },
                {
                    "tag": "action",
                    "actions": [
                        {
                            "tag": "button",
                            "text": {"tag": "plain_text", "text": "查看流水线"},
                            "type": "primary",
                            "url": CI_PIPELINE_URL
                        }
                    ]
                }
            ]
        }
    }
    
    response = requests.post(WEBHOOK_URL, json=card)
    print(f"✅ 通知已发送: {response.text}")

if __name__ == "__main__":
    send_notification()
```

#### 效果
流水线执行完成（成功/失败），飞书立即收到详细通知 ✅

---

## 6. 最佳实践与常见问题

### 6.1 最佳实践

#### ✅ **消息简洁明了**
- 标题控制在 20 字以内
- 关键信息放在最前面
- 使用 emoji 增强可读性

#### ✅ **合理使用卡片消息**
- 普通提醒 → 文本消息
- 重要通知 → 卡片消息
- 紧急告警 → 卡片 + 按钮

#### ✅ **定时任务时间选择**
- 工作时间提醒 → 9:00-18:00
- 日报/周报 → 下班前 30 分钟
- 避免深夜/凌晨推送（除非紧急）

#### ✅ **错误处理**
- 所有脚本都要有异常捕获
- 失败时发送通知告警
- 保留详细日志便于排查

#### ✅ **安全性**
- Webhook URL 不要提交到代码仓库
- 使用环境变量存储敏感信息
- 定期更换 Webhook 地址

### 6.2 常见问题

#### Q1: 飞书收不到消息？
**排查步骤**：
1. 检查 Webhook URL 是否正确
2. 检查网络连接是否正常
3. 在飞书机器人设置中测试发送
4. 查看 Trae Solo 日志是否有错误

#### Q2: 定时任务没有执行？
**排查步骤**：
1. 检查任务状态是否为「运行中」
2. 检查 Cron 表达式是否正确
3. 查看执行历史是否有错误
4. 手动点击「立即执行」测试

#### Q3: 消息格式显示异常？
**可能原因**：
- JSON 格式错误
- 飞书不支持的 HTML 标签
- 消息内容超过长度限制

**解决方法**：
- 使用在线 JSON 验证工具
- 简化消息格式
- 分割长消息分多次发送

#### Q4: 如何实现更复杂的自动化？
**进阶方案**：
- 使用 `n8n`、`Make (formerly Integromat)` 等工作流工具
- 搭建自己的 Webhook 服务
- 结合钉钉/企业微信的更多 API
- 使用 serverless 函数（如阿里云函数计算）

#### Q5: 手机端如何使用？
**操作步骤**：
1. 下载 Trae App（iOS/Android）
2. 登录与电脑相同的账号
3. 开启通知权限
4. 在「通知设置」中配置推送偏好

### 6.3 进阶学习路径

1. **入门**（已完成 ✅）
   - 飞书机器人配置
   - 基础定时任务
   - 简单消息推送

2. **进阶**
   - 复杂工作流编排
   - 多渠道消息推送
   - 错误监控与告警

3. **高级**
   - 自定义 Webhook 服务
   - 企业级自动化平台
   - 团队协作自动化

### 6.4 资源推荐

- 📚 飞书开放平台文档：https://open.feishu.cn/document/
- 📚 Trae Solo 官方文档：https://docs.trae.ai
- 📚 Cron 表达式教程：https://crontab.guru
- 💬 Trae 用户交流群：[飞书群链接]

---

## 🎉 总结

通过本教程，你已经学会了：

1. ✅ **配置飞书机器人** - 实现手机接收通知
2. ✅ **创建定时任务** - 自动执行重复性工作
3. ✅ **实现事件触发** - 智能响应代码变更和错误
4. ✅ **多个实战案例** - 早会提醒、代码编译、周报生成、文件监控等

**下一步建议**：
- 选择 1-2 个最实用的案例立即实践
- 根据自己的项目定制脚本
- 逐步扩展到更多自动化场景

---

> 📝 **文档版本**：v1.0
> 
> ⏰ **更新日期**：2026-05-08
> 
> 👨‍💻 **作者**：AI Assistant
> 
> 💬 **反馈建议**：如有疑问或建议，欢迎在评论区留言！

---

**祝你玩转 Trae Solo，效率提升 10 倍 🚀**
