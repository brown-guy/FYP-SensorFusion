import os# set the directory where the files are located
directory = r"D:\MTS\Datasets\2011_09_28_drive_0070_sync\image_03\data"# loop through each file in the directory
for filename in os.listdir(directory):
# check if the filename starts with "000000000"
    if filename.startswith("00000000"):
    # get the number from the filename by removing the leading zeros
        number = filename.lstrip("0")
        # construct the new filename by adding the directory path and the number
        new_filename = os.path.join(directory, f"{number}")
        # rename the file
        os.rename(os.path.join(directory, filename), new_filename)