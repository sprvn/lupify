import logging
import sys

logging.basicConfig(format='%(asctime)-15s [%(levelname)s] %(message)s',
                    stream=sys.stdout,
                    level=logging.INFO)
