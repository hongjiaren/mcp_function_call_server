from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functions import chat_func, registry
from functions import web_search_func, chat_func
import uvicorn

app = FastAPI(
    title="MCP Function Call Server",
    description="为大语言模型设计的标准化 Function Call 服务",
    version="1.0.0"
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 加载 function 路由
app.include_router(chat_func.router, prefix="/function")
app.include_router(web_search_func.router, prefix="/function")

# 查看所有注册的 function 定义
@app.get("/function/list")
async def list_functions():
    return registry.function_registry

# 欢迎页
@app.get("/")
async def root():
    return {"message": "Welcome to MCP Function Call Server"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=17315, reload=True)
