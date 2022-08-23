#generate results using loguru library
from loguru import logger

def success(msg):
    logger.remove(0)
    logger.success(msg)

def error(msg):
    logger.remove(0)
    logger.error(msg)

def info(msg):
    logger.remove(0)
    logger.info(msg)