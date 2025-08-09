# Technology Stack & Build System

## Core Dependencies
- **Pillow (PIL)**: Primary image processing library for filters, drawing, and manipulation
- **OpenCV (cv2)**: Computer vision operations and advanced image processing
- **piexif**: EXIF metadata extraction and manipulation
- **NumPy**: Array operations (via OpenCV dependency)

## Build System
- **Build Backend**: setuptools with pyproject.toml configuration
- **Python Version**: >=3.7 required
- **Package Manager**: pip for dependency installation

## Common Commands

### Development Setup
```bash
# Install dependencies
pip install pillow opencv-python piexif

# Install from requirements
pip install -r requirements.txt

# Install development dependencies (includes ruff linter)
pip install -e ".[dev]"

# Build package
python -m build
```

### Code Quality
```bash
# Run linter
ruff check .

# Auto-fix linting issues
ruff check --fix .

# Format code
ruff format .
```

### Testing & Usage
```bash
# Run tests
pytest tests/ -v

# Run example usage
python example_usage.py

# Run main script directly
python lensprint/main.py
```

## CI/CD Pipeline

### GitHub Workflows
- **CI Pipeline** (`.github/workflows/ci.yml`): Runs on push/PR to main/develop
  - Tests multiple Python versions (3.8-3.12)
  - Runs linting with ruff
  - Checks code formatting
  - Runs test suite with pytest
  - Builds package artifacts

- **Release Pipeline** (`.github/workflows/release.yml`): Runs on version tags
  - Builds package for distribution
  - Creates GitHub releases with artifacts
  - Publishes to PyPI (when configured)

## Code Style Conventions
- **Linting**: Uses Ruff for code quality and formatting
- **Line Length**: 88 characters maximum
- **Imports**: Organized and sorted automatically
- **Exception Handling**: Use `except Exception:` instead of bare `except:`
- Mixed language comments (Chinese and English) - preserve existing style
- Function names use snake_case
- Image processing functions return file paths for chaining
- Default parameter values provided for common use cases
- Error handling with try/except blocks for EXIF parsing

## Architecture Notes
- Modular design with separate functions for blur, EXIF extraction, and text overlay
- Main convenience function `create_blurred_frame_with_text()` chains operations
- Font fallback to system default when custom fonts unavailable