from PIL import Image, ImageFilter, ImageDraw, ImageFont
import piexif
import cv2
import numpy as np
import os

def add_blur_border(image_path, output_path='output.jpg', blur_radius=30, border_size=50):
    # 读取图片
    image = Image.open(image_path).convert("RGB")
    width, height = image.size

    # 扩展画布
    new_size = (width + 2*border_size, height + 2*border_size)
    background = image.resize(new_size).filter(ImageFilter.GaussianBlur(blur_radius))

    # 粘贴原图在中间
    background.paste(image, (border_size, border_size))

    # 保存
    background.save(output_path)
    print(f"模糊边框图已保存: {output_path}")
    return output_path

def extract_exif_info(image_path):
    exif_dict = piexif.load(image_path)
    info = {}

    try:
        info['相机型号'] = exif_dict['0th'][piexif.ImageIFD.Model].decode()
    except: pass

    try:
        exposure = exif_dict['Exif'][piexif.ExifIFD.ExposureTime]
        info['快门'] = f"{exposure[0]}/{exposure[1]} 秒"
    except: pass

    try:
        fnum = exif_dict['Exif'][piexif.ExifIFD.FNumber]
        info['光圈'] = f"f/{round(fnum[0]/fnum[1], 1)}"
    except: pass

    try:
        iso = exif_dict['Exif'][piexif.ExifIFD.ISOSpeedRatings]
        info['ISO'] = f"ISO {iso}"
    except: pass

    print("📸 拍摄参数:")
    for k, v in info.items():
        print(f"{k}: {v}")

    return info

def overlay_exif_text(image_path, exif_info, output_path='final.jpg'):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 300)
    except:
        font = ImageFont.load_default()

    text = " | ".join([f"{k}:{v}" for k, v in exif_info.items()])
    draw.text((10, 10), text, font=font, fill="white")

    image.save(output_path)
    print(f"最终图像保存: {output_path}")


# === 示例使用 ===
image_file = 'sample.JPG'  # 替换为你的图片路径
blurred = add_blur_border(image_file)
exif = extract_exif_info(image_file)
overlay_exif_text(blurred, exif)
