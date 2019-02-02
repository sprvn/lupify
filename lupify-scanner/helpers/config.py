from configparser import ConfigParser
from socket import inet_aton
from re import sub
from sys import exit
import helpers.validators as validators
import helpers.parsers as parsers
import logging

log = logging.getLogger(__name__)

def read_configuration():
    '''
    Read configuration for the scanner:
    1. If available from DB
    2. If available from file
    3. Use default configuration
    '''

    config = read_config_file()
    if config:
        d_config = default_config()
        return {**d_config, **config}
    else:
        return default_config()

def read_config_file():
    '''
    Read configuration from file.
    '''

    log.info('Loading configuration from file')
    config = {}

    config_keys = [
        'mongodb_uri',
        'mongodb_port',
        'mongodb_user',
        'mongodb_pass',
    ]
    log.debug('Loading keys: %s' % (','.join(config_keys)))
    config_file = ConfigParser()
    config_file.read('config.ini')

    if 'DEFAULT' not in config_file:
        log.critical('Failed to read configuration')
        exit(1) 
        
    # Dynamically read configuration, parse and validate them
    for key in config_keys:
        if key in config_file['DEFAULT']:
            log.debug('Parsing %s' % (key))
            parse = globals()['parse_%s' % (key)]
            log.debug('Validating %s' % (key))
            validate = globals()['validate_%s' % (key)]
            tmp_conf = parse(config_file['DEFAULT'][key])
            config[key] = validate(tmp_conf)
        else:
            log.warning('Did not find %s in configuration' % (key))
    log.info('Configuration loaded')

    return config

def default_config():
    '''
    Return default configuration.
    '''
    return {
        'queue': 'local'
        }

def parse_targets(targets):
    return parsers.parse_targets(targets)

def parse_db(db):
    return parsers.parse_db(db)

def parse_mongodb_uri(mongodb_uri):
    return parsers.parse_mongodb_uri(mongodb_uri)
def parse_mongodb_port(mongodb_port):
    return parsers.parse_mongodb_port(mongodb_port)
def parse_mongodb_user(mongodb_user):
    return parsers.parse_mongodb_user(mongodb_user)
def parse_mongodb_pass(mongodb_pass):
    return mongodb_pass


def validate_targets(targets):
    return validators.validate_targets(targets)

def validate_db(db):
    return validators.validate_db(db)

def validate_mongodb_uri(mongodb_uri):
    return validators.validate_mongodb_uri(mongodb_uri)
def validate_mongodb_port(mongodb_port):
    return validators.validate_mongodb_port(mongodb_port)
def validate_mongodb_user(mongodb_user):
    return validators.validate_mongodb_user(mongodb_user)
def validate_mongodb_pass(mongodb_pass):
    return mongodb_pass