# Notes
* This is a visual SLAM project and not object segmentation 
* 200m

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
    - [ ] Data Transfer tool
        - Lora or 3G
        - See Lora Airtime calculator https://docs.google.com/spreadsheets/d/1QvcKsGeTTPpr9icj4XkKXq4r2zTc2j0gsHLrnplzM3I/edit#gid=0
    - https://stackoverflow.com/questions/33027942/opencv-convert-image-to-bytes-and-back
    - Check out Zlib compression http://www.zlib.net/
    - Check out FFMpeg http://ffmpeg.org
    - http://cpham.perso.univ-pau.fr/WSN-MODEL/tool-html/imagesensor.html
- [ ] Anomaly detecion
- [ ] (Optional) Electron GUI app version 
    - [ ] ReactJS tutorial https://reactjs.org/tutorial/tutorial.html
    - [ ] React Router setup https://reacttraining.com/react-router/web/guides/quick-start
    - [ ] React Proton Native https://proton-native.js.org/#/?id=proton-native 

# Academic Papers
## Algorithms
* https://infoscience.epfl.ch/record/149300/files/SLIC_Superpixels_TR_2.pdf;
## Neural techniques

# Online Resources
* DSTL Satellite image kaggle https://www.kaggle.com/c/dstl-satellite-imagery-feature-detection/data 
    * currently on https://www.kaggle.com/torrinos/exploration-and-plotting?scriptVersionId=558039
* https://blog.deepsense.ai/deep-learning-for-satellite-imagery-via-image-segmentation/
* https://adeshpande3.github.io/Analyzing-the-Papers-Behind-Facebook's-Computer-Vision-Approach/