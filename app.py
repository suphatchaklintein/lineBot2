from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นางสาวสุภัชชา กลิ่นเทียน เลขที่ 22 ชั้น ม.4/4"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    userText = decoded["events"][0]['message']['text']
    if (a2 == 'สวัสดี');
        print('ดีด้วยจ้า);
    else (a2 == 'สบายดีไหม')
        print('ยังไม่ตายค่ะ);
    else ;
         print('ว่าอะไรค่ะ);
    return '',200
