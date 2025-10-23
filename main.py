from src.data_science_project import logger 
logger.info("Welcom to our custom data science projct")

import os
import yaml
import urllib.request
import zipfile
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: str
    unzip_dir: str


class ConfigurationManager:
    def __init__(self, config_filepath="config.yaml"):
        with open(config_filepath) as yaml_file:
            self.config = yaml.safe_load(yaml_file)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']
        os.makedirs(config['root_dir'], exist_ok=True)
        return DataIngestionConfig(
            root_dir=config['root_dir'],
            source_URL=config['source_URL'],
            local_data_file=config['local_data_file'],
            unzip_dir=config['unzip_dir']
        )


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            urllib.request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            print("✅ File downloaded successfully!")
        else:
            print("⚠️ File already exists.")

    def extract_zip_file(self):
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        print("✅ Files extracted successfully!")


# Run
try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()

except Exception as e:
    raise e
