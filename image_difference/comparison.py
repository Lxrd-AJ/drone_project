import numpy as np 
import matplotlib.pyplot as plt
import cv2
import imutils
from PIL import Image
from skimage.measure import compare_ssim 

def mean_squared_error(imageA, imageB):
    assert imageA.shape == imageB.shape
    error = np.sum((imageA - imageB) ** 2)
    return error / (imageA.shape[0] * imageA.shape[1])

"""
score, diff
- score is a value between -1 and 1 with 1 being an absolute match
"""
def structural_similarity_index(imageA, imageB):
    assert imageA.shape == imageB.shape
    return compare_ssim(imageA, imageB, full=True)

imageA_ = Image.open('./data/A.jpg')
imageA = imageA_.convert("L")
imageB_ = Image.open('./data/B.jpg')
imageB = imageB_.convert("L")

imageA_ = np.array(imageA_)
imageB_ = np.array(imageB_)
imageA = np.array(imageA)
imageB = np.array(imageB)

mse = mean_squared_error(imageA, imageB)
ss_index,diff = structural_similarity_index(imageA, imageB)
print("MSE = {:}".format(mse))
print("SS Index = {:}".format(ss_index))

diff = (diff * 255).astype("uint8")
cv2.imshow("difference between image A and B", diff)


"""
Threshold the image differences and use that to find contours of the regions
"""
threshold = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU )[1]
cv2.imshow("Thresholded difference", threshold)
contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
contours = contours[0] if imutils.is_cv2() else contours[1]

"""
Drawing rectangles around the different regions 
"""
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(imageA_, (x,y), (x+w,y+h), (0,0,255), 2)
    cv2.rectangle(imageB_, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow("Original target", imageA_)
cv2.imshow("Modified target", imageB_)



cv2.waitKey(0)