cmake_minimum_required(VERSION 3.0)

project(lab_4)

add_executable(lab_4 main.cpp GeomObjects.cpp GeomObjects.h)

install(TARGETS lab_4 RUNTIME DESTINATION bin)
