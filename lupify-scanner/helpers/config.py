from configparser import ConfigParser
from socket import inet_aton
from re import sub
from sys import exit
import helpers.validators as validators
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
        'config_level'
    ]
    log.debug('Loading keys: %s' % (','.join(config_keys)))
    config_file = ConfigParser()
    config_file.read('config.ini')

    if 'DEFAULT' not in config_file:
        log.critical('Failed to read configuration')
        exit(1) 
        
    # Dynamically read configuration and validate them
    for key in config_keys:
        if key in config_file['DEFAULT']:
            log.debug('Validating %s' % (key))
            validate = globals()['validate_%s' % (key)]
            log.debug('Validating %s' % (key))
            config[key] = validate(config_file['DEFAULT'][key])
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

def validate_config_level(config_level):
    return validators.string(config_level)

def validate_mongodb_uri(mongodb_uri):
    return validators.uri(mongodb_uri)
def validate_mongodb_port(mongodb_port):
    return validators.integer(mongodb_port)
def validate_mongodb_user(mongodb_user):
    return validators.username(mongodb_user)
def validate_mongodb_pass(mongodb_pass):
    return mongodb_pass