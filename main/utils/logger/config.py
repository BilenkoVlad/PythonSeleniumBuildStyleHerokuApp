import logging
import logging.config
import os

import yaml


def configure_logger():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{path}/config.yaml', 'r') as f:
        log_cfg = yaml.safe_load(f.read())

    logging.config.dictConfig(log_cfg)
