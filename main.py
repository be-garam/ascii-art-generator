from ascii_converter import ImageToASCII, ASCIIFormatter
from ascii_converter.utils import get_file_extension
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    extension = get_file_extension(image_path)

    if extension not in ['.svg', '.png']:
        print("Error: Only SVG and PNG files are supported.")
        sys.exit(1)

    converter = ImageToASCII(image_path)
    ascii_art = converter.convert()
    
    formatter = ASCIIFormatter()
    bordered_art = formatter.add_border(ascii_art)
    colored_art = formatter.colorize(bordered_art)
    
    print(colored_art)

if __name__ == "__main__":
    main()
