import os

import click
import sqlalchemy_data_model_visualizer

from .users import User
from .pings import Ping


@click.group()
def main():
    pass


@main.command()
def graph_models():
    models = [
        Ping,
        User,
    ]
    sqlalchemy_data_model_visualizer.generate_data_model_diagram(models, "gabby/models", add_labels=True)
    os.unlink("gabby/models")


if __name__ == "__main__":
    main()
