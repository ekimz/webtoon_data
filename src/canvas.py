from configparser import ConfigParser
import pandas as pd
import requests
import json

# access
config = ConfigParser()
config.read('config.ini')
api_host = config.get('api', 'host')
api_key = config.get('api', 'key')


