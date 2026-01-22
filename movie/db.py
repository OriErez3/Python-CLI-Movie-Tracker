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

def delete_movie(position):
    c.execute("select count(*) from movies")
    count = c.fetchone()[0]

    with conn: 
        c.execute("DELETE from movies WHERE position=:position", {"position": position})
        for pos in range(position+1, count):
            change_position(pos, pos-1, False)

def change_position(old_position: int, new_position: int, commit=True):
    c.execute('UPDATE movies SET position = :position_new WHERE position = :position_old',
              {'position_old': old_position, 'position_new': new_position})
    if commit:
        conn.commit()

