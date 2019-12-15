from yaml_parser import ConfigManger
from pprint import pprint
config = ConfigManger(DEFAULT_CONFIG_PATH="base_config.yaml",verbose=False, integrality_check=False).config
pprint(config)