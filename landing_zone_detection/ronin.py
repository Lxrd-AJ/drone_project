import numpy as np 
import cv2 
from matplotlib import pyplot as plt


def match( desc1, desc2, matcher ):
    matches = matcher.knnMatch( desc1, desc2, k=2 )
    good = []
    for m, n in matches:
        # print("m distance = {:} and n distance = {:}".format(m.distance,n.distance))
        if m.distance < 0.70 * n.distance:
            good.append([m])
    return good 

def drawBoundingBoxInto( sceneImage, queryImage, queryKP, sceneKP, matches ):
    good = matches
    print("{:} matches made ".format(len(good)))
    if len(good) > 15:
        print("Match found [x]")
        src_pts = np.float32([ queryKP[m[0].queryIdx].pt for m in good]).reshape(-1,1,2)
        dst_pts = np.float32([ sceneKP[m[0].trainIdx].pt for m in good]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        h,w = queryImage.shape 
        pts = np.float32([ [0,0], [0,h-1], [w-1,h-1], [w-1,0]]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts, M)

        sceneImage = cv2.polylines( sceneImage, [np.int32(dst)], True, (200,50,50), 2, cv2.LINE_AA)
        return sceneImage
    else:
        print("No match found .....")
        return sceneImage


sift = cv2.xfeatures2d.SIFT_create()
bruteForce = cv2.BFMatcher()

queryImage = cv2.imread("./real_target_common.png",0)
queryKP, queryDesc = sift.detectAndCompute(queryImage, None)


capture = cv2.VideoCapture("./short_real_drone_feed.mp4") # real_drone_feed.mp4
frame_count = 0


# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# out = None

cv2.namedWindow('main', cv2.WINDOW_NORMAL)
while capture.isOpened(): 
    frame_count += 1
    print("Frame count = " + str(frame_count))
    
    ret, frame_c = capture.read()
    frame = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (1000,600))
    frame_c = cv2.resize(frame_c, (1000,600))

    # if frame_count % 12 == 0:
    sceneKP, sceneDesc = sift.detectAndCompute(frame, None)
    matches = match( queryDesc, sceneDesc, bruteForce )
    
    frame_c =  drawBoundingBoxInto( frame_c, queryImage, queryKP, sceneKP, matches )
    cv2.imshow('main', frame_c)
    # if out is None:
    #     out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1000,600), False)
    # out.write(frame)
    
    cv2.imwrite("./Promo/frames_color/{:}.jpg".format(frame_count), frame_c)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# out.release()
capture.release()
cv2.destroyAllWindows()


# sift = cv2.xfeatures2d.SIFT_create()
#     kp = sift.detect(frame,None)
#     outimg = np.copy(frame)
#     outimg = cv2.drawKeypoints(frame,kp,outimg,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     cv2.imshow('main',outimg)
#     frame_count += 1
#     print("Frame count {:} with shape {:}".format(frame_count,frame.shape))