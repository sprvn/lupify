from sys import exit
import nmap
import logging
import helpers.validators as validators

log = logging.getLogger(__name__)

class scanner():
    def __init__(self, options):
        self.options = options
        if not self.options:
            log.critical('No scans to run')
            exit(1)
        try:
            self.nm = nmap.PortScanner()
            log.debug('Initialized NMAP scanner')
        except Exception as e:
            log.critical('Failed to create NMAP scanner')

        self._check_options()

    def scan_target(self):
        print(options)
        pass
    
    def insert_result(self):
        pass
    
    def parse_result(self):
        pass

    def _check_options(self):
        log.debug('Verifying required fields in options exists')
        for option in ['target', 'interval']:
            log.debug('Verifying {}'.format(option))
            if (option not in self.options or
                not self.options[option]):
                log.error('{} not specified in scan'.format(option))
                exit(1)
        log.debug('Required fields in options exists')

        log.debug('Validating options')
        if not validators.target(self.options['target']):
            log.error('Invalid target specified: {}'.format(self.options['target']))
        if not validators.integer(self.options['interval']):
            log.error('Invalid interval specified: {}'.format(self.options['interval']))
