cmake_minimum_required(VERSION 2.8)
project( Ronin )
# find_package( OpenCV REQUIRED PATHS /usr/local/Cellar/opencv/3.4.1_2)
set(CMAKE_CXX_STANDARD 11)
SET(OpenCV_DIR "/usr/local/Cellar/opencv/3.4.1_2/")
SET(OpenCV_INCLUDE_DIR "/usr/local/Cellar/opencv/3.4.1_2/include/")
SET(OpenCV_LIBRARIES "/usr/local/Cellar/opencv/3.4.1_2/lib/")

include_directories( ${OpenCV_INCLUDE_DIR} )

# get_cmake_property(_variableNames VARIABLES)
# list (SORT _variableNames)
# foreach (_variableName ${_variableNames})
#     message(STATUS "${_variableName}=${${_variableName}}")
# endforeach()

SET( SOURCE_FILES ronin.cpp)
add_executable( Ronin ${SOURCE_FILES} )
# target_link_libraries( Ronin ${OpenCV_LIBRARIES} )