import typer 
from rich import print
from rich.console import Console
from rich.table import Table
from movie import Movie
from db import get_all_movies, delete_movie, insert_movie, watch_movie, update_movie

console = Console()

app = typer.Typer(name="Movie")

@app.command(short_help="Add a new movie")
def add(movie: str, watched:bool, rating: int):
    typer.echo(f"Adding {movie}")
    current_movie = Movie(movie, str(watched), str(rating))
    insert_movie(current_movie)
    show()

@app.command(short_help="Delete a movie")
def remove(position: int):
    typer.echo(f"Removing {position}")
    delete_movie(position-1)
    show()
    
@app.command(short_help="View all movies")
def show():
    all_movie = get_all_movies()
    console.print(r"""[red] /$$      /$$                      /$$                 /$$$$$$$$                           /$$                          
| $$$    /$$$                     |__/                |__  $$__/                          | $$                          
| $$$$  /$$$$  /$$$$$$  /$$    /$$ /$$  /$$$$$$          | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ /$$__  $$|  $$  /$$/| $$ /$$__  $$         | $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
| $$  $$$| $$| $$  \ $$ \  $$/$$/ | $$| $$$$$$$$         | $$| $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
| $$\  $ | $$| $$  | $$  \  $$$/  | $$| $$_____/         | $$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$      
| $$ \/  | $$|  $$$$$$/   \  $/   | $$|  $$$$$$$         | $$| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
|__/     |__/ \______/     \_/    |__/ \_______/         |__/|__/      \_______/ \_______/|__/  \__/ \_______/|__/      
                                                                                                                        
                                                                                                                        
                                                                                                                        [/red]""")
    table = Table(show_header=True,header_style="bold red")
    table.add_column("#", style="dim", width=6)
    table.add_column("Movie", min_width=20)
    table.add_column("Watched?", min_width=10)
    table.add_column("Rating", min_width=10)

    for idx, movie in enumerate(all_movie, start=1):
        is_watched = "✅" if movie.watched == 2 else "❌"
        table.add_row(str(idx), movie.movie, is_watched, str(movie.rating))
    console.print(table)

@app.command(short_help="Watch a movie")
def watch(position: int):
    typer.echo(f'Watch {position}')
    watch_movie(position-1)
    show()


@app.command(short_help="Update a movie")
def update(position: int, movie: str, watched: bool, rating: int):
    typer.echo(f"Updating {movie}")
    update_movie(position-1, movie, watched, rating)
    show()



if __name__ == '__main__':
    app()