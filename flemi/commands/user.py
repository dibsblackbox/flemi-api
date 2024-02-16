import click
from flask import Flask

def register_user_group(app: Flask, db):
    user_group = app.cli.group("user", help="User commands")

    @user_group.command("query")
    @click.option("--username", default=None, help="query from username")
    @click.option("--email", default=None, help="query from email")
    @click.option("--name", default=None, help="query from name")
    @click.option("--location", default=None, help="query from location")
    def query(username, email, name, location):
        """
        Query user information and return the user IDs as a list.
        """
