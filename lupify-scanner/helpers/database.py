from pymongo import MongoClient
import logging

log = logging.getLogger(__name__)


def connect(config):
    log.info('Connecting to database on %s:%s' % (config['mongodb_uri'], config['mongodb_port']))
    #mongoClient = MongoClient(mongodb_uri, 27017)
    #db = mongoClient.lupify
    #db.authenticate(mongodb_user, mongodb_pass)
    #return db