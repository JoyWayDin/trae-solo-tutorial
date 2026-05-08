# ============ 配置区域 ============
# 请替换为你的飞书 Webhook 地址
WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

# 项目名称（可自定义）
PROJECT_NAME = "我的项目"

# 飞书机器人名称
BOT_NAME = "Trae助手"
# ==================================

import requests
import json
from datetime import datetime

def send_text_message(message):
    """发送文本消息到飞书"""
    data = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }
    response = requests.post(WEBHOOK_URL, json=data)
    return response.json()

def send_rich_message(title, content):
    """发送富文本消息到飞书"""
    data = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": title,
                    "content": [[
                        {
                            "tag": "text",
                            "text": content
                        }
                    ]]
                }
            }
        }
    }
    response = requests.post(WEBHOOK_URL, json=data)
    return response.json()

def main():
    print("=" * 50)
    print("🚀 Trae Solo 飞书通知测试")
    print("=" * 50)
    print()
    
    print(f"📦 项目名称：{PROJECT_NAME}")
    print(f"🤖 机器人名称：{BOT_NAME}")
    print(f"⏰ 测试时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 发送测试消息
    print("📤 发送文本消息...")
    result1 = send_text_message(f"🎉 Trae Solo 配置成功！\n\n这是一个测试消息\n时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if result1.get('code') == 0:
        print("✅ 文本消息发送成功！")
    else:
        print(f"❌ 文本消息发送失败：{result1}")
    
    print()
    
    # 发送富文本消息
    print("📤 发送富文本消息...")
    result2 = send_rich_message(
        "📢 配置测试通知",
        f"**项目**：{PROJECT_NAME}\n**状态**：✅ 配置成功\n\n如果你看到这条消息，说明飞书机器人已经配置成功！\n\n接下来你可以：\n1. 创建定时任务\n2. 设置事件触发\n3. 开始你的自动化之旅 🚀"
    )
    
    if result2.get('code') == 0:
        print("✅ 富文本消息发送成功！")
    else:
        print(f"❌ 富文本消息发送失败：{result2}")
    
    print()
    print("=" * 50)
    print("✨ 测试完成！")
    print("=" * 50)
    print()
    print("📱 请检查你的飞书是否收到消息。")
    print("💡 如果没有收到消息，请检查：")
    print("   1. Webhook 地址是否正确")
    print("   2. 网络连接是否正常")
    print("   3. 飞书群机器人是否正常")

if __name__ == "__main__":
    main()
