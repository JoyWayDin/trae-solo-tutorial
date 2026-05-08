"""
飞书卡片消息示例
包含标题、文本、按钮等元素的卡片消息
"""

# ============ 配置区域 ============
WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
PROJECT_NAME = "我的项目"
# ==================================

import requests
import json
from datetime import datetime

def send_card_message(title, content, template="blue", buttons=None):
    """
    发送卡片消息到飞书

    参数:
        title: 卡片标题
        content: 卡片内容（支持 Markdown）
        template: 卡片颜色 (blue/red/green/yellow/purple/gray)
        buttons: 按钮列表 [{"text": "按钮文本", "url": "https://..."}]
    """
    elements = [
        {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": content
            }
        }
    ]

    # 添加按钮（如果有）
    if buttons:
        action_buttons = []
        for btn in buttons:
            action_buttons.append({
                "tag": "button",
                "text": {"tag": "plain_text", "text": btn["text"]},
                "type": btn.get("type", "default"),
                "url": btn.get("url", "")
            })

        elements.append({
            "tag": "action",
            "actions": action_buttons
        })

    # 添加时间戳
    elements.append({
        "tag": "note",
        "elements": [
            {"tag": "plain_text", "text": f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"}
        ]
    })

    card = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "text": title},
                "template": template
            },
            "elements": elements
        }
    }

    response = requests.post(WEBHOOK_URL, json=card)
    return response.json()

def example_build_notification():
    """示例：代码编译完成通知"""
    print("📤 发送编译完成通知...")

    result = send_card_message(
        title="🚀 代码编译完成",
        content=(
            f"**项目**：{PROJECT_NAME}\n"
            f"**状态**：✅ 编译成功\n"
            f"**耗时**：3分24秒\n\n"
            "**变更文件**：\n"
            "- src/index.js\n"
            "- src/components/Header.tsx\n"
            "- package.json"
        ),
        template="green",
        buttons=[
            {"text": "📝 查看详情", "type": "primary", "url": "https://github.com"},
            {"text": "📦 部署", "type": "default", "url": "https://deploy.example.com"}
        ]
    )

    if result.get('code') == 0:
        print("✅ 编译通知发送成功！")
    else:
        print(f"❌ 发送失败：{result}")

def example_error_alert():
    """示例：错误告警通知"""
    print("📤 发送错误告警...")

    result = send_card_message(
        title="🚨 错误告警",
        content=(
            "**服务器**：生产环境\n"
            "**错误级别**：ERROR\n\n"
            "**错误信息**：\n"
            "```\n"
            "TypeError: Cannot read property 'map' of undefined\n"
            "    at App.componentDidMount (App.js:45)\n"
            "```\n\n"
            "**建议**：立即检查数据源"
        ),
        template="red",
        buttons=[
            {"text": "🔍 查看日志", "type": "danger", "url": "https://logs.example.com"}
        ]
    )

    if result.get('code') == 0:
        print("✅ 告警发送成功！")
    else:
        print(f"❌ 发送失败：{result}")

def example_daily_reminder():
    """示例：每日提醒通知"""
    print("📤 发送每日提醒...")

    result = send_card_message(
        title="⏰ 每日站会提醒",
        content=(
            "**会议**：每日站会\n"
            "**时间**：9:30 - 9:45\n"
            "**地点**：腾讯会议\n\n"
            "📋 **今日 Agenda**：\n"
            "1. 昨日完成\n"
            "2. 今日计划\n"
            "3. 遇到的问题"
        ),
        template="blue",
        buttons=[
            {"text": "🎥 加入会议", "type": "primary", "url": "https://meeting.qq.com"}
        ]
    )

    if result.get('code') == 0:
        print("✅ 提醒发送成功！")
    else:
        print(f"❌ 发送失败：{result}")

def main():
    print("=" * 50)
    print("📨 飞书卡片消息示例")
    print("=" * 50)
    print()

    # 示例 1：编译完成通知
    print("【示例 1】代码编译完成通知")
    example_build_notification()
    print()

    # 示例 2：错误告警
    print("【示例 2】错误告警通知")
    example_error_alert()
    print()

    # 示例 3：每日提醒
    print("【示例 3】每日站会提醒")
    example_daily_reminder()
    print()

    print("=" * 50)
    print("✨ 所有示例发送完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()
