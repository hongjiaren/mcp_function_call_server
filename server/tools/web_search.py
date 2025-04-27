import requests

def search_web(query):
    response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
    data = response.json()
    return data.get("AbstractText", "No information found.")
