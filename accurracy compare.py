import numpy as np
import cv2
import read_depth as rd
import pandas as pd

# Initialize an empty array to store the results
results = []

# Load in the depth map and ground truth data
for a in range (5,99):
    depth_map = rd.depth_read(rf"D:\dataspell project\FinalYearProject\FinalYearProject\2011_09_26_drive_0001_syncimage_02\depth maps generated\{a}.png")
    gt_data =  rd.depth_read(rf"D:\dataspell project\FinalYearProject\FinalYearProject\2011_09_26_drive_0001_syncimage_02\groundtruth\{a}.png")
    print(depth_map.shape)
    # Compare the depth map to the ground truth data
    error = np.abs(depth_map - gt_data)
    mean_error = np.mean(error)

    print("Mean error:", mean_error)

    # Calculate the percentage of pixels within a certain tolerance
    tolerance = 0.1 # 10% tolerance
    num_pixels = depth_map.shape[0] * depth_map.shape[1]
    accurate_pixels = np.sum(error < tolerance)
    accuracy = accurate_pixels / num_pixels

    print("Accuracy within tolerance:", accuracy)