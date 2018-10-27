from configparser import ConfigParser
from socket import inet_aton
from re import sub
from sys import exit

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

    config = {}

    config_keys = [
        'targets'
    ]
    config_file = ConfigParser()
    config_file.read('config.ini')

    if 'DEFAULT' not in config_file:
        print("[!] Failed to read configuration!")
        exit(1) 
        
    # Dynamically read configuration, parse and validate them
    for key in config_keys:
        if key in config_file['DEFAULT']:
            parse = globals()['parse_%s' % (key)]
            validate = globals()['validate_%s' % (key)]
            tmp_conf = parse(config_file['DEFAULT'][key])
            config[key] = validate(tmp_conf)


    return config

def default_config():
    '''
    Return default configuration.
    '''
    return {
        'queue': 'local'
        }

def parse_targets(targets):
    '''
    Parse and format the list of targets.
    '''
    targets = sub(r'[^0-9./\n]', "", targets)
    return list(filter(None, targets.split('\n')))

def validate_targets(targets):
    '''
    Validate the list of targets
    '''
    for target in targets:
        t = target.split('/')
        if len(t) == 2:
            t[1] = int(t[1])

        if not t or len(t) > 2:
            #print("[!] Invalid target specified: %s" % (target))
            raise ValueError("Invalid target specified: %s" % (target))

        if (not inet_aton(t[0])) or (len(t) == 2 and (t[1] < 8 or t[1] > 32)):
            #print("[!] Invalid target specified: %s" % (target))
            raise ValueError("Invalid target specified: %s" % (target))

    return targets
