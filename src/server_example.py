from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)

@app.route('/data')
def read_uart():
    # 使用随机数据模拟UART读取
    fake_data = random.randint(0, 100)  # 生成0到100之间的随机数
    return jsonify({'data': fake_data})

if __name__ == '__main__':
    CORS(app)  # 启用CORS
    app.run(debug=True)
