from zhipuai import ZhipuAI

def get_complete_response():
    try:
        # 初始化ZhipuAI客户端，需填入有效的API Key
        client = ZhipuAI(api_key="088ac276f3c9e876d8f9eb3921170a39.I3YVkRLzqUzeAp7N")
        # 调用聊天完成接口，设置为流式响应
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=[
                {"role": "system", "content": "你是一个乐于回答各种问题的小助手，你的任务是提供专业、准确、有洞察力的建议。"},
                {"role": "user", "content": "我对太阳系的行星非常感兴趣，尤其是土星。请提供关于土星的基本信息，包括它的大小、组成、环系统以及任何独特的天文现象。"},
            ],
            stream=True
        )

        # 用于存储拼接后的完整回复内容
        complete_content = ""
        for chunk in response:
            # 获取当前响应块中的ChoiceDelta对象
            delta = chunk.choices[0].delta
            # 检查ChoiceDelta对象中是否包含content字段
            if 'content' in delta.__dict__:
                # 若包含content字段，则将其拼接到完整内容中
                complete_content += delta.content

        return complete_content
    except Exception as e:
        print(f"发生错误：{e}")
        return None


result = get_complete_response()
if result:
    print("大模型思考中：")
    print(result)
else:
    print("未从API接收到有效内容或发生错误。")
