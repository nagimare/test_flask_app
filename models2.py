from peewee import *
from datetime import datetime

db = PostgresqlDatabase(
    'flask2_db',
    host = 'localhost',
    port = '5432',
    user = 'flask2_user',
    password = '123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    name = CharField(max_length=255, null=False)
    username = CharField(max_length=255, null=False)
    email = CharField(max_length=255, null=False)
    recording = CharField(max_length=255, null=False)
    time = CharField(max_length=255, null=False)
    date = DateField(default=datetime.now)
    
    


    def __repr__(self):
        return self.title

db.create_tables([Post])

db.close()