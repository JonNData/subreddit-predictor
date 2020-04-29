from flask import request, jsonify
from flask import current_app as app
import numpy as np 
import pandas as pd 
import json
import pickle

# pickled vectorizer and classifier
with open('vectorizer.pkl', 'rb') as file:
    vec_pickle = pickle.load(file)

with open('SGDClassifier.pkl', 'rb') as file1:
    clf_pickle = pickle.load(file1)

# endpoint for sending the post    
@app.route('/predict', methods=['POST'])
def make_predict():
    # read in data
    text_inputs = request.get_json(force=True)
    
    # get variables
    title = text_inputs['title']
    selftext = text_inputs['body']
    
    # combine
    text = title + ' ' + selftext

    # vect should be pickled here
    text_vect = vec_pickle.transform([text])
    
    # make prediction USING PICKLED MODEL and convert it to list so that jsonify is happy
    output = clf_pickle.predict(text_vect)

    # send back the top 5 subreddits and their associated probabilities

    return jsonify(output[0])
    


