from typing import Optional

import typer
from typing_extensions import Annotated


app = typer.Typer()


@app.callback()
def callback():
    """
    This will say Hello World!!!!!!
    """


@app.command(help="Say Hello World!!!")
def helloworld(
    dryrun: Annotated[
        Optional[bool],
        typer.Option(
            "--dry-run/--actual-run", help="this will not execute the command"
        ),
    ] = None
):
    """
    Say Hello World
    """
    if dryrun is None:
        typer.echo("This is the default, Hello World")
    elif dryrun:
        typer.echo("Dry run of Hello World")
    else:
        typer.echo("Actual run of Hello World")


if __name__ == "__main__":
    app()
