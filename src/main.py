from pathlib import Path
import os
from dotenv import load_dotenv

from utils.extract_table import download_table
from utils.look_path import manipulacao_path, remove_files
from utils.compress_csv import compress_table
from utils.append_sql import save_sql

load_dotenv()

path_data = Path(os.getenv("PATH_DATA"))
path_download = Path(os.getenv("PATH_DOWNLOAD"))

download_table()
manipulacao_path()
remove_files()
compress_table(path_data)

data = os.getenv("FILE")

# save_sql(data)
