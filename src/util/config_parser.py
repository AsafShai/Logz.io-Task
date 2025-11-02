import json

class ConfigParser:
    def __init__(self, config_file):
        self.data_sources = []
        self.logz_io = {}
        self.polling_interval = 60

        self.parse_config(config_file)

    def parse_config(self, config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
        self.data_sources = config['data_sources']
        self.logz_io = config['logz_io']
        self.polling_interval = config['polling_interval']
        # TODO: handle errors and missing keys or values, including type errors (for example, data_sources missing or not a list or wrong type)

    def get_data_sources(self):
        return self.data_sources

    def get_logz_io(self):
        return self.logz_io

    def get_polling_interval(self):
        return self.polling_interval