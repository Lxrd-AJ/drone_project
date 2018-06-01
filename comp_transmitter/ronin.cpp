#include <iostream>
#include <stdio.h>
#include <string>
#include <opencv2/opencv.hpp>

using namespace std;

/*
 * Convert image to bytes
 *
byte* matrixToBytes(cv::Mat image){
  int size = image.total() * image.elemSize();
  byte* bytes = new byte[size];
  std::memcpy(bytes, image.data, size * sizeof(byte));
  return bytes;
}

cv::Mat bytesToMatrix(byte* bytes, int width, int height){
  cv::Mat image = cv::Mat(height,width,cv::CV_8UC3,bytes).clone();
  return image;
}
*/

int main(int argc, char **argv){
    std::string filename = argv[1];
    cout << "Input image " << filename << " len args = " << argc << endl;

    cv::Mat image = cv::imread(filename);

    std::vector<uchar> buffer;
    std::vector<int> compression_params = std::vector<int>();

    bool result = cv::imencode(".bmp", image, buffer, compression_params);
    cout << result << endl;
    cout << buffer.size() * sizeof(uchar) << " bytes"  << endl;

    cout << "Converting the image back to a matrix" << endl;
    cv::Mat cImage = cv::imdecode( buffer, 1 );
    cout << image << endl;

    return 0;
}
