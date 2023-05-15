"""
import numpy as np
import cv2
import read_depth as rd

# Load in the depth map and ground truth data
depth_map = rd.depth_read(r"D:\dataspell project\FinalYearProject\FinalYearProject\2011_09_26_drive_0001_syncimage_02\depth maps generated\0000000005.png")
gt_data =  rd.depth_read(r"D:\dataspell project\FinalYearProject\FinalYearProject\2011_09_26_drive_0001_syncimage_02\groundtruth\0000000005.png")
fused_map=rd.depth_read(r"D:\dataspell project\FinalYearProject\FinalYearProject\2011_09_26_drive_0001_syncimage_02\Fused depth maps\0000000005.png")
print(depth_map.shape)
# Compare the depth map to the ground truth data
error1 = np.abs(depth_map - gt_data)
mean_error1 = np.mean(error1)

print("Mean error of depth map:", mean_error1)
# Compare the fused map to the ground truth data

error2= np.abs(fused_map-gt_data)
mean_error2=np.mean(error2)
print("Mean error of Fused depth map:", mean_error2)

# Calculate the percentage of pixels within a certain tolerance
tolerance = 0.1 # 10% tolerance
num_pixels = depth_map.shape[0] * depth_map.shape[1]
accurate_pixels = np.sum(error1 < tolerance)
accuracy = accurate_pixels / num_pixels

print("Accuracy within tolerance for depth map:", accuracy)

# Calculate the percentage of pixels within a certain tolerance
tolerance = 0.1 # 10% tolerance
num_pixels = depth_map.shape[0] * depth_map.shape[1]
accurate_pixels = np.sum(error2 < tolerance)
accuracy = accurate_pixels / num_pixels

print("Accuracy within tolerance for fused map:", accuracy)
"""
# this code is for comparing the accuracy of the depth map and fused depth map with the ground truth data
# and this only considers the valid values of ground truth to compare the error to
import numpy as np
import cv2
import read_depth as rd
import pandas as pd

# Initialize an empty array to store the results
stereo_error = []
fused_error=[]


# Load in the depth map and ground truth data
for a in range(5,6):
    depth_map = rd.depth_read(rf"D:\MTS\Datasets\2011_09_28_drive_0070_sync\image_02\depth maps generated\{a}.png")
    gt_data =  rd.depth_read(rf"D:\MTS\Datasets\2011_09_28_drive_0070_sync\image_02\ground truth stereo\{a}.png")
    fused_map=rd.depth_read(rf"D:\MTS\Datasets\2011_09_28_drive_0070_sync\image_02\test\{a}.png")
    print(depth_map.shape)
    nonzero_indices = np.where(gt_data != 0)
    error1 = np.abs(depth_map[nonzero_indices] - gt_data[nonzero_indices])
    mean_error1 = np.mean(error1)
    print("Mean error of depth map:", mean_error1)
    stereo_error.append(mean_error1)

    nonzero_indices = np.where(gt_data != 0)
    error2 = np.abs(fused_map[nonzero_indices] - gt_data[nonzero_indices])
    mean_error2 = np.mean(error2)
    print("Mean error of fused map:", mean_error2)
    fused_error.append(mean_error2)

print("error0")
df = pd.DataFrame({'Stereo Error': stereo_error,'Fused Error': fused_error})

# Save the DataFrame to an Excel file

filename = '2011_09_28_drive_0070_sync.xlsx'
print("error1")
df.to_excel(filename, index=False)

"""1.051200209920971
tolerance = 0.1 # 10% tolerance
num_pixels = depth_map.shape[0] * depth_map.shape[1]
accurate_pixels = np.sum(error1[nonzero_indices] < tolerance)
accuracy = accurate_pixels / num_pixels

print("Accuracy within tolerance for depth map:", accuracy)

# Calculate the percentage of pixels within a certain tolerance
tolerance = 0.1 # 10% tolerance
num_pixels = depth_map.shape[0] * depth_map.shape[1]
accurate_pixels = np.sum(error2[nonzero_indices] < tolerance)
accuracy = accurate_pixels / num_pixels

print("Accuracy within tolerance for fused map:", accuracy)

"""