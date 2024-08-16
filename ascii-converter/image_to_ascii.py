import PIL.Image
import numpy as np

class ImageToASCII:
    def __init__(self, path):
        self.image = PIL.Image.open(path)
    
    def convert(self, width=100, height=None):
        # 이미지를 흑백으로 변환
        image = self.image.convert('L')
        
        # 높이가 지정되지 않은 경우, 원본 비율 유지
        if height is None:
            aspect_ratio = image.height / image.width
            height = int(width * aspect_ratio)
        
        # 이미지 크기 조정
        image = image.resize((width, height))
        
        # 픽셀 데이터를 numpy 배열로 변환
        pixels = np.array(image)
        
        # ASCII 문자 리스트 (밝기에 따라 정렬)
        ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
        
        # 픽셀 값을 ASCII 문자로 변환
        ascii_str = ''
        for row in pixels:
            for pixel in row:
                ascii_str += ascii_chars[int(pixel / 25)]
            ascii_str += '\n'
        
        return ascii_str

