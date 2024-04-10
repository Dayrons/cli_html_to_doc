from peewee import Model, CharField
from config.databases import db

class Config(Model):
    path_templates = CharField()
    path_export = CharField()

    class Meta:
        database = db