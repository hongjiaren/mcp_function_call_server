from flask import Flask, request, jsonify
from server.tools.web_search import search_web
from server.tools.weather_search import get_weather
from server.tools.chat import chat_with_ai

app = Flask(__name__)

@app.route("/function_call", methods=["POST"])
def function_call():
    data = request.get_json()
    function_name = data.get("function")
    arguments = data.get("arguments", {})

    if function_name == "web_search":
        result = search_web(**arguments)
    elif function_name == "weather_search":
        result = get_weather(**arguments)
    elif function_name == "chat":
        result = chat_with_ai(**arguments)
    else:
        return jsonify({"error": "Unknown function"}), 400

    return jsonify({"result": result})

def start_function_call_server():
    app.run(debug=True)
