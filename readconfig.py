import sys, os
import yaml 


class ReadConfig:
    def __init__(self, configFile='dbconfig.yml'):
        with open(configFile, 'r') as ymlfile:
            self._cfg = yaml.load(ymlfile)
    def getConfig(self):
        return self._cfg
