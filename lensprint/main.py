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
    background = image.resize(new_size).filter(
        ImageFilter.GaussianBlur(blur_radius))

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
    except:
        pass

    try:
        exposure = exif_dict['Exif'][piexif.ExifIFD.ExposureTime]
        info['快门'] = f"{exposure[0]}/{exposure[1]} 秒"
    except:
        pass

    try:
        fnum = exif_dict['Exif'][piexif.ExifIFD.FNumber]
        info['光圈'] = f"f/{round(fnum[0]/fnum[1], 1)}"
    except:
        pass

    try:
        iso = exif_dict['Exif'][piexif.ExifIFD.ISOSpeedRatings]
        info['ISO'] = f"ISO {iso}"
    except:
        pass

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

# Step 1: Add rounded rectangle background blur (mimic style)


def create_blurred_frame_with_text(image_path, output_path, exif_text, border_radius=60, border_size=100, blur_amount=25):
    # Load the original image
    image = Image.open(image_path).convert("RGB")
    width, height = image.size

    # Create a larger blurred background
    new_width = width + 2 * border_size
    new_height = height + 2 * border_size
    resized = image.resize((new_width, new_height))
    blurred_background = resized.filter(ImageFilter.GaussianBlur(blur_amount))

    # Create mask for rounded rectangle
    mask = Image.new("L", (new_width, new_height), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle(
        (0, 0, new_width, new_height), radius=border_radius, fill=255)

    # Composite the blurred image with rounded corners
    rounded_bg = Image.new("RGB", (new_width, new_height))
    rounded_bg.paste(blurred_background, mask=mask)

    # Paste the original image in center
    rounded_bg.paste(image, (border_size, border_size))

    # Draw EXIF text at the bottom
    draw = ImageDraw.Draw(rounded_bg)
    try:
        font_bold = ImageFont.truetype("arialbd.ttf", 28)
        font_regular = ImageFont.truetype("arial.ttf", 24)
    except:
        font_bold = font_regular = ImageFont.load_default()

    # Format: Bold brand + regular text
    brand_text = exif_text.get("brand", "Nikon")
    model_text = exif_text.get("model", "NIKON Z 30")
    settings_text = exif_text.get("settings", "345mm  F6  1/500s  ISO100")

    # Center alignment
    text_margin = 20
    brand_bbox = draw.textbbox((0, 0), brand_text, font=font_bold)
    brand_size = (brand_bbox[2] - brand_bbox[0], brand_bbox[3] - brand_bbox[1])
    model_bbox = draw.textbbox((0, 0), model_text, font=font_regular)
    model_size = (model_bbox[2] - model_bbox[0], model_bbox[3] - model_bbox[1])
    settings_bbox = draw.textbbox((0, 0), settings_text, font=font_regular)
    settings_size = (settings_bbox[2] - settings_bbox[0],
                     settings_bbox[3] - settings_bbox[1])

    center_x = new_width // 2
    base_y = new_height - settings_size[1] - 30

    draw.text((center_x - brand_size[0] // 2, base_y - 40),
              brand_text, font=font_bold, fill="white")
    draw.text((center_x - model_size[0] // 2, base_y - 10),
              model_text, font=font_regular, fill="white")
    draw.text((center_x - settings_size[0] // 2, base_y + 20),
              settings_text, font=font_regular, fill="white")

    # Save the result
    rounded_bg.save(output_path)
    return output_path


# === 示例使用 ===
image_file = 'sample.JPG'  # 替换为你的图片路径
output_file = 'output.jpg'
exif_data = extract_exif_info(image_file)
blurred = add_blur_border(image_file)
exif = extract_exif_info(image_file)
overlay_exif_text(blurred, exif)
create_blurred_frame_with_text(image_file, output_file, exif_data)
