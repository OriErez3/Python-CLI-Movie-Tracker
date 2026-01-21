import typer 
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer(name="Movie")

@app.command(short_help="Add a new movie")
def add(movie: str, watched:bool, rating: int):
    typer.echo(f"Adding {movie}")
    show()

@app.command(short_help="Delete a movie")
def remove(movie: str):
    typer.echo(f"Removing {movie}")
    show()
    
@app.command(short_help="View all movies")
def show():
    testTable = [("Interstellar", True, 10), ("Marty Supreme", True, 7)]
    console.print('[red]Test[/red]')
    table = Table(show_header=True,header_style="bold red")
    table.add_column("#", style="dim", width=6)
    table.add_column("Movie", min_width=20)
    table.add_column("Watched?", min_width=10)
    table.add_column("Rating", min_width=10)

    for idx, movie in enumerate(testTable, start=1):
        is_watched = "✔" if True == 2 else "Ⅹ"
        table.add_row(str(idx), movie[0], str(movie[1]), str(movie[2]))
    console.print(table)



@app.command(short_help="Update a movie")
def update(movie: str, watched: bool, rating: int):
    typer.echo(f"Updating {movie}")
    show()



if __name__ == '__main__':
    app()