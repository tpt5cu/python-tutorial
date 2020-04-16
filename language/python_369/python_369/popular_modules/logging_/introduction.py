# https://docs.python.org/3.6/library/logging.html

import logging

'''
The default logging levels and their associated integer representations are:
- CRITICAL 50
- ERROR 40
- WARNING 30 
- INFO 20
- DEBUG 10
- NOTSET 0
'''

def create_custom_logger():
    '''A logger will ignore any message below its specified logging level'''
    logger = logging.getLogger(__name__)
    logger.setLevel(50)
    logger.debug('Ignore debug')
    logger.info('Ignore info')
    logger.warning('Ignore warning')
    logger.error('Ignore error')
    logger.critical('CRITICAL FAILURE') # CRITICAL FAILURE


if __name__ ==  '__main__':
    create_custom_logger()