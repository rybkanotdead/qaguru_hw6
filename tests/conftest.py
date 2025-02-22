from zipfile import ZipFile
import os
import pytest

current_file = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file)
current_project_path = os.path.dirname(current_directory)
tmp_file_path = os.path.join(current_project_path,"tmp")
arhive_path = os.path.join(tmp_file_path, "archive_files.zip")

@pytest.fixture(scope='function',autouse=True)
def create_zip():
    with ZipFile(arhive_path, 'w') as zip_file:
        for file in os.listdir(tmp_file_path):
            zip_file.write(os.path.join(tmp_file_path,file), file)