# 📸 LensPrint

**LensPrint** is a Python-based tool that transforms your photos into beautiful, editorial-style visuals by adding soft blurred borders and embedding camera shooting parameters (EXIF data) into the final image. Inspired by mobile apps like 光影边框, this tool is perfect for photographers who want to stylize their work for social media, blogs, or portfolios.

---

## ✨ Features

- ✅ Add a soft blurred border around your image
- ✅ Rounded corners for a clean, modern aesthetic
- ✅ Auto-extract and overlay EXIF metadata (camera, lens, shutter speed, ISO, etc.)
- ✅ Customize text font, size, and position
- ✅ High-resolution output suitable for sharing or printing

---

## 📦 Installation

```bash
pip install pillow opencv-python piexif
```

---

## 🚀 Usage

```python
from lensprint import create_blurred_frame_with_text

exif_data = {
    "brand": "Nikon",
    "model": "NIKON Z 30",
    "settings": "345mm  F6  1/500s  ISO100"
}

input_image = "your_photo.jpg"
output_image = "framed_output.jpg"

create_blurred_frame_with_text(input_image, output_image, exif_data)
```

Or use the provided command-line interface (coming soon!).

---

## 🧪 Sample Output

![example](./example_output.jpg)

---

## 🛠 Technologies Used

- [Pillow](https://python-pillow.org/)
- [piexif](https://pypi.org/project/piexif/)
- [OpenCV](https://opencv.org/)

---

## 🖼 License

MIT License © 2025 [Yuan Chen](https://github.com/chenyuan99)

---

## 💬 Acknowledgements

- Inspired by the mobile app “光影边框”
- Developed with ❤️ for photography lovers

---