from sys import exit
import nmap
import logging
import helpers.validators as validators
import helpers.functions as functions

log = logging.getLogger(__name__)

class scanner():
    def __init__(self, db, options):
        self.db = db
        self.options = options
        self.nm = nmap.PortScanner()
        if not self.options:
            log.critical('No scans to run')
            exit(1)
        try:
            self.nm = nmap.PortScanner()
            log.debug('Initialized NMAP scanner')
        except Exception as e:
            log.critical('Failed to create NMAP scanner')

        if not self._check_options():
            log.error('Option check failed. Exiting scan')
            exit(1)
        self.scan_target()
        result = self.parse_result()
        log.debug('Fetching current time')
        time = 0
        try:
            time = functions.getEpochSeconds()
        except Exception as e:
            log.error('Failed to fetch current time: {}'.format(e))
        #result.update({
        #    'scan_id': self.options['_id'],
        #    'time': time
        #})
        #print(result)
        scan_result = {
            'scan_id': self.options['_id'],
            'time': time,
            'result': result
        }
        try:
            db.scan_results.insert_one(scan_result)
        except Exception as e:
            log.error('Failed to insert scan results into DB: {}'.format(e))

    def scan_target(self):
        log.info('Scanning {}'.format(self.options['target']))
        try:
            self.nm.scan(
                hosts=self.options['target'],
                arguments=' '.join(self.options['arguments']))
        except Exception as e:
            log.error('Failed to scan {}: {}'.format(self.options['target'], e))
        log.debug('Scanning of {} complete'.format(self.options['target']))
    
    def insert_result(self):
        pass
    
    def parse_result(self):
        result = []
        log.debug('Parsing hosts from scan result')
        for host in self.nm.all_hosts():
            host_result = {}
            tcp_ports = None
            udp_ports = None
            log.debug('Parsing {}'.format(host))
            log.debug('Saving first hostname out of: {}'.format(self.nm[host]['hostnames']))
            hostname = self.nm[host]['hostnames'][0]['name']
            log.debug('Saving state')
            state = self.nm[host]['status']['state']
            host_result.update({
                'ipaddress': host,
                'hostname': hostname,
                'state': state,
            })
            if 'tcp' in self.nm[host] and self.nm[host]['tcp']:
                log.debug('Extracting found TCP ports')
                tcp_ports = self._parse_ports(self.nm[host]['tcp'])
                host_result.update({'tcp': tcp_ports})
            if 'udp' in self.nm[host] and self.nm[host]['udp']:
                log.debug('Extracting found UDP ports')
                udp_ports = self._parse_ports(self.nm[host]['udp'])
                host_result.update({'udp': udp_ports})

            result.append(host_result)

        log.debug('Finished parsing result from scan')
        return result

    def _parse_ports(self, ports):
        result = {}
        for k,v in ports.items():
            result.update({str(k):{
                'name': v['name'],
                'product': v['product'],
                'version': v['version'],
            }})
        return result

    def _check_options(self):
        log.debug('Verifying required fields in options exists')
        for option in ['target', 'interval', 'arguments']:
            log.debug('Verifying {}'.format(option))
            if (option not in self.options or
                not self.options[option]):
                log.error('{} not specified in scan'.format(option))
                exit(1)
        log.debug('Required fields in options exists')

        log.debug('Validating options')
        if not validators.target(self.options['target']):
            log.error('Invalid target specified: {}'.format(self.options['target']))
            return False
        if not validators.integer(self.options['interval']):
            log.error('Invalid interval specified: {}'.format(self.options['interval']))
            return False
        if not validators.nmap_args(self.options['arguments']):
            log.error('Invalid argument specified: {}'.format(self.options['arguments']))
            return False

        return True
