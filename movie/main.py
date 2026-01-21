import typer 
from rich import print
from rich import console
from rich import table



app = typer.Typer(name="Movie")

@app.command(short_help="Add a new movie")
def add(movie: str, watched:bool, rating: int):
    typer.echo(f"Adding {movie}")

@app.command(short_help="Delete a movie")
def remove(movie: str):
    typer.echo(f"Removing {movie}")
    

@app.command()
def update(movie: str, watched: bool, rating: int):
    typer.echo(f"Updating {movie}")



if __name__ == '__main__':
    app()