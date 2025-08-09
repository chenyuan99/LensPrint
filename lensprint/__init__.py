import piexif
from PIL import Image, ImageDraw, ImageFilter, ImageFont


def add_blur_border(
    image_path, output_path="output.jpg", blur_radius=30, border_size=50
):
    image = Image.open(image_path)
    width, height = image.size
    new_width = width + 2 * border_size
    new_height = height + 2 * border_size
    background = image.filter(ImageFilter.GaussianBlur(blur_radius)).resize(
        (new_width, new_height)
    )
    background.paste(image, (border_size, border_size))
    background.save(output_path)
    return output_path


def extract_exif_info(image_path):
    exif_dict = piexif.load(image_path)
    info = {}
    try:
        info["品牌"] = exif_dict["0th"][piexif.ImageIFD.Make].decode()
    except Exception:
        pass
    try:
        info["型号"] = exif_dict["0th"][piexif.ImageIFD.Model].decode()
    except Exception:
        pass
    try:
        lens = exif_dict["Exif"][piexif.ExifIFD.LensModel].decode()
        info["镜头"] = lens
    except Exception:
        pass
    try:
        focal = exif_dict["Exif"][piexif.ExifIFD.FocalLength]
        info["焦距"] = f"{focal[0] // focal[1]}mm"
    except Exception:
        pass
    try:
        fnum = exif_dict["Exif"][piexif.ExifIFD.FNumber]
        info["光圈"] = f"F{fnum[0] / fnum[1]:.1f}"
    except Exception:
        pass
    try:
        exp = exif_dict["Exif"][piexif.ExifIFD.ExposureTime]
        info["快门"] = f"1/{int(1 / exp[0] * exp[1])}s" if exp[0] != 0 else f"{exp[1]}s"
    except Exception:
        pass
    try:
        iso = exif_dict["Exif"][piexif.ExifIFD.ISOSpeedRatings]
        info["ISO"] = f"ISO {iso}"
    except Exception:
        pass
    return info


def overlay_exif_text(image_path, exif_info, output_path="final.jpg"):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 300)
    except Exception:
        font = ImageFont.load_default()
    text = " | ".join([f"{k}:{v}" for k, v in exif_info.items()])
    draw.text((10, 10), text, font=font, fill="white")
    image.save(output_path)
    print(f"最终图像保存: {output_path}")


# Convenience function for users


def create_blurred_frame_with_text(input_image, output_image, exif_data=None):
    temp_blur = add_blur_border(input_image)
    if exif_data is None:
        exif_data = extract_exif_info(input_image)
    overlay_exif_text(temp_blur, exif_data, output_image)
