# This script uses the glob.glob() function to get a list of all the files in the specified folder. 
# It then uses the os.path.basename() function to extract the key from the filename, 
# and uses a dictionary to store the key ranges. Finally, it returns the key ranges.

import os
import glob
import zipfile

def distribute_load(folder):
    # Get a list of all the files in the folder
    files = glob.glob(folder + "/*")

    # Create a dictionary to store the key ranges
    key_ranges = {}

    # Loop through the files and extract the key from the filename
    for file in files:
        # Extract the key from the filename
        key = os.path.basename(file)[:-4]

        # Check if the key exists in the dictionary
        if key in key_ranges:
            # If it does, add the file to the corresponding key range
            key_ranges[key].append(file)
        else:
            # If it doesn't, create a new key range and add the file to it
            key_ranges[key] = [file]

    # Return the key ranges
    return key_ranges

# Test the function
key_ranges = distribute_load("data/large_folder")
print(key_ranges)
