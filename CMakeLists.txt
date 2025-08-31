cmake_minimum_required(VERSION 3.14)
project(BuildOnline VERSION 1.0.0)
set(CMAKE_CXX_STANDARD 17)

add_executable(app_hello src/main.cpp)

# 使用CPack打包
include(InstallRequiredSystemLibraries)
set(CPACK_GENERATOR "ZIP")
set(CPACK_PACKAGE_FILE_NAME "app_hello-${CMAKE_PROJECT_VERSION}-win64")
include(CPack)

# cd build
# cpack -G ZIP