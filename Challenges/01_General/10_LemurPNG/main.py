import cv2
import numpy as np

flag = cv2.imread('flag.png')
lemur = cv2.imread('lemur.png')
xored = np.bitwise_xor(flag, lemur)
cv2.imwrite("result.png", xored)
