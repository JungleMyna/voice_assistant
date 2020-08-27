## 在树莓派里使用的HomeAssistant语音助手

因为唤醒词识别率的问题，这里使用默认唤醒词`snowboy`（可以自行申请）

## 运行环境

- 树莓派全系列
- Python2.7

## 依赖安装
```bash
sudo apt-get install python-pyaudio python3-pyaudio python3-pip python-pip sox -y
sudo apt-get install git gcc libatlas-base-dev swig3.0 libpcre3 libpcre3-dev -y
sudo apt-get install mpg123 pulseaudio -y
# 使用python2.7安装依赖
python -m pip install pyaudio
python -m pip install mpg123
python -m pip install baidu-aip
python -m pip install pycrypto
python -m pip install pyyaml
```

## 使用USB声卡时需要配置
```bash
# 检查播放设备
aplay -l
# 检查录音设备
arecord -l

# 设置默认音频设备
nano ~/.asoundrc
```
文件：`~/.asoundrc`
```
pcm.!default {
  type asym
   playback.pcm {
     type plug
     slave.pcm "hw:0,0"
   }
   capture.pcm {
     type plug
     slave.pcm "hw:1,0"
   }
}
```

## 配置

配置HomeAssistant的token长令牌
```yaml
name: snowboy
url: http://localhost:8123
token: 长令牌
app_id: 百度语音识别
api_key: 百度语音识别
secret_key: 百度语音识别
```

## 遇到的问题

> IOError: [Errno Invalid sample rate] -9997这个问题
```bash
pulseaudio --start
```

## 详细文档请查看源项目

https://github.com/x2018/Voice_assistant_Xiao_Er

## 唤醒词识别文档

https://snowboy.kitt.ai/docs