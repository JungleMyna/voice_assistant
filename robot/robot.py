# -*- coding:UTF-8 -*-
import requests,json
from recognition import Recognition
from nlu import Nlu
from speaker import Speaker

# 功能调度模块
class Robot():
    def __init__(self, config):
        self.config = config
        self.recognizer = Recognition(config) # 语音识别
        self.nlu = Nlu(config) # 语义识别
        self.speaker = Speaker(config) # 语音合成
    
    # HA接口
    def hass_api(self, api_url, data):
        try:
            cfg = self.config
            api_url = cfg['url'].strip('/') + '/api/' + api_url
            result = requests.post(api_url, json=data, headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + cfg['token']
            }, timeout=6)
            print(result)
        except Exception as ex:
            print('请求超时：')
            print(ex)

    # 识别语音并进行对应的处理
    def process(self, fname):
        speech = self.recognizer.recognize(fname) # 语音识别(语音转文字)
        if speech is not None:
            print('识别结果：{0}'.format(speech))
            if speech == '':
                self.speaker.speak("我没有听清楚，请再讲一遍")
                return
            self.hass_api('services/conversation/process', {'text': speech, 'source': 'baidu'})