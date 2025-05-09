from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .registry import register_function
from config import settings
from fastapi.responses import StreamingResponse
import openai
import os
import json

router = APIRouter()

# 注册 function 定义
register_function({
    "name": "special_chat",
    "description": "闲聊功能（流式输出）",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "用户输入的聊天内容"
            }
        },
        "required": ["query"]
    }
})

# 数据模型
class SpecialChatRequest(BaseModel):
    query: str

# 读取 prompt
def get_special_prompt() -> str:
    path = os.path.join(os.path.dirname(__file__), "prompts/special_chat_prompt.txt")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# 流式生成器
def stream_chat_response(prompt, query):
    openai.api_type = settings.azure_api_type
    openai.api_version = settings.azure_api_version
    openai.api_base = settings.azure_api_base
    openai.api_key = settings.azure_api_key

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        engine=settings.azure_engine,
        messages=messages,
        temperature=0.8,
        max_tokens=800,
        stream=True
    )

    # 逐块返回
    for chunk in response:
        if "choices" in chunk:
            delta = chunk["choices"][0]["delta"]
            if "content" in delta:
                yield delta["content"]

# 聊天接口（流式）
@router.post("/special_chat")
async def special_chat(request: SpecialChatRequest):
    try:
        system_prompt = get_special_prompt()
        generator = stream_chat_response(system_prompt, request.query)
        return StreamingResponse(generator, media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
