from peewee import *
from BaseModel import *
from Story import Story
from Status import Status


class DbHandler:

    def __init__(self):
        self.db = db

    def db_connect(self):
        self.db.connect()

    def build_tables(self):
        self.db.create_tables([Story, Status], safe=True)

    @staticmethod
    def populate_status():
        Status.create(name='planning')
        Status.create(name='to do')
        Status.create(name='in progress')
        Status.create(name='review')
        Status.create(name='done')

    def init_db(self):
        self.db_connect()
        self.build_tables()
        if Status.select().count() == 0:
            self.populate_status()

