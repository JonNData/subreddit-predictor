from flask import request, render_template, make_response, jsonify
from flask import current_app as app

# import json
# from sklearn.feature_extraction.text import TfidfVectorizer
# import pickle

# pickled multiple regression model
# clf = pickle.load(open('PICKLED_CLF.pkl','rb'))
# vec = pickle.load('PICKLED_VECTORIZER.pkl')

@app.route('/predict', methods=['POST'])
def make_predict():
    # read in data
    text_inputs = request.get_json(force=True)
    
    # get variables
    title = text_inputs['title']
    selftext = text_inputs['selftext']
    
    # combine
    text = title + ' ' + selftext
    text = list(text)


    def vectorize(text):
        # vect should be pickled here
        test_sparse = vect.transform([test_input])
        return test_sparse
    
    # make prediction USING PICKLED MODEL and convert it to list so that jsonify is happy
    # Ideally the pickled pipeline should take the input all the way to output list
    output = clf(test_sparse.todense(), n_neighbors=5)
    rec_id_list = test_array[1][0]
    recommendations = data.iloc[rec_id_list]["subreddit"]

    # send back the top 5 subreddits and their associated probabilities

    return jsonify(top_five = recommendations)
    


