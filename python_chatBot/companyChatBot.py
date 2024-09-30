from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  # CORS 활성화

# Gemini API 키 설정
os.environ['GOOGLE_API_KEY'] = "AIzaSyAFJYfdRVCJKHAJabsPxiXYS8xs12LMUEk"  # 여기에 실제 API 키를 입력하세요

# Gemini 모델 설정
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

# 전역 변수로 채팅 세션 저장
chat_session = model.start_chat(history=[])

def chat_with_gemini(prompt):
    try:
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json(force=True)
        if not data or 'message' not in data:
            return jsonify({'error': 'Invalid request data'}), 400
        
        user_message = data['message']
        response = chat_with_gemini(user_message)
        print(response)
        response.encode('utf-8')
        print(response)
        return jsonify({'response': response})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)