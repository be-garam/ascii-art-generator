# main.py
from ascii_converter import ImageToASCII, ASCIIFormatter
from ascii_converter.utils import get_file_extension, save_to_file, save_colored_to_file
import sys
import os

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_image> [output_file]")
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

    # 출력 디렉토리 확인 및 생성
    output_dir = "outputs"
    ensure_dir(output_dir)

    # 출력 파일 저장 로직
    if len(sys.argv) > 2:
        output_filename = sys.argv[2]
        base_name, ext = os.path.splitext(output_filename)
    else:
        # 기본 출력 파일명 생성
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        ext = ".txt"

    output_path = os.path.join(output_dir, f"{base_name}_ascii{ext}")
    color_output_path = os.path.join(output_dir, f"{base_name}_ascii_color{ext}")

    save_to_file(bordered_art, output_path)  # 색상 없는 버전을 저장
    save_colored_to_file(colored_art, color_output_path)  # 색상 있는 버전을 저장

if __name__ == "__main__":
    main()