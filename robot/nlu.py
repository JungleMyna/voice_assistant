# -*- coding:UTF-8 -*-
import requests
import uuid
from aip import AipNlp

# 自然语言处理(语义识别)
class Nlu():
    def __init__(self, config):
        APP_ID = str(config['app_id'])
        API_KEY = config['api_key']
        SECRET_KEY = config['secret_key']
        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    def query(self, tex):
        result = self.client.lexer(tex)
        print('语义识别：', result)
        import json
        with open("temp.json",'w') as f:#,encoding='utf-8'
            json.dump(result, f)#, ensure_ascii=False
        return self.parser(result)
    
    def parser(self, result):
        response_list = result['result']['items']
        response = response_list[0]
        if response['origin'] == '51011':
            return ('weather', response)
        elif response['origin'] == '51010':
            return ('chat', response)
        elif response['origin'] == '51027':
            return ('ticket', response)
        elif response['origin'] == '51028':
            return ('noun_interpretaion', response)
        elif response['origin'] == '50968':
            return ('music', response)
            


