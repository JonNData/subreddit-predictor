from . import db


class RedditPost(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'RedditPost'
    id = db.Column(db.String,
                   primary_key=True,
                         nullable=False)
    subreddit = db.Column(db.String(64),
                         index=False,
                         unique=False,
                         nullable=False)
    title = db.Column(db.String(255),
                      index=True,
                      unique=True,
                      nullable=False)
    selftext = db.Column(db.Text,
                    index=False,
                    unique=False,
                    nullable=True)

    def __repr__(self):
        return '<RedditPost {}>'.format(self.id)
