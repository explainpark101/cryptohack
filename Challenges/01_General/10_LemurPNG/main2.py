from PIL import Image, ImageChops
import numpy as np

lemur = Image.open("lemur.png")
flag = Image.open("flag.png")

lemur = np.asarray(lemur)
flag = np.asarray(flag)

key = np.bitwise_xor(lemur, flag)

Image.fromarray(key).show()