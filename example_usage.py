from lensprint import create_blurred_frame_with_text, extract_exif_info

image_file = 'sample.JPG'  # Replace with your image path
blurred = 'output.jpg'
final = 'final.jpg'

# Add blurred border
temp_blur = create_blurred_frame_with_text(image_file, final)

# Or, for more control:
# exif = extract_exif_info(image_file)
# create_blurred_frame_with_text(image_file, final, exif)
