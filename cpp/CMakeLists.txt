cmake_minimum_required(VERSION 3.0.0)
project(mba_cv VERSION 0.1.0)

include(CTest)
enable_testing()
set(EXECUTABLE_OUTPUT_PATH build)
find_package( OpenCV REQUIRED )

add_executable(main src/main.cpp)
add_executable(a1d1 src/a1d1.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
include_directories(include)
target_link_libraries( main ${OpenCV_LIBS} )
target_link_libraries( a1d1 ${OpenCV_LIBS} )
