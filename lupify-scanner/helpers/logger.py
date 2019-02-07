import logging
import sys
    
log = logging.getLogger(__name__)

logging.basicConfig(format='%(asctime)-15s [%(levelname)s] %(message)s',
                    stream=sys.stdout,
                    level=logging.INFO)

log.info('Configured basic logging')

def configure(level='warning',
              format='%(asctime)-15s [%(levelname)s] %(message)s'):

    level_label = level

    if level == 'debug':
        level = logging.DEBUG
    elif level == 'info':
        level = logging.INFO
    elif level == 'warning':
        level = logging.WARNING
    elif level == 'critical':
        level = logging.CRITICAL
    else:
        level = logging.WARNING

    log.info('Configured logging level to %s' % (level_label))

    # Remove default configuration
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Reconfigure logging again, this time user defined config
    logging.basicConfig(format=format,
                        stream=sys.stdout,
                        level=level)
