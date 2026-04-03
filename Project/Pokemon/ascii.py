from PIL import Image
import os

def image_to_ascii(name, new_width=25, invert=True):
    image_path = os.path.join(os.path.dirname(__file__), 'ascii', f'{name}.png')
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"이미지를 열 수 없습니다: {e}")
        return

    # 1. 크기 조정
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.5)
    image = image.resize((new_width, new_height))

    # 2. 흑백 이미지로 변환
    image = image.convert("L")

    # 3. 아스키 문자 매핑
    # 기본: 어두운 곳 -> 밝은 곳 순서
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    
    # invert가 True이면 리스트를 뒤집습니다.
    if invert:
        chars = chars[::-1]

    pixels = image.getdata()
    
    ascii_str = ""
    for i, pixel in enumerate(pixels):
        # 0~255 값을 0~10 인덱스로 변환 (255/11은 약 23)
        # 픽셀 값이 작으면(어두우면) 리스트 앞쪽 문자 사용
        ascii_str += chars[min(pixel // 23, len(chars)-1)]
        if (i + 1) % new_width == 0:
            ascii_str += "\n"

    print(ascii_str)

