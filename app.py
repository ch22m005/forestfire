import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler




app = Flask(__name__)

# # import ridge regressor model and standard scaler pickel
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler_model = pickle.load(open('models/scaler.pkl', 'rb'))


# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

## Route for home page
@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
      Tempreature = float(request.form.get('Tempreature'))
      RH = float(request.form.get('RH'))
      Ws = float(request.form.get('Ws'))
      Rain = float(request.form.get('Rain'))
      FFMC = float(request.form.get('FFMC'))
      DMC = float(request.form.get('DMC'))
      ISI = float(request.form.get('ISI'))
      Region = float(request.form.get('Region'))
      
      new_data_scaled = StandardScaler.transform([[Tempreature, RH, Ws, Rain,FFMC,DMC, ISI, Classes, Region]])
      result = ridge_model.predict(new_data_scaled)
      return render_template('home.html', result = result[0])
     
    else:
        return render_template('home.html')




if __name__=="__main__":
    app.run(host="0.0.0.0")
