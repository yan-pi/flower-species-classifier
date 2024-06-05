from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Carrega o modelo
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({'prediction': int(prediction[0])})

@app.route('/ping', methods=['GET'])
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
