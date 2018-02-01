# conan-librdkafka

[Conan.io](https://conan.io) package for [librdkafka C/C++ library](https://github.com/edenhill/librdkafka)

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload rdkafka/0.8.6@sobotklp/stable -r <remote> --all

## Reuse the packages

### Basic setup

    $ conan install rdkafka/0.8.6@sobotklp/stable

### Project setup

If you handle multiple dependencies in your project, it would be better to add a *conanfile.txt*

    [requires]
    rdkafka/0.8.6@sobotklp/stable

    [generators]
    txt
    cmake


## TODO

* Update this package to support later versions of librdkafka
* Test on Linux and Windows
