from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
# 修正服务名 ollama_llm
OLLAMA_API = "http://ollama_llm:11434"

@app.route("/api/chat", methods=["POST"])
def chat():
    req_json = request.get_json()
    req_json["stream"] = False
    res = requests.post(f"{OLLAMA_API}/api/chat", json=req_json)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)