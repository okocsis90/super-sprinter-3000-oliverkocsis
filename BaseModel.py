from peewee import *

db = PostgresqlDatabase('super_sprinter_3000', user='okocsis90', password='skatanic')


class BaseModel(Model):
    class Meta:
        database = db
