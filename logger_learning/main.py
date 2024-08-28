import logging.config
import yaml

from logger_learning.module_1 import main

with open('logger_learning/logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

main()