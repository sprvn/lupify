from sys import exit
from socket import inet_aton
import logging
import re

log = logging.getLogger(__name__)

def string(item):
    log.debug('Validating as string: %s' % (item))
    if not re.match('^[a-z]+$', item, re.I):
        log.warning('Validating failed')
        return False

    log.debug('Validate successful')
    return item

def integer(item):
    log.debug('Validating as integer: %s' % (item))
    if not re.match('^[0-9]+$', item):
        log.warning('Validating failed')
        return False

    log.debug('Validate successful')
    return item

def uri(item):
    log.debug('Validating as string: %s' % (item))
    if not (re.match('^[a-z]+$', item, re.I) or
       re.match('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', item)):
        log.warning('Validating failed')
        return False

    log.debug('Validate successful')
    return item

def username(item):
    log.debug('Validating as string: %s' % (item))
    if not re.match('^[a-z_]+$', item, re.I):
        log.warning('Validating failed')
        return False

    log.debug('Validate successful')
    return item
