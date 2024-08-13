import matplotlib.pyplot as plt
import os
import cv2

plt.figure(figsize=(15,8))
plt.suptitle("Zooms diferentes para rotações da cabine", fontsize=18, y=0.95)

datadir = 'images\zoom'
category = os.listdir(datadir)

# set number of columns (use 3 to demonstrate the change)
ncols = 5
# calculate number of rows
nrows = len(category) // ncols + (len(category) % ncols > 0)

n = 0

path = os.path.join(datadir,"cabin")

images = list(os.listdir(path))
images = images [:10:]

while n < 10:
    ax = plt.subplot(2, ncols, n+1)
    ax.set_axis_off()
    # ax.set_title(f"{cat}")
    img_array = cv2.imread(os.path.join(path,images[n]))
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    ax.imshow(img_array)
    n+=1


plt.savefig('TCC_Zoom')