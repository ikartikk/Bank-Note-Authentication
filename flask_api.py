from pickle import PicklingError
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
pickle_in = open('rf.pkl','rb')
rf = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict')
def predict_note_authentication():

    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Variance
        in: query
        type: number
        required: true
      - name: Skewness
        in: query
        type: number
        required: true
      - name: Curtosis
        in: query
        type: number
        required: true
      - name: Entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    Variance = request.args.get('Variance')
    Skewness = request.args.get('Skewness')
    Curtosis = request.args.get('Curtosis')
    Entropy = request.args.get('Entropy')
    prediction = rf.predict([[Variance,Skewness,Curtosis,Entropy]])
    return 'The predicted value is ' + str(prediction)
    #predict?Variance=2&Skewness=3&Curtosis=2&Entropy=1


@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=rf.predict(df_test)
    
    return str(list(prediction))




if __name__ == '__main__':
    app.run()
#link/apidocs
