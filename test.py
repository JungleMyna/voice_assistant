# -*- coding:UTF-8 -*-
import sys, os, yaml
from aip import AipNlp

f = open('config.yaml')
config = yaml.load(f)
APP_ID = str(config['app_id'])
API_KEY = config['api_key']
SECRET_KEY = config['secret_key']
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


# 如果文本中包含打开or关闭，则进行以下处理
result = client.lexer("我在播放下一曲。")
# items = result['items']
# find_text = ''
# for item in items:
#     if find_text != '' or item['item'] == '打开' or item['item'] == '关闭':
#         find_text += item['item']

print(result)