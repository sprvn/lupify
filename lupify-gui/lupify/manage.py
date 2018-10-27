from lupify import app, db
from lupify.models import User
from flask_script import Manager, prompt_bool
from pymongo import MongoClient

manager = Manager(app)

@manager.command
def initdb():
    #print("Initializing SQLite database")
    #db.create_all()
    #db.session.add(User(username="kevgus"))
    #db.session.commit()
    #print("SQLite database initialized")

    print("Initializing MongoDB database")
    mongoClient = MongoClient('127.0.0.1', 27017)
    mongodb = mongoClient.admin
    mongodb.authenticate('mongoadmin', 'secret')
    collection = mongodb.users
    collection.insert_one({'username': 'kevgus'})
    print("MongoDB database initialized")
    


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to drop the database"):
        db.drop_all()
        print("Database dropped")

if __name__ == '__main__':
    manager.run()