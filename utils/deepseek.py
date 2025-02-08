# -*- coding: utf-8 -*-
"""
@Auth ：
@File ：deepseek.py
@IDE ：
@Motto :学习新思想，争做新青年
"""
import json

import requests
from PySide6.QtCore import QThread, Signal

# 配置API密钥和基础URL
api_key = 'sk-b9a4014ea83e490286347239e7edb310'
base_url = 'https://api.deepseek.com'

# 构建请求头
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

class ApiThread(QThread):
    """用于处理API请求的线程"""
    response_signal = Signal(str)
    complete_signal = Signal()

    def __init__(self, user_input):
        super().__init__()
        self.user_input = user_input

    def run(self):
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": self.user_input},
                {"role": "user", "content": ""}
            ],
            "stream": True  # 启用流式传输
        }

        try:
            # 发送POST请求
            response = requests.post(f'{base_url}/chat/completions', headers=headers, json=data, stream=True)
            if response.status_code == 200:
                # 逐行处理流式响应
                for line in response.iter_lines():
                    if line:
                        decoded_line = line.decode('utf-8')
                        if decoded_line.startswith("data:"):
                            try:
                                json_data = json.loads(decoded_line[5:])
                                content = json_data['choices'][0]['delta'].get('content', '')
                                if content:
                                    self.response_signal.emit(content)
                                    print(content, end='', flush=True)
                            except json.JSONDecodeError:
                                pass
            else:
                print(f'请求失败，状态码: {response.status_code}')
                print(f'响应内容: {response.text}')
                self.response_signal.emit("API请求失败")
        except Exception as e:
            self.response_signal.emit(f"请求异常: {str(e)}")
        finally:
            self.complete_signal.emit()  