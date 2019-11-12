import os
import random
import math
import shutil
import time

files = []
train_perc = 75 #percent

assert train_perc < 100 and train_perc > 0, "Train percentage out of bounds"

for file in os.listdir("Images/"):
	files.append(file)

train = (int)(math.ceil((len(files)*train_perc)/100))


#loop through to get random training images
for i in range(0, train):
	training_example = random.choice(files)
	print(training_example, ", train")
	shutil.copy(os.path.join("Images", training_example), "train")
	time.sleep(0.5)
	files.remove(training_example)

#go through rest to get the testing examples
for item in files:
	print(item, ", test")
	shutil.copy(os.path.join("Images", item), "test")
	time.sleep(0.5)
