import numpy as np
from numpy.linalg import inv
import read_depth as rd
import cv2
from threading import Thread
# import pycuda.autoinit
# import pycuda.driver as cuda
# from pycuda.compiler import SourceModule



def fuse_depth_values(z1, z2, x, P, A, B, C, Q, R):
    # Prediction step
    x=A.dot(x) + B.dot(u)
    P=A.dot(P).dot(A.T) + Q
    # Kalman gain
    S=C.dot(P).dot(C.T) + R
    K=P.dot(C.T).dot(inv(S))

    # Update step
    z=np.array([[z1],
                [z2]])
    y=z - C.dot(x)
    x=x + K.dot(y.T)
    P=(np.eye(2) - K.dot(C)).dot(P)

    # Get fused depth estimate
    fused_depth_estimate=x[0, 0]

    # Return fused depth estimate
    return fused_depth_estimate



# System matrices
A=np.array([[1, 0],  # State transition matrix
            [0, 1]])
B=np.array([[0],  # Control matrix
            [0]])
C=np.array([[1, 0]])  # Measurement matrix (only measuring depth)
Q=np.array([[2, 0],  # Process noise covariance (how much do we trust the model)
            [0, 2]])
# Measurement noise covariance (how much do we trust the measurements)
R=np.array([[0.1]])
u=np.array([[0]])  # Control vector

# Initial state and covariance
x=np.array([[0],  # Initial depth estimate
            [0]])
P=np.array([[1, 0],  # ` Initial covariance
            [0, 1]])


def runner(a):
    # Generate some example depth maps
    # Measured depth map from Stereo Camera
    depth_stereo=rd.depth_read(
        rf"D:\MTS\Datasets\2011_09_26_drive_0009_sync\image_02\depth maps generated\{a}_compressed.png")
    # Measured depth map from LIDAR
    depth_lidar=rd.depth_read(
        rf"D:\MTS\Datasets\2011_09_26_drive_0009_sync\image_02\ground truth Lidar\{a}_compressed.png")

    # Create empty depth estimate array
    depth_estimate=np.zeros_like(depth_stereo)

    #Loop through each pixel in the input depth maps and run the EKF algorithm
    # for i in range(depth_stereo.shape[0]):
    #     for j in range(depth_stereo.shape[1]):
    #         depth_estimate[i, j]=fuse_depth_values(
    #             depth_stereo[i, j], depth_lidar[i, j], x, P, A, B, C, Q, R)
    depth_estimate = np.array(list(map(lambda i: list(map(lambda j: fuse_depth_values(depth_stereo[i, j], depth_lidar[i, j], x, P, A, B, C, Q, R), range(depth_stereo.shape[1]))), range(depth_stereo.shape[0]))))
    # Save output image
    depth_uint16=(depth_estimate * 256.0).astype(np.uint16)
    cv2.imwrite(rf"D:\MTS\Datasets\2011_09_26_drive_0009_sync\image_02\Fused depth maps multi\{a}_compressed.png", depth_uint16)

    print(depth_estimate)

threads = [Thread(target=runner, args=(a,)) for a in range(5,8)]

 # start the threads
for thread in threads:
    thread.start()

# wait for the threads to complete
for thread in threads:
    thread.join()

