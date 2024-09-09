import cv2, os, sys
import numpy as np
import matplotlib.pyplot as plt

def base_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

img = cv2.imread(f"{base_path()}/gato.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("image", img)
# rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(rgb_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.waitforbuttonpress()
# plt.close('all')