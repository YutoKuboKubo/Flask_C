from flask_script import Command
from app import db
from app.models.user import User


class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()
