# ascii_converter/utils.py
import os

def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower()

def save_to_file(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"ASCII art saved to {output_path}")