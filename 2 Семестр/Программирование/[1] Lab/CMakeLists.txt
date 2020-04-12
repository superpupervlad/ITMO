cmake_minimum_required(VERSION 3.0)
project(programming)

add_executable(programming main.cpp functions.cpp functions.h)

install(TARGETS programming RUNTIME DESTINATION bin)
