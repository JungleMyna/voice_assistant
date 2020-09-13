# -*- coding:UTF-8 -*-
import shutil, os
from aip import AipNlp

# 语音识别
class Recognition():
    def __init__(self, config):
        APP_ID = str(config['app_id'])
        API_KEY = config['api_key']
        SECRET_KEY = config['secret_key']
        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def xunfei_recognize(self, fname):
        # 将文件移到识别目录
        root_path = os.path.abspath('.') + '/'
        print(root_path)
        shutil.copyfile(fname, root_path + "voice.wav")
        rs = os.popen(root_path + "xunfei/bin/iat_sample")
        text = rs.read()
        print(text)
        arr = text.split('=============================================================')
        if len(arr) == 0:
            return None
        result = arr[1].strip('\n')
        return result

    def recognize(self, fname):
        text = self.xunfei_recognize(fname)
        # 如果文本中包含打开or关闭，则进行以下处理
        if '打开' in text or '关闭' in text:
            result = self.client.lexer(text)
            items = result['items']
            find_text = ''
            for item in items:
                if find_text != '' or item['item'] == '打开' or item['item'] == '关闭':
                    find_text += item['item']
            if find_text != '':
                text = find_text
        return text