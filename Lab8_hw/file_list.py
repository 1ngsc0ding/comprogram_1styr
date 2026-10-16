# Write program to show list of files in a given directory
# - show total file size
# - change to list only image files (.jpg, .gif, .png ?)
# then show total size of image files

import os

directory = input("Enter directory: ")

total_size = 0
image_size = 0

for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        size = os.path.getsize(path)
        total_size += size
        print(filename, size, "bytes")

        if filename.lower().endswith((".jpg", ".gif", ".png")):
            image_size += size

print("Total file size:", total_size, "bytes")
print("Total image size:", image_size, "bytes")
