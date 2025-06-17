from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load model and preprocessing tools
model = pickle.load(open('final_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
pca = pickle.load(open('pca.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict_csv', methods=['POST'])
def predict_csv():
    try:
        file = request.files['file']
        df = pd.read_csv(file)

        if 'class' in df.columns:
            df = df.drop(columns=['class'])

        scaled = scaler.transform(df)
        reduced = pca.transform(scaled)
        predictions = model.predict(reduced)

        return jsonify({'predictions': predictions.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)