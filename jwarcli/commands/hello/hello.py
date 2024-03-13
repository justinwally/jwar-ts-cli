import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    This will say Hello World
    """


@app.command()
def hello():
    """
    Say Hello
    """
    typer.echo("Hello")


@app.command()
def world():
    """
    Say World
    """
    typer.echo("World")


if __name__ == "__main__":
    app()
