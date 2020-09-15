# -*- coding:UTF-8 -*-
import pyaudio, os, random
import wave
import time
import subprocess

# 音频播放器
class Player():
    def __init__(self):
        pass

    def play_ding(self):
        mp3_path = 'ding'
        file_list = os.listdir(mp3_path)
        index = random.randint(0, len(file_list) - 1)
        self.play_music(mp3_path + '/' + file_list[index])

    def play_dong(self):
        mp3_path = 'dong'
        file_list = os.listdir(mp3_path)
        index = random.randint(0, len(file_list) - 1)
        self.play_music(mp3_path + '/' + file_list[index])

    def play_music(self, fname):
        subprocess.Popen(['mpg123', '-a', 'hw:0,0', '-q', fname]).wait()