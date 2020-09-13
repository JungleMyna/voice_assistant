# -*- coding:UTF-8 -*-
import shutil, os
from aip import AipSpeech

# 语音识别
class Recognition():
    def __init__(self, config):
        APP_ID = str(config['app_id'])
        API_KEY = config['api_key']
        SECRET_KEY = config['secret_key']
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def xunfei_recognize(self, fname):
        # 将文件移到识别目录
        xunfei_path = os.path.abspath('../xunfei/bin') + '/'
        print(xunf)
        shutil.copyfile(fname, xunfei_path + "voice.wav")
        rs = os.popen(xunfei_path + "iat_sample")
        text = rs.read()
        print(text)
        arr = text.split('=============================================================')
        if len(arr) == 0:
            return None
        result = arr[1].strip('\n')
        return result

    def recognize(self, fname):
        return self.xunfei_recognize(fname)
        '''
        # 百度语音识别
        result = self.client.asr(self.get_file_content(fname), 'wav', 16000, {
            'dev_pid': 1537,
        })
        print(result)
        if 'result' in result:
            return result['result'][0]
        else:
            return None
        '''