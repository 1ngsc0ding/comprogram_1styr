# Calculate split dataset to tune hyperparameters of a model

# Acquire user input for total images
total_images = int(input("Enter total images: "))

train = int(total_images * 70 / 100) # Calculate number of training images
validation = int(total_images * 15 / 100) # Calculate number of validation images
test = int(total_images * 15 / 100) # Calculate number of test images

print("Training images:", str(train) + " images") # Display number of training images
print("Validation images:", str(validation) + " images") # Display number of validation images
print("Testing images:", str(test) + " images") # Display number of test images