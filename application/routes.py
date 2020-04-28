from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, RedditPost, User
import json
from sklearn.feature_extraction.text import TfidfVectorizer

@app.route('/', methods=['GET'])
def create_user():
    """Create a user."""
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing_user:
            return make_response(f'{username} ({email}) already created!')
        new_user = User(username=username,
                        email=email,
                        created=dt.now()
                        )  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return render_template('users.html',
                           users=User.query.all(),
                           title="Show Users")

@app.route('/predict', methods['POST'])
def make_predict():
    # read in data
    text_inputs = request.get_json(force=True)
    
    # get variables
    title = text_inputs['title']
    selftext = text_inputs['selftext']
    
    # combine
    text = title + ' ' + selftext
    text = list(text)

# should be done with pickled vectorizer
    # def vectorize(text):
    #     vect = TfidfVectorizer(
    #                 max_features=400,
    #                 min_df=1,
    #                 ngram_range=(1, 2),
    #                 stop_words='english'
    #                 )
        # Learn vocabulary and idf, return term-document matrix.
        # tdm = vect.fit_transform(text)

    def vectorize(text):
        # vect should be pickled here
        test_sparse = vect.transform([test_input])
        return test_sparse
    
    # make prediction USING PICKLED MODEL and convert it to list so that jsonify is happy
    # Ideally the pickled pipeline should take the input all the way to output list
    output = nn.kneighbors(test_sparse.todense(), n_neighbors=5)
    rec_id_list = test_array[1][0]
    recommendations = data.iloc[rec_id_list]["subreddit"]

    # send back the top 5 subreddits and their associated probabilities

    return jsonify(top_five = recommendations)
    


