from socket import inet_aton

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

def validate_db(db):
    return db

def validate_mongodb_uri(mongodb_uri):
    return mongodb_uri
def validate_mongodb_port(mongodb_port):
    return mongodb_port
def validate_mongodb_user(mongodb_user):
    return mongodb_user