import helpers.validators as validators
from netaddr import IPNetwork
from re import sub, split
from socket import inet_aton

def _convert_ip_gen_to_list(generator):
    return list((str(item) for item in generator))

def target_list(targets):
    validators.validate_targets(targets)
    target_list = set([])
    for target in targets:
        target = normalize_target(target)
        t = target.split('/')
        if len(t) != 2:
            raise ValueError
        if int(t[1]) > 24 and int(t[1]) < 33:
            target_list = [*target_list, *[target]]
        else:
            ip_generator = IPNetwork(target).subnet(24)
            target_list = list(
                set(
                    [
                        *target_list, 
                        *_convert_ip_gen_to_list(ip_generator)
                    ]
                ))
    
    return sorted(target_list, key=lambda item: split('/|\.', item))

def parse_targets(targets):
    '''
    Parse and format the list of targets.
    '''
    targets = sub(r'[^0-9./\n]', "", targets)
    return list(filter(None, targets.split('\n')))

def normalize_target(target):
    '''
    Normalize the format of a target.
    '''
    t = target.split('/')
    if len(t) == 1:
        target = target + '/32'
    return target