import mcp_server
import function_call_server

def main():
    # 启动 MCP 服务
    mcp_server()

    # 启动传统服务调用处理
    function_call_server()

if __name__ == "__main__":
    main()
