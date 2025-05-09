from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import aiohttp
import os
from config import BING_SUBSCRIPTION_KEY, BING_SEARCH_URL

router = APIRouter()

class SearchRequest(BaseModel):
    query: str
    history: Optional[List[dict]] = []

class SearchResponse(BaseModel):
    output: str

@router.post("/", response_model=SearchResponse)
async def search(request: SearchRequest):
    try:
        # 这里是一个简单的示例实现
        # 实际应用中，这里应该调用Bing搜索API或其他搜索服务
        headers = {
            "Ocp-Apim-Subscription-Key": BING_SUBSCRIPTION_KEY
        }
        
        params = {
            "q": request.query,
            "count": 5,
            "responseFilter": "Webpages"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(BING_SEARCH_URL, headers=headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    # 处理搜索结果
                    results = data.get("webPages", {}).get("value", [])
                    if results:
                        output = "搜索结果：\n"
                        for result in results[:3]:
                            output += f"- {result['name']}: {result['snippet']}\n"
                    else:
                        output = "未找到相关结果"
                else:
                    output = "搜索服务暂时不可用"
        
        return SearchResponse(output=output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))