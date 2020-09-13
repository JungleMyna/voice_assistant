# -*- coding:UTF-8 -*-
from snowboy import snowboydecoder
import sys, os, yaml
import signal
from robot.player import Player
from robot.robot import Robot
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SmartSpeaker():
    # 初始化
    def __init__(self):
        self.interrupted = False
        # 读取配置
        config_file = 'config.yaml'
        if os.path.exists(config_file) == False:
            print('【警告】配置文件不存在')
            return
        f = open('config.yaml')
        config = yaml.load(f)
        model_name = config.get('name', 'snowboy')
        if ['snowboy','alexa'].count(model_name) > 0:
            model_name = model_name + '.umdl'
        else:
            model_name = model_name + '.pmdl'

        self.model = "唤醒词/" + model_name # 使用的语音模型
        print('【唤醒词文件】' + self.model)
        if os.path.exists(self.model) == False:
            print('【警告】唤醒词文件不存在')
            return
        signal.signal(signal.SIGINT, self.signal_handler) # 捕获ctrl+c
        self.detector = snowboydecoder.HotwordDetector(self.model, sensitivity=0.5) # 设置语音模型与敏感度
        print('Listening... Press Ctrl+Z to exit')
        self.robot = Robot(config) # 创建应用模块
        self.player = Player(config) # 触发响应词叮咚播放
        
    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    def detected_callback(self):
        self.player.play_ding() # 触发 叮

    def speeched_callback(self, fname):
        self.player.play_dong() # 检测时间到后触发 咚
        self.robot.process(fname) # 将收到的语音传给应用模块执行相应的操作
        # sleep(1) # 等待片刻

    # 启动机器人
    def run(self):
        self.detector.start(detected_callback=self.detected_callback, speeched_callback=self.speeched_callback,
               interrupt_check=self.interrupt_callback,
               sleep_time=0.03)

SmartSpeaker().run()
