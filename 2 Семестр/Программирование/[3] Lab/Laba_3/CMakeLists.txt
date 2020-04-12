cmake_minimum_required(VERSION 3.0)

project(lab_3)

add_executable(lab_3 main.cpp Complex.cpp Complex.h Array.cpp Array.h)

install(TARGETS lab_3 RUNTIME DESTINATION bin)
