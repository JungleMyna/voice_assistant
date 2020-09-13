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
    
    # 将文字发给HomeAssistant
    def conversation_process(self, speech):
        try:
            cfg = self.config
            api_url = cfg['url'].strip('/') + '/api/services/conversation/process'
            result = requests.post(api_url, json={'text': speech, 'source': 'baidu'}, headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + cfg['token']
            }, timeout=5)
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
            self.conversation_process(speech) # 发送到HA
            '''
            skill, response = self.nlu.query(speech) # 语义识别(情感倾向)
            if skill == 'weather':
                print("命中技能天气")
                self.weather.process(response)
            elif skill == 'chat':
                print("命中技能闲聊")
                self.chat.process(response)
            elif skill == 'noun_interpretaion':
                print("命中技能名词解释")
                self.noun.process(response)
            elif skill == 'ticket':
                print("命中技能订购车票")
                self.ticket.process(response)
            elif skill == 'music':
                print("命中技能播放音乐")
                self.music.process(response)
            '''