# app.py
import json
from flask import Flask, request, jsonify
from model import predict  # model.py에서 predict 함수 가져오기

app = Flask(__name__)

@app.route('/test') # /
def home():
    test_data = '코딩테스트 공부하기'
    pred = predict(test_data)
    return pred

@app.route('/predict', methods=['POST'])
def predict_api():
    # JSON 요청을 파싱
    data = request.json
    sentence = data['sentence']
    if sentence is None:
        return 'sentence parameter is missing', 400
    # 예측 수행
    prediction = predict(sentence)

    return prediction
    

if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)