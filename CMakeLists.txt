cmake_minimum_required(VERSION 3.9)
project(notes_pdf_samplers_MDGFRD)

set(CMAKE_C_STANDARD 11)

add_executable(main
        generate_data.c
        greensFunct.h
        draw.h
        make_data_fig1.h make_data_fig2.h make_data_convexPall.h make_data_convexS.h make_data_convexP.h make_data_fig6.h make_data_fig7.h)

find_package(GSL REQUIRED)
target_link_libraries(main GSL::gsl GSL::gslcblas)

set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
