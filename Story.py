from peewee import *
from BaseModel import BaseModel
from Status import Status


class Story(BaseModel):
    story_title = CharField()
    user_story = TextField()
    acceptance_criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = ForeignKeyField(Status)