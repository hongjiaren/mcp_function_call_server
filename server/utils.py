import logging
import yaml

def load_config(config_file="config/config.yaml"):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config

def setup_logging(log_config_file="config/logging_config.yaml"):
    with open(log_config_file, "r") as file:
        log_config = yaml.safe_load(file)
    logging.config.dictConfig(log_config)
