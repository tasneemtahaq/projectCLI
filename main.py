import click
from mycliapp.core import TaskManager

tm = TaskManager()

@click.group()
def cli():
    """MyCLIApp: A simple task manager with persistence."""
    pass

@cli.command()
@click.argument("title")
def add(title):
    """Add a new task."""
    t = tm.add(title)
    click.echo(f"Added: {t}")

@cli.command("list")
def _list():
    """List all tasks."""
    tasks = tm.list()
    if not tasks:
        click.echo("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        click.echo(f"{i}. {t}")

@cli.command()
@click.argument("index", type=int)
def done(index):
    """Mark task INDEX as done."""
    try:
        t = tm.complete(index-1)
    except IndexError:
        click.echo("Invalid task number.")
        return
    click.echo(f"Completed: {t}")

if __name__ == "__main__":
    cli()
