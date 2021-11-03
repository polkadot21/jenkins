from flask import Flask, render_template, request
from joblib import load
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/model')
def model():
    return render_template("model.html")

@app.route('/regressor', methods=['POST'])
def predict_regression():
    """Predict X values"""

    int_feature = [int(x) for x in request.form.values()]
    print('')
    print(int_feature)
    print('')
    final_feature = np.array([[1, int_feature[0]]])

    df = pd.DataFrame(data=final_feature, columns=["const", "Age"])

    #upload the model
    model_regressor = load("model/model.joblib")
    #make predicitons
    predictions = model_regressor.fit().predict(df)
    output = int(predictions[0])
    return render_template('model.html', prediction_text='Height is {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)