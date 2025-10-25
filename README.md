# Python-Chat

![](https://img.shields.io/badge/language%20-python-blue)
![](https://img.shields.io/badge/AIModel%20-ZHIPU-green)

一款基于智谱AI的简单AI对话应用。

## 项目结构

```
Python-Chat
├─chat
│  └─__pycache__
├─init
│  └─__pycache__
├─py-chat.py
└─README.md
```

## 快速开始

### 获取 Api-Key

在[智谱平台](https://bigmodel.cn/)注册账号并获取新的 Api-Key 。

### 从源代码开始

```shell
git clone https://github.com/pykelysia/python-chat.git
cd python-chat

# 然后创建新文件 .env
# 并填入内容 AI_API_KEY = "your-zhipu-api-key"

pip install zai
python python.py
```

### 使用可执行文件

选择 `Release` 中的任意版本，下载相应可执行文件。

在同目录下新建文件 `.env` 并添加

```
AI_API_KEY="your-zhipu-api-key"
```