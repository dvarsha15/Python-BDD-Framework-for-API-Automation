#configurations (taken from properties.ini)
import configparser

def getconfig():
    config = configparser.ConfigParser()
    config.read('conf\properties.ini')
    return config
