cmake_minimum_required(VERSION 3.0)

project(lab_7)

add_executable(lab_7 main.cpp circular_buffer.cpp circular_buffer.h)

install(TARGETS lab_7 RUNTIME DESTINATION bin)
