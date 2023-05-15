#!/usr/bin/python

from PIL import Image
import numpy as np
import cv2


def depth_read(filename):
    # loads depth map D from png file
    # and returns it as a numpy array,
    # for details see readme.txt

    depth_png = np.array(Image.open(filename), dtype=int)
    # make sure we have a proper 16bit depth map here.. not 8bit!
    assert(np.max(depth_png) > 255)

    depth = depth_png.astype(float) / 256.
  
    return depth


#a=depth_read(r'D:\MTS\Datasets\2011_09_26_drive_0011_sync\image_02\depth maps generated\0000000005.png')
#a=a*256
def save_depth_map(save_path, depth_map,
                   version='cv2', png_compression=3):
    """Saves depth map to disk as uint16 png

    Args:
        save_path: path to save depth map
        depth_map: depth map numpy array [h w]
        version: 'cv2' or 'pypng'
        png_compression: Only when version is 'cv2', sets png compression level.
            A lower value is faster with larger output,
            a higher value is slower with smaller output.
    """

    # Convert depth map to a uint16 png
    depth_image = (depth_map * 256.0).astype(np.uint16)

    if version == 'cv2':
        cv2.imwrite(save_path, depth_image)



    else:
        raise ValueError('Invalid version', version)