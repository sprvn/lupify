from sys import exit
from socket import inet_aton
import ipaddress
import logging
import re

log = logging.getLogger(__name__)

def string(item):
    log.debug('Validating as string: %s' % (str(item)))
    if not re.match('^[a-z]+$', str(item), re.I):
        log.warning('Validating failed')
        return False

    log.debug('Validate successful')
    return str(item)

def integer(item):
    log.debug('Validating as integer: %s' % (str(item)))
    if not re.match('^[0-9]+$', str(item)):
        log.warning('Validating failed')
        return False

    log.debug('Validate successful')
    return int(item)

def uri(item):
    log.debug('Validating as uri: %s' % (str(item)))
    if not (re.match('^[a-z]+$', str(item), re.I) or
       re.match('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', str(item))):
        log.warning('Validating failed')
        return False

    log.debug('Validate successful')
    return str(item)

def target(item):
    log.debug('Validating as uri: %s' % (str(item)))
    try:
        ipaddress.ip_network(str(item))
    except Exception as e:
        log.warning('Validating failed')
        return False
    log.debug('Validate successful')
    return str(item)

def ip(item):
    log.debug('Validating as IP: %s' % (str(item)))
    if not re.match('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', str(item)):
        log.warning('Validating failed')
        return False

    log.debug('Validate successful')
    return str(item)

def username(item):
    log.debug('Validating as string: %s' % (str(item)))
    if not re.match('^[a-z_]+$', str(item), re.I):
        log.warning('Validating failed')
        return False

    log.debug('Validate successful')
    return str(item)
