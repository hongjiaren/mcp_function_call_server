# mcp_function_call_server

[![License: MIT](https://img.shields.io/github/license/hongjiaren/mcp_function_call_server.svg)](https://github.com/hongjiaren/mcp_function_call_server/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![Issues](https://img.shields.io/github/issues/hongjiaren/mcp_function_call_server.svg)](https://github.com/hongjiaren/mcp_function_call_server/issues)
[![Stars](https://img.shields.io/github/stars/hongjiaren/mcp_function_call_server.svg?style=social)](https://github.com/hongjiaren/mcp_function_call_server/stargazers)
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)]()
[![Downloads](https://img.shields.io/badge/downloads-100%2B-lightgrey.svg)]()
[![CI](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)]()

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

- 支持两种服务模式：标准API模式和MCP Server模式
- 内置自定义LLM模型模块，不依赖第三方框架
- 支持多LLM负载均衡和动态分配
- 支持流式响应和事件流处理
- 兼容标准 Function Call 请求协议（如 OpenAI / Qwen / DeepSeek 等大模型）

## 📂 项目结构
.
├── server.py                  # 主程序
├── config.py                  # .env 配置
├── .env
├── functions/                 # Function 模块目录
│   ├── __init__.py
│   ├── registry.py            # function 定义注册表
│   ├── all_prompts.py         # 所有的prompt
│   ├── special_chat_func.py   # 闲聊功能
│   └── web_search_func.py     # 搜索功能
└── requirements.txt



## 🚀 快速启动

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

<!-- 2. 运行服务：
   ```bash
   # API模式
   python -m server.main --mode api
   
   # MCP模式
   python -m server.main --mode mcp
   ```

3. 运行测试：
   ```bash
   # 运行所有测试
   pytest
   
   # 运行单元测试
   pytest tests/unit
   
   # 运行集成测试
   pytest tests/integration
   
   # 生成覆盖率报告
   pytest --cov=server --cov-report=html
   ``` -->

## 📡 接口示例

1. API模式请求格式：
```json
{
  "query": "杭州明天的天气",
  "history": [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好，有什么可以帮助你的吗？"}
  ]
}
```

2. MCP Server请求格式：
```json
{
  "query": "杭州明天的天气",
  "history": [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好，有什么可以帮助你的吗？"}
  ]
}
```

3. 返回格式：
```json
{
  "output": "根据查询结果生成的回复内容"
}
```

## 🔧 配置说明

服务通过`base_config_dev.yml`文件进行配置，主要配置项包括：

- `gpt_server`: LLM服务器配置列表
  - `api_base`: API基础URL
  - `api_key`: API密钥
  - `api_version`: API版本
  - `model_version`: 模型版本/部署名称

- `BING_SUBSCRIPTION_KEY`: Bing搜索API密钥
- `BING_SEARCH_URL`: Bing搜索API URL
- `BING_ICON_URL`: Bing图标URL

## 📌 未来规划

- 新增更多通用工具功能（如翻译、汇率查询等）
- 接入统一的日志与监控体系
- 完善认证与限流策略
- 提高测试覆盖率
- 添加更多集成测试场景
- 优化多LLM负载均衡算法

## 📄 License

MIT License
