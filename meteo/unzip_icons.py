import zipfile
import os

zip_file_path = 'icons/icons_ipma_weather.zip'

extract_to_path = 'static/meteo'

os.makedirs(extract_to_path, exist_ok=True)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)
