"""This module is used as proof & practice of logging in python"""

import logging

def log_output_to_console():
    """logs output to the console"""

    logging.debug('level 0 debug message')
    logging.info('level 1 info message')
    logging.warning('level 2 warning message')
    logging.error('level 3 error message')
    logging.critical('level 4 critical message')

def log_output_to_file():
    """log the logging output to a file"""

    # By default the logging output level is set to "warning".

    logging.basicConfig(level='DEBUG', filename='output.log')
    logging.debug("outputs DEBUG:root:debug message")

    # Assign the logger to an object and use to output logging
    # statements.
    logger = logging.getLogger('root')
    logger.info("This is an INFO message.")

if __name__ == '__main__':
    # The following functions are mutually exclusive.
    # Uncomment to test output to console.
    # log_output_to_console()

    # Uncomment to test output to a logging file.
    log_output_to_file()
