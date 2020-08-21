## 在树莓派里使用的HomeAssistant语音助手

因为唤醒词识别率的问题，这里使用默认唤醒词`snowboy`（可以自行申请）

## 运行环境

- 树莓派全系列
- Python3

## 依赖安装
```bash
sudo apt-get install python-pyaudio python3-audio python3-pip python-pip sox
sudo apt-get install git gcc libatlas-base-dev swig3.0 libpcre3 libpcre3-dev

pip install mpg123
pip install baidu-aip
pip install pycrypto
```

## 配置

配置HomeAssistant的token长令牌
```yaml
ha_token: HA长令牌
```

## 详细文档请查看源项目

https://github.com/x2018/Voice_assistant_Xiao_Er

## 唤醒词识别文档

http://docs.kitt.ai/snowboy/