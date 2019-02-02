import helpers.validators as validators
from netaddr import IPNetwork
from re import sub, split
from socket import inet_aton

def parse_targets(targets):
    '''
    Parse and format the list of targets.
    '''
    targets = sub(r'[^0-9./\n]', "", targets)
    return list(filter(None, targets.split('\n')))

def parse_db(db):
    return db