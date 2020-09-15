# -*- coding:UTF-8 -*-
import shutil, os, re

# 语音识别
class Recognition():
    def __init__(self):
        pass

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
        return self.xunfei_recognize(fname)