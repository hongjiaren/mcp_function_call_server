from server.tools.web_search import search_web
from server.tools.weather_search import get_weather
from server.tools.chat import chat_with_ai
from mcp import MCPServer

def mcp_function_call(request):
    function_name = request.get("function")
    arguments = request.get("arguments", {})

    if function_name == "web_search":
        return search_web(**arguments)
    elif function_name == "weather_search":
        return get_weather(**arguments)
    elif function_name == "chat":
        return chat_with_ai(**arguments)
    else:
        return {"error": "Unknown function"}

def start_mcp_server():
    mcp_server = MCPServer()
    mcp_server.add_function(mcp_function_call)
    mcp_server.start()
