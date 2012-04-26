import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(threadName)s [%(levelname)s] %(message)s")

from . import config 

# load config
if len(sys.argv) > 1:
    config.load(sys.argv[1])
    
# Make sure the storage directory exists
if not os.path.exists(config.storage['directory']):
    os.makedirs(config.storage['directory'])

from . import webapp

# Intialize
webapp.setup()

application = webapp.application

