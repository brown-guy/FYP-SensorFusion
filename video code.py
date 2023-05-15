import cv2
import os

# Define the path to the images and the output video
images_path = r'D:\MTS\Datasets\2011_09_26_drive_0015_sync\image_02\data'
output_video = r'\output.mp4'

# Get the list of images
images = [f for f in os.listdir(images_path) if f.endswith('.png')]
images.sort()

# Get the dimensions of the first image
img = cv2.imread(os.path.join(images_path, images[0]))
height, width, channels = img.shape
print(height,width)
# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(images_path+output_video, fourcc, 1, (width, height))

# Loop through the images and write them to the video
for image in images:
    img = cv2.imread(os.path.join(images_path, image))
    img=  cv2.applyColorMap(img, cv2.COLORMAP_JET)
    out.write(img)

# Release the VideoWriter and destroy all windows
out.release()
cv2.destroyAllWindows()
