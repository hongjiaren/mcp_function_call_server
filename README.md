# mcp_function_call_server

[![License: MIT](https://img.shields.io/github/license/hongjiaren/mcp_function_call_server.svg)](https://github.com/hongjiaren/mcp_function_call_server/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![Issues](https://img.shields.io/github/issues/hongjiaren/mcp_function_call_server.svg)](https://github.com/hongjiaren/mcp_function_call_server/issues)
[![Stars](https://img.shields.io/github/stars/hongjiaren/mcp_function_call_server.svg?style=social)](https://github.com/hongjiaren/mcp_function_call_server/stargazers)
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)]()
[![Downloads](https://img.shields.io/badge/downloads-100%2B-lightgrey.svg)]()
[![CI](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

---
# mcp_function_call_server

## 📖 项目简介

`mcp_function_call_server` 是一个为大语言模型（LLM）设计的外部 Function Call 工具服务，兼容当前主流的大模型 Function Call 标准及最新的 MCP Server 接入规范。通过该服务，大模型可以灵活调用外部工具，扩展自身能力，获取实时信息或执行特定功能。

## 🎯 功能概览

目前服务内置以下功能模块：

- **Web Search**：调用在线搜索服务，获取实时网页搜索结果。
- **Weather Query**：查询指定城市的实时天气信息。
- **Chat**：进行简单闲聊对话，作为功能示例。

未来可灵活扩展更多 Function Call 工具。

## 📦 服务架构

- 兼容标准 Function Call 请求协议（如 OpenAI / Qwen / DeepSeek 等大模型）
- 同时支持 MCP Server 调用方式，便于集成到多模型统一控制平台

## 📂 项目结构

mcp_function_call_server/
├── server/
│   ├── __init__.py
│   ├── main.py                # 启动服务的主程序
│   ├── function_call_server.py # 传统服务调用处理
│   ├── mcp_server.py          # MCP 服务处理
│   ├── tools/
│   │   ├── web_search.py      # Web 搜索工具
│   │   ├── weather_query.py   # 天气查询工具
│   │   └── chat.py            # 闲聊工具
│   └── utils.py               # 公用工具类文件
├── config/
│   ├── config.yaml            # 服务配置文件
│   └── logging_config.yaml    # 日志配置文件
├── requirements.txt           # 项目依赖文件
├── .gitignore                 # Git 忽略文件
├── LICENSE                    # 开源协议文件
└── README.md                  # 项目说明文件




## 🚀 快速启动

1. 安装依赖：
   ```bash
   pip install -r requirements.txt


2. 运行服务

python server/main.py


## 📡 接口示例

1. Function Call 请求格式

{
  "function": "web_search",
  "arguments": {
    "query": "今天的新闻"
  }
}

2. MCP Server 请求格式：
{
  "tool_name": "web_search",
  "params": {
    "query": "今天的新闻"
  }
}

3. 返回格式：

{
  "result": "搜索结果内容"
}

## 📌 未来规划

新增更多通用工具功能（如翻译、汇率查询等）
接入统一的日志与监控体系
完善认证与限流策


## 📄 License

MIT License
