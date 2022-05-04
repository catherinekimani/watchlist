from urllib import response
from . import db

class User(db.model):
    __table__name = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    
    def __repr__(self):
        return f'User {self.username}'
    
class Movie:
    '''
    Movie class to define movie objects
    '''
    
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/' + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        
class Review:
    '''
    review class
    '''
    all_reviews = []
    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review
        
    def save_review(self):
        Review.all_reviews.append(self)
        
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
        
    @classmethod
    def get_reviews(cls,id):
        response = []
        
        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)
                
        return response
        