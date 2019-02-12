from helpers.config import read_configuration
from models.queue import Queue
from models.scheduler import Scheduler
from models.scanner import scanner
import helpers.parsers as helpers
import helpers.logger
import helpers.database
import logging

log = logging.getLogger(__name__)

def main():

    log.info('Reading configuration')
    config = read_configuration()

    if 'config_level' in config:
        helpers.logger.configure(config['config_level'])
        log.info('Updated logging configuration')

    db = helpers.database.connect(config)
    #print(db.scans.find_one({'target': '192.168.0.0/24'}))

    s = Scheduler(db)
    scans = s.checkConfiguredScans()
    scanner(db,
        {
            '_id': '123345-345-345-345',
            'target': '192.168.1.16/28', 
            'interval': 60, 
            'arguments':[
                '-sV'
            ]
        })


if __name__ == '__main__':
    main()

