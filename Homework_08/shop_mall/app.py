# 强制容器全局UTF8编码，解决中文乱码
import os
os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ["LANG"] = "C.UTF-8"

from flask import Flask, render_template, request, jsonify
import pymysql
import requests

app = Flask(__name__)

# 数据库连接，指定utf8mb4字符集
def get_db_conn():
    conn = pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PWD"),
        database=os.getenv("MYSQL_DB"),
        charset="utf8mb4"
    )
    return conn

# 商城首页
@app.route("/")
def index():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM goods")
    goods_list = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", goods=goods_list)

# MCP智能客服接口，调用8000代理访问大模型
@app.route("/chat_ai", methods=["POST"])
def chat_ai():
    user_msg = request.form.get("msg")
    mcp_url = os.getenv("MCP_URL")
    req_data = {
        "model": "qwen3:0.6b",
        "messages": [{"role":"user","content":f"你是商城客服，简短回答：{user_msg}"}]
    }
    resp = requests.post(mcp_url, json=req_data)
    return jsonify(ans=resp.json()["message"]["content"])

# 用户下单接口
@app.route("/buy", methods=["POST"])
def buy_goods():
    user_id = request.form.get("uid")
    goods_id = request.form.get("gid")
    num = int(request.form.get("num"))
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO orders(user_id,goods_id,buy_num) VALUES(%s,%s,%s)",(user_id,goods_id,num))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(msg="下单成功！")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)