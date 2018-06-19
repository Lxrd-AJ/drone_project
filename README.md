# Notes
* This is a visual SLAM project and not object segmentation 
* 200m

# Drone Video Requirements
- Scene with motion 
- Scene with animals/humans
- Dense vegetation

# TODO
- [x] Draw a bounding box around the matched feature
- [x] Show how the number of matched features decrease with gaussian noise
    * https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv#30609854
- [x] Extract identified region from the scene
- [x] Prepare Promotion materials for the website
    - Join frames as video 'ffmpeg -framerate 25 -i %d.jpg -c:v libx264 -vf "fps=25,format=yuv420p" common_video.mp4'
- [x] Compress and send the region at around (rate 37.5 kbps) [Video/Image transmission/Compression] i.e streaming technologies
    - [x] Image Compression tool
        - https://stackoverflow.com/questions/19153122/image-compression-tools-via-command-line
        - https://www.tecmint.com/optimize-and-compress-jpeg-or-png-batch-images-linux-commandline/
    - [x] Data Transfer tool
        - Lora or 3G
        - See Lora Airtime calculator https://docs.google.com/spreadsheets/d/1QvcKsGeTTPpr9icj4XkKXq4r2zTc2j0gsHLrnplzM3I/edit#gid=0
        - Data rates https://blog.dbrgn.ch/2017/6/23/lorawan-data-rates/
    - https://stackoverflow.com/questions/33027942/opencv-convert-image-to-bytes-and-back
    - Check out Zlib compression http://www.zlib.net/
    - Check out FFMpeg http://ffmpeg.org
    - http://cpham.perso.univ-pau.fr/WSN-MODEL/tool-html/imagesensor.html
- [x] `CV Books <-> Implementation` Image comparison (stored target image vs real-time target image)
    - [x] Gather dataset
    - [ x MSE and Structural Similarity https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
    - [x] Structural Similarity deep dive https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
    - Fourier transforms
    - Difference between histograms
    - Keypoint (SIFT) matching
    - PCA differences
        - try reducing the dimensions and using SSIM on it
- [x] Track moving objects
    - [x] Simple object tracking
        - https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
    - [ ] Optical flow
        - https://docs.opencv.org/3.3.1/d7/d8b/tutorial_py_lucas_kanade.html
    - [ ] Dense optical flow
        - https://docs.opencv.org/3.3.1/d7/d8b/tutorial_py_lucas_kanade.html

# Academic Papers
## Algorithms
* https://infoscience.epfl.ch/record/149300/files/SLIC_Superpixels_TR_2.pdf;
## Neural techniques

# Online Resources
* DSTL Satellite image kaggle https://www.kaggle.com/c/dstl-satellite-imagery-feature-detection/data 
    * currently on https://www.kaggle.com/torrinos/exploration-and-plotting?scriptVersionId=558039
* https://blog.deepsense.ai/deep-learning-for-satellite-imagery-via-image-segmentation/
* https://adeshpande3.github.io/Analyzing-the-Papers-Behind-Facebook's-Computer-Vision-Approach/