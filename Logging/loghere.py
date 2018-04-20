import logging
# import Logging.log_setup as log_setup
# format_text = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=format_text, filename='myapp.log', level=logging.INFO)
# logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
# logging.info('START')
# log_setup.do_something()
# log_setup.debug(10, 0)
# log_setup.debug(10, 1)
# logging.info('END')

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')


def log_debug(message):
    logger.debug(message)


def log_info(message):
    logger.info(message)


def log_error(message):
    logger.error(message)
