from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
image = Image.open(r'/Users/soapedya/Github/2025_research/Healthy_test_case.png')
pixels = np.asarray(image)
reds = pixels[:, :, 0]
greens = pixels[:, :, 1]
blues = pixels[:, :, 2]


imgplot = plt.imshow(blues, cmap='Blues')
plt.show()
