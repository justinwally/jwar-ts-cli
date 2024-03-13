from jwarcli.commands.hello import hello
import typer

app = typer.Typer()
app.add_typer(hello.app, name="say")
