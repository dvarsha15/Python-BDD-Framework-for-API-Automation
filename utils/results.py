#create methods to display results using loguru library
from loguru import logger

def success(msg):
    logger.success(msg)

def error(msg):
    logger.error(msg)

def info(msg):
    logger.info(msg)