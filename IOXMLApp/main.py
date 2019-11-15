"""
This is Flask Application for ML.
"""
import pickle
from flask import Flask, jsonify, request
import pandas as pd

# load model
MODEL = pickle.load(open('iotmodel.pkl', 'rb'))

# app
APP = Flask(__name__)

# routes
@APP.route('/', methods=['POST'])

def predict():
    """
        To predit the data
    """
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = MODEL.predict(data_df)

    # send back to browser
    output = {'Active Power': (result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8000)
