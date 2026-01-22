import datetime
class Movie:
    def __init__(self, movie, watched, rating, date_added=None, date_watched=None, position=None):
        self.movie = movie
        self.watched = watched
        self.rating = rating
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat
        self.date_watched = date_watched if date_watched is not None else datetime.datetime.now().isoformat
        self.position = position if position is not None else None
    def __repr__(self) -> str:
        return f"({self.movie}, {self.watched}, {(self.rating)}, {self.date_added}, {self.date_watched}, {self.position})"
        



        
