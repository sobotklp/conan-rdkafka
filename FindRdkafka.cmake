# Try to find librdkafka
# Once done, this will define
#
# LIBRDKAFKA_FOUND        - system has LIBRDKAFKA
# LIBRDKAFKA_INCLUDE_DIRS - LIBSJON include directories
# LIBRDKAFKA_LIBRARIES    - libraries need to use GFLAGS

find_path(
        LIBRDKAFKA_INCLUDE_DIR
        NAMES rdkafka.h
        PATHS ${CONAN_INCLUDE_DIRS_LIBRDKAFKA}
)

find_library(
        LIBRDKAFKA_LIBRARY
        NAMES rdkafka
        PATHS ${CONAN_LIB_DIRS_LIBRDKAFKA}
)

set(LIBRDKAFKA_FOUND TRUE)
set(LIBRDKAFKA_INCLUDE_DIRS ${LIBRDKAFKA_INCLUDE_DIR})
set(LIBRDKAFKA_LIBRARIES ${LIBRDKAFKA_LIBRARY})

mark_as_advanced(LIBRDKAFKA_LIBRARY LIBRDKAFKA_INCLUDE_DIR)
