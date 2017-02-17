from BaseModel import BaseModel
from peewee import *


class Status(BaseModel):
    name = CharField()
