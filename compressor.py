from PIL import Image
import os

# Set the path to the folder containing the images to be compressed
folder_path = rf"D:\MTS\Datasets\2011_09_26_drive_0009_sync\image_02\ground truth Lidar"

# Set the target size for the compressed images
target_size = (300, 300)

# Loop through all the files in the folder and compress each image
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # Open the image using Pillow
        image = Image.open(os.path.join(folder_path, filename))
        # Resize the image to the target size
        image = image.resize(target_size, Image.ANTIALIAS)
        # Save the compressed image in the same folder with a "_compressed" suffix
        image.save(os.path.join(folder_path, filename.split('.')[0] + '_compressed.png'), optimize=True, quality=50)
