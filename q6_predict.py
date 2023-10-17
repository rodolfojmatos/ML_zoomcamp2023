import pickle

from flask import Flask
from flask import request
from flask import jsonify


def load(model_file: str):
    with open(model_file, 'rb') as f_in:
        return pickle.load(f_in)

dv = load('dv.bin')
model = load('model2.bin')

app = Flask('credit')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    get_card = y_pred >= 0.5

    result = {
        'get_card_probability': float(y_pred),
        'get_card': bool(get_card)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)