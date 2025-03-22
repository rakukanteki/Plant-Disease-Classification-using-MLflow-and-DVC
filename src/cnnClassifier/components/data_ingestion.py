import zipfile
import gdown
from src.cnnClassifier import logger
from src.cnnClassifier.utils.common import get_size
import os
from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """Fetch Data from URL"""
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)

            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]  # Extracting file ID
            gdown.download(f"https://drive.google.com/uc?id={file_id}", zip_download_dir, quiet=False, use_cookies=True)

            # Verify the downloaded file
            if not zipfile.is_zipfile(zip_download_dir):
                raise ValueError("Downloaded file is not a valid ZIP file. Please check the Google Drive link.")

        except Exception as e:
            logger.error(f"Error downloading file: {e}")
            raise e

        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)