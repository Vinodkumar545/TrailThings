import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('Start reading database')

# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records.keys())
logger.info('Updating records ...', records)

# update records here
logger.info('Finish updating records')
