import typer 
from rich import print

app = typer.Typer(name="Movie")

@app.command()
def drive(miles: int, direction: str = typer.Option("north", "--direction", "-d")):
    print(f"[green]Going on a {miles} mile drive {direction}[/green]")

@app.command()
def stop():
    print("[red]stopping[/red]")


if __name__ == '__main__':
    app()