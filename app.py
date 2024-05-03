# app.py
import json
from flask import Flask, request, jsonify
from model import predict  # model.py에서 predict 함수 가져오기
import model

from flask import Flask, request, render_template
import json
from werkzeug.utils import secure_filename
from socket import *

app = Flask(__name__)

@app.route('/')
def home():
    return '성공!!'

@app.route('/test')
def test():
    test_data = '코딩테스트 공부하기'
    prediction = model.predict(test_data)
    return prediction

@app.route('/predict', methods=['POST'])
def predict():

    # SpringBoot로부터 checklist 전달 'str'
    checklist = request.get_json()        
	
   	# SpringBoot에서 받은 데이터를 출력해서 확인
    print('>>> Data from SpringBoot :', checklist)
    # print(type(checklist))

    global category
    category = model.predict(checklist)
    print('>>> Checklist Category prediction :', category)

    return category

@app.route('/send')
def send():
    return category


if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)
