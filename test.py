import cv2
import os

# Set the paths to the two directories containing the images
image02_path = 'D:\MTS\Datasets\2011_09_26_drive_0011_sync\image_02\data'
image03_path = 'D:\MTS\Datasets\2011_09_26_drive_0011_sync\image_03\data'

# Set the path to the directory where you want to save the output images
output_dir_path = 'D:\MTS\Datasets\2011_09_26_drive_0011_sync\image_02\depth maps generated'

# Get a list of all the files in the first directory
image02_files = os.listdir(image02_path)

# Loop through each file in the first directory
for filename in image02_files:
    # Set the path to the corresponding file in the second directory
    image03_filename = filename  # You may need to modify this depending on the naming convention of your files
    image03_filepath = os.path.join(image03_path, image03_filename)

    # Read in the images from the two directories
    image02_filepath = os.path.join(image02_path, filename)
    image02_img = cv2.imread(image02_filepath)
    image03_img = cv2.imread(image03_filepath)

    # Compare the two images
    # Example code to compare images
    
    # Write the output image to the third directory
    output_filepath = os.path.join(output_dir_path, filename)
    cv2.imwrite(output_filepath, diff)
