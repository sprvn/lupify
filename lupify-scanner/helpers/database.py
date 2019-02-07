from pymongo import MongoClient
from sys import exit
import logging

log = logging.getLogger(__name__)


def connect(config):
    log.info('Attempting to connect to database on %s:%s' %
        (config['mongodb_uri'], 
         config['mongodb_port']))

    _check_config(config)

    mongoClient = MongoClient(str(config['mongodb_uri']), int(config['mongodb_port']))
    db = mongoClient.lupify
    if not config['mongodb_user']:
        print('sdf')
    i = 5
    while i > 0:
        if i < 5:
            log.info('Reattempting to connect to database')
        i -= 1
        try:
            db.authenticate(str(config['mongodb_user']), str(config['mongodb_pass']))
            break
        except Exception as e:
            log.error('Failed to connect to database: %s' % (e))
            if i == 0:
                log.critical('Unable to connect to database: %s' % (e))
                exit(1)
    log.info('Connection to database established')
    return db

def _check_config(config):
    log.debug('Verifying database authentication configuration is set')
    for var in ['uri', 'port', 'user', 'pass']:
        _t = 'mongodb_%s' % (var)
        log.debug('Verifying {}'.format(_t))
        if not _t in config:
            log.error('{} configuration not found'.format(_t))
            exit(1)
        elif not config[_t]:
            log.error('{} configured incorrectly'.format(_t))
            exit(1)
