#!/bin/bash

# 写入文件
sudo cat>/etc/systemd/system/voice_assistant.service<<EOF
[Unit]
Description=voice_assistant
After=network.target

[Service]
ExecStart=/usr/bin/python main.py
WorkingDirectory=/home/pi/git/voice_assistant
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOF

# 开始运行
sudo systemctl start voice_assistant

# 查看状态
sudo systemctl status voice_assistant.service

# 查看日志
sudo grep "voice_assistant" /var/log/syslog