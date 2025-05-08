import click
import os
from Repository import Repository

project_path = os.getcwd()

my_repository = Repository(project_path)


@click.group()  #יוצר קבוצה של פקודות CLI
def cli():
    """ Wit Version Control CLI """
    pass


@cli.command()  #פקודה נפרדת ב-CLI
def init():
    try:
        my_repository.wit_init()
        click.echo(f"Initialized empty Wit repository in {my_repository.current_directory}")
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.argument('name_file')
def add(name_file):
    try:
        my_repository.wit_add(name_file)
        click.echo(f'File {name_file} Added successfully')
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.argument('message')
def commit(message):
    try:
        my_repository.wit_commit(message)
        click.echo(f'Committed {message} Succeeded:)')
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
def log():
    try:
        my_repository.wit_log()
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
def status():
    try:
        my_repository.wit_status()
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.argument('id_of_commit')
def checkout(id_of_commit):
    try:
        my_repository.wit_checkout(id_of_commit)
        click.echo(f'Checked out {id_of_commit} Succeeded:)')
    except Exception as e:
        click.echo(f"Error: {e}")
    # הוספת הפקודות לקבוצת ה-CLI


cli.add_command(init)
cli.add_command(add)
cli.add_command(commit)
cli.add_command(log)
cli.add_command(status)
cli.add_command(checkout)
