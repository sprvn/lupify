import sched
import time
import logging
import helpers.validators as validators

log = logging.getLogger(__name__)

class Scheduler():
    def __init__(self, db):
        self._schedule = sched.scheduler(time.time, time.sleep)
        self.db = db

    def checkConfiguredScans(self):
        log.debug('Checking scheduled scans')
        scans = self._getScans()
        return self._getScansToSchedule(scans)

    def _getScans(self):
        log.debug('Fetching all scans')
        result = []
        try:
            result = list(self.db.scans.find())
            log.debug('Fetched scans successfully')
        except Exception as e:
            log.error('Failed to fetch scans: %s' % (e))
        if len(result) > 0:
            log.debug('Scans fetched: %s' % (result))
        else:
            log.info('No scans found')

        return result

    def _getScansToSchedule(self, scans):
        result = []

        for scan in scans:
            if not validators.integer(str(scan['interval'])):
                log.error('Scan interval invalid format: {}'.format(
                    str(scan['interval'])))
                continue

            try:
                epoch_seconds = str(time.time()).split('.')[0]
                log.debug('Current epoch: {}'.format(epoch_seconds))
            except Exception as e:
                log.error('Failed to get time: {}'.format(e))
                continue

            interval_seconds = 60 * int(scan['interval'])
            log.debug('Scan interval in seconds: {}'.format(interval_seconds))
            interval = int(epoch_seconds) % interval_seconds
            log.debug('Interval: {}'.format(interval))
            if interval < 60:
                log.debug('Adding scan to be scheduled')
                result.append(scan)

        return result

    def _scheduleScans(self):
        pass

    def run(self):
        self._schedule.run()
