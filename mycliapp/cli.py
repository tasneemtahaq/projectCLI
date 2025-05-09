import click
from .core import Task

tasks = []

@click.group()
def cli():
    """MyCLIApp: Manage your tasks."""
    pass

@cli.command()
@click.argument("title")
def add(title):
    """Add a new task."""
    task = Task(title)
    tasks.append(task)
    click.echo(f"Added: {task}")

@cli.command()
def list():
    """List all tasks."""
    for idx, t in enumerate(tasks, 1):
        click.echo(f"{idx}. {t}")
