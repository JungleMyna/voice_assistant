# -*- coding:UTF-8 -*-

import re
text = "我想打开灯"

matchObj = re.match(r'.*((打开|关闭)(.+))', text)
if matchObj is not None:
    print(matchObj.group(1))
    print(matchObj.group(3))