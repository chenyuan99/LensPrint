"""Basic tests for lensprint package."""

import pytest

from lensprint import create_blurred_frame_with_text, extract_exif_info


def test_imports():
    """Test that main functions can be imported."""
    assert callable(create_blurred_frame_with_text)
    assert callable(extract_exif_info)


def test_extract_exif_info_with_invalid_path():
    """Test extract_exif_info with non-existent file."""
    with pytest.raises((FileNotFoundError, OSError)):
        extract_exif_info("nonexistent.jpg")


def test_create_blurred_frame_with_text_with_invalid_path():
    """Test create_blurred_frame_with_text with non-existent file."""
    with pytest.raises((FileNotFoundError, OSError)):
        create_blurred_frame_with_text("nonexistent.jpg", "output.jpg")
