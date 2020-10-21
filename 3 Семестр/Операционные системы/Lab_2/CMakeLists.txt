cmake_minimum_required(VERSION 3.18)
project(Lab_2_1)

set(CMAKE_CXX_STANDARD 17)

set(SERVER_FILES server_main.cpp err_handle.h err_handle.cpp codes.cpp codes.h server_processes.h server_processes.cpp unilib.cpp unilib.h)
set(CLIENT_FILES client_main.cpp err_handle.h err_handle.cpp codes.cpp codes.h client_processes.cpp client_processes.h unilib.cpp unilib.h)

add_executable(server ${SERVER_FILES})
add_executable(client ${CLIENT_FILES})