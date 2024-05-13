import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import CreateTable

from sqlalchemy.orm import *
from sqlalchemy.orm import *

def init_db(file_path: str, create_ddl: booö = False, generate_example_data: bool = False):
    path = Path(file_path)
    data_folder = path.parent
    engine = create_engine(f"sqlite:///{file_path}")

    if path.is_file():
        Base.metadata.drop_all(engine)

