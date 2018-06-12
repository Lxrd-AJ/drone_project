# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html

import numpy as np 
import cv2 
from matplotlib import pyplot as plt
from pprint import pprint

cv2.ocl.setUseOpenCL(False)

queryImage = cv2.imread("./target_landing_2.png",0) #  real_target_common.png
sceneImage = cv2.imread("./landing_scene_2.png",0) #  ./landing_scene_common.png

# Using the ORB Feature extractor
# orb = cv2.ORB_create()
# queryKP, queryDesc = orb.detectAndCompute( queryImage, None )
# sceneKP, sceneDesc = orb.detectAndCompute( sceneImage, None )

# # Brute-Force Matcher
# bruteForce = cv2.BFMatcher( cv2.NORM_HAMMING, crossCheck=True ) 
# matches = bruteForce.match( queryDesc, sceneDesc )
# matches = sorted( matches, key=lambda x: x.distance)

# matchedImage = np.copy(queryImage)
# matchedImage = cv2.drawMatches( queryImage,queryKP, sceneImage,sceneKP, matches[:], matchedImage, flags=2)

# plt.figure(1)
# plt.imshow(matchedImage)


#SIFT Matching
matchedImage = np.copy(queryImage)
sift = cv2.xfeatures2d.SIFT_create()
queryKP_sift, queryDesc_sift = sift.detectAndCompute(queryImage, None)
sceneKP_sift, sceneDesc_sift = sift.detectAndCompute(sceneImage, None)
bruteForce = cv2.BFMatcher()
matches = bruteForce.knnMatch( queryDesc_sift, sceneDesc_sift, k=2 )
# matches = sorted( matches, key=lambda x: x.distance)
good = [] # Good ratio test
for m,n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])
matchedImage = cv2.drawMatchesKnn( queryImage,queryKP_sift,sceneImage,sceneKP_sift, good[:200], matchedImage, flags=2)
"""
Visualisations
====
plt.figure(2)
plt.imshow(matchedImage)
plt.show()
cv2.imwrite('./Promo/lagos_sift_matching.jpg', matchedImage)
# Draw SIFT Keypoints in the target scene
x = np.copy(sceneImage)
x = cv2.drawKeypoints( sceneImage, sceneKP_sift, x, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.figure(1)
plt.imshow(x)
plt.show()
cv2.imwrite('./Promo/sift_keypoints_lagos.jpg',x)
"""

# Boundary Box
MIN_MATCH_COUNT = 10
if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([ queryKP_sift[m[0].queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.float32([ sceneKP_sift[m[0].trainIdx].pt for m in good]).reshape(-1,1,2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()

    h,w = queryImage.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    startPt = np.int32(dst[0][0])
    croppedOutTarget = sceneImage[startPt[1]:startPt[1]+h,startPt[0]:startPt[0]+w]

    """
    Extracting image of the boundary box
    ===
    plt.figure(10)
    plt.imshow(croppedOutTarget)
    plt.show()
    """

    """
    Compression/Decompression section
    
    rt_val, buf = cv2.imencode(".png", croppedOutTarget, [cv2.IMWRITE_JPEG_QUALITY,1])
    print(len(buf))
    scene_buff = sceneImage.getbuffer() #np.getbuffer( sceneImage )
    print(scene_buff)
    """
    resImage = np.copy(sceneImage)
    resImage = cv2.polylines(resImage,[np.int32(dst)],True,(255,100,50),3, cv2.LINE_AA)
    plt.figure(4)
    plt.imshow(resImage)
    plt.show()
    cv2.imwrite("./Promo/lagos_bounding_box.jpg", resImage)
else:
    print("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
    matchesMask = None
# draw_params = dict(matchColor = (0,255,0), singlePointColor = None, matchesMask = matchesMask, flags = 2)
# matchedImage = cv2.drawMatches( queryImage, queryKP_sift, sceneImage, sceneKP_sift, good, None, **draw_params)
# plt.figure(3)
# plt.imshow(matchedImage)
# plt.show()




"""
- TODO: Plot a graph of how the number of matched features `good` changes with increase in variance of gaussian noise

matchedImage = np.copy(queryImage)
sift = cv2.xfeatures2d.SIFT_create()
queryKP_sift, queryDesc_sift = sift.detectAndCompute(queryImage, None)

mean = 0
length = sceneImage.shape[0] * sceneImage.shape[1]
strength = []
for variance in np.linspace(0.1,200,200):
    gaussian_noise = np.random.normal(mean, variance, length )
    gaussian_noise = np.reshape(gaussian_noise,sceneImage.shape)

    noisyImage = sceneImage + np.round(gaussian_noise).astype(np.uint8)
    noisykp_sift, noisy_sift = sift.detectAndCompute(sceneImage, None)
    bruteForce = cv2.BFMatcher()
    matches = bruteForce.knnMatch( queryDesc_sift, noisy_sift, k=2 )
    good = [] # Good ratio test
    for m,n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
    strength.append(len(good))
    print("Variance = {:}, Num matches = {:}".format(variance, len(good)))

plt.figure(4)
plt.imshow(sceneImage)
plt.figure(5)
plt.imshow(noisyImage)

matchedImage = np.copy(queryImage)
matchedImage = cv2.drawMatchesKnn( queryImage,queryKP_sift, noisyImage,noisykp_sift, good, matchedImage, flags=2)
plt.figure(6)
plt.imshow(matchedImage)
plt.figure(7)
plt.plot(strength)
plt.xlabel("Gaussian variance")
plt.ylabel("Num Matches")
plt.savefig("./good2noise.png")
plt.show()
"""
