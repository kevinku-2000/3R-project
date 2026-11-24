"""CLI script for the three_r_project package. This will be called on the command line"""

import click

from three_r_project.analysis import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def three_r_project_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
