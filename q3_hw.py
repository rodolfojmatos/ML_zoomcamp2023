import pickle

def car(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

dv = car('dv.bin')
model = car('model1.bin')

customer = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([customer])

y_pred = model.predict_proba(X)[0, 1]

print('output:', y_pred)

