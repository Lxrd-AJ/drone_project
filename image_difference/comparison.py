import numpy as np 
from PIL import Image 

def mean_squared_error(imageA, imageB):
    assert imageA.shape == imageB.shape
    error = np.sum((imageA - imageB) ** 2)
    return error / (imageA.shape[0] * imageA.shape[1])

imageA = Image.open('./data/A.jpg').convert("L")
imageB = Image.open('./data/B.jpg').convert("L")

imageA = np.array(imageA)
imageB = np.array(imageB)

mse = mean_squared_error(imageA, imageB)
print("MSE = {:}".format(mse))