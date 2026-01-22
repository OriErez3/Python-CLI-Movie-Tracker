import sqlite3
from typing import List
import datetime
from movie import movie

conn = sqlite3.connect('movies.db')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS movies (
              movie text,
              watched boolean,
              rating integer,
              date_added text,
              date_watched text
              position integer)""")

create_table()

def insert_movie(movie: movie):
    c.execute('select count(*) FROM movies')
    count = c.fechone()[0]
    movie.position = count if count else 0
    with conn: 
        c.execute('INSERT INTO movies VALUES (:movie, :watched, :rating, :date_added, :date_watched, :position)', 
                  {'movie': movie.movie, 'watched': movie.watched, 'rating': movie.rating, 'date_added': movie.date_added, 'date_watched': movie.date_watched, 'position': movie.position})


def get_all_movies()->List[movie]:
    c.execute("select * from movies")
    results = c.fetchall()
    movies = []
    for result in results:
        movies.append(movie(*result))
    return movie
