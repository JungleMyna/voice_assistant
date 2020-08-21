# -*- coding:UTF-8 -*-
from aip import AipSpeech

# 语音识别
class Recognition():
    def __init__(self, config):
        APP_ID = config['app_id']
        API_KEY = config['api_key']
        SECRET_KEY = config['secret_key']
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def recognize(self, fname):
        result = self.client.asr(self.get_file_content(fname), 'wav', 16000, {
            'dev_pid': 1536,
        })
        print(result)
        if 'result' in result:
            return result['result'][0]
        else:
            return None