cmake_minimum_required(VERSION 3.0)

project(lab_8)

add_executable(lab_8 main.cpp Kubik.h Kubik.cpp)

install(TARGETS lab_8 RUNTIME DESTINATION bin)
