from peewee import *


db = PostgresqlDatabase('super_sprinter_3000', user='okocsis90', password='skatanic')


class BaseModel(Model):
    class Meta:
        database = db


class Story(BaseModel):
    story_title = CharField()
    user_story = CharField()
    acceptance_criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()


class Status(BaseModel):
    status = CharField()


db.connect()
if Story.table_exists():
    db.drop_table(Story)
if Status.table_exists():
    db.drop_table(Status)
db.create_tables([Story, Status], safe=True)


Status.create(status='planning')
Status.create(status='to do')
Status.create(status='in progress')
Status.create(status='review')
Status.create(status='done')