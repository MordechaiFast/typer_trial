from typer import *

app = Typer()

@app.command()
def hello(name: str):
    echo(f"Hello, {name}!")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        echo(f"Goodnight {name}.")
    else:
        echo(f"Bye {name}!")

app()