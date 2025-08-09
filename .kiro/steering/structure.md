# Project Structure & Organization

## Root Directory Layout
```
lensprint/
├── lensprint/           # Main package directory
│   ├── __init__.py      # Core functions and public API
│   └── config.py        # Configuration (currently empty)
├── main.py              # Standalone script with all functions
├── example_usage.py     # Usage examples and demos
├── pyproject.toml       # Package configuration and dependencies
├── requirements.txt     # Pip dependencies list
├── README.md           # Project documentation
├── LICENSE             # MIT license
├── sample.JPG          # Test image for development
├── output.jpg          # Generated output examples
├── final.jpg           # Final processed images
└── dist/               # Built package artifacts
```

## Code Organization Patterns

### Main Package (`lensprint/`)
- `__init__.py`: Contains all core image processing functions
- Public API functions: `create_blurred_frame_with_text()`, `extract_exif_info()`, `add_blur_border()`
- Internal utilities: `overlay_exif_text()`

### Development Files
- `main.py`: Development script with duplicate functions (legacy)
- `example_usage.py`: Simple usage demonstrations
- Sample images: `sample.JPG`, `output.jpg`, `final.jpg`

## File Naming Conventions
- Snake_case for Python files and functions
- Descriptive output filenames: `output.jpg`, `final.jpg`
- Test images use original extensions: `.JPG`, `.jpg`

## Import Structure
```python
from lensprint import create_blurred_frame_with_text, extract_exif_info
```

## Notes
- Code duplication exists between `main.py` and `lensprint/__init__.py`
- `config.py` is placeholder for future configuration options
- Built package stored in `dist/` directory
- EXIF metadata preserved in Chinese variable names in some functions