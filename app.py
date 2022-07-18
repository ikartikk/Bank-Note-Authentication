from pickle import PicklingError
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_in = open('/Users/ikartik/Desktop/python/jupyter/BankNote/rf.pkl','rb')
rf = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict')
def predict_note_authentication():
    Variance = request.args.get('Variance')
    Skewness = request.args.get('Skewness')
    Curtosis = request.args.get('Curtosis')
    Entropy = request.args.get('Entropy')
    prediction = rf.predict([[Variance,Skewness,Curtosis,Entropy]])
    return 'The predicted value is ' + str(prediction)
    #predict?Variance=2&Skewness=3&Curtosis=2&Entropy=1

if __name__ == '__main__':
    app.run()

