import os
import pathlib

import click
from click import echo
from click_default_group import DefaultGroup

from tilly.plugin import hookimpl
from tilly.utils import add_config_to_env, static_folder

from datasette.app import Datasette
from asgiref.sync import async_to_sync


root = pathlib.Path.cwd()

@hookimpl
def til_command(cli):
    @cli.group(
        cls=DefaultGroup,
        default="default",
        default_if_no_args=True,
    )
    @click.version_option(message="tilly-{{ cookiecutter.hyphenated }}, version %(version)s")
    def {{ cookiecutter.underscored }}():
        """{{ cookiecutter.description }}"""

    @{{ cookiecutter.underscored }}.command("default")
    def default():
        add_config_to_env()
        echo("<implement your plugin here>")

