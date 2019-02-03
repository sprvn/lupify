from helpers.config import read_configuration
from models.queue import Queue
import helpers.parsers as helpers
import helpers.logger
import helpers.database
import logging


def main():
    log = logging.getLogger(__name__)

    log.info('Reading configuration')
    config = read_configuration()
    if 'config_level' in config:
        helpers.logger.configure(config['config_level'])
        log.info('Updated logging configuration')
    helpers.database.connect(config)


if __name__ == '__main__':
    main()

