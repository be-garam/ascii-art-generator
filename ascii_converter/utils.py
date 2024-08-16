import os

def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower()