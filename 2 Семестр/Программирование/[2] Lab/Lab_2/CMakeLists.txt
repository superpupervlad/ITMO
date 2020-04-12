cmake_minimum_required(VERSION 3.0)

project(lab_2)

add_executable(lab_2 main.cpp Complex.cpp Complex.h)

install(TARGETS lab_2 RUNTIME DESTINATION bin)
