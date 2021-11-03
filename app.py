from flask import Flask, render_template, request
from joblib import load
import pandas as pd
import numpy as np

app = Flask(__name__)


def check_age(int_feature):
    if int_feature > 20:
        int_feature = 20
    elif int_feature < 0:
        int_feature = 0.1
    return int_feature


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/model')
def model():
    return render_template("model.html")

@app.route('/regressor', methods=['POST'])
def predict_regression():
    """Predict X values"""

    int_feature = [int(x) for x in request.form.values()]

    int_feature = check_age(int_feature[0])

    final_feature = np.array([[1, int_feature]])

    df = pd.DataFrame(data=final_feature, columns=["const", "Age"])

    #upload the model
    model_regressor = load("model/model.joblib")
    #make predicitons
    predictions = model_regressor.fit().predict(df)
    output = int(predictions[0])
    return render_template('model.html', prediction_text='Height is {}'.format(output))

@app.route('/test')
def hello_world():
    return "Hello, world!\n"

if __name__ == '__main__':
    app.run(debug=True)