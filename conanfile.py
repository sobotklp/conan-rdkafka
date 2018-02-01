from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class RabbitMQConan(ConanFile):
    name = "rdkafka"
    version_info = (0, 8, 6)
    version = ".".join(map(str, version_info))
    license = "MIT"
    description = "librdkafka is a C library implementation of the Apache Kafka protocol"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    exports = "FindRdkafka.cmake"
    default_options = "shared=True"
    requires = ("OpenSSL/1.0.2k@lasote/stable", ("zlib/1.2.11@lasote/stable", "override"))
    unzipped_name = "librdkafka-%s" % version

    @property
    def zip_name(self):
        if self.version_info > (0, 9, 1):
            return "v%s.tar.gz" % self.version
        else:
            return "%s.tar.gz" % self.version

    def source(self):
        url = "https://github.com/edenhill/librdkafka/archive/%s" % (self.zip_name)
        self.output.info("Downloading %s..." % url)

        tools.download(url, self.zip_name)
        tools.unzip(self.zip_name)
        os.unlink(self.zip_name)


    @property
    def subfolder(self):
        return self.unzipped_name


    def build(self):
        with tools.chdir(self.subfolder):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.configure()
            self.run("make")  # Run make manually so AutoToolsBuildEnvironment doesn't pass the -j parameter. That breaks the build


    def package(self):
        self.copy("*.h", dst="include", src="%s/src" % self.subfolder)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", src="%s/src" % self.subfolder, keep_path=False)

        # Copy cmake find_package script into project
        self.copy("FindRdkafka.cmake", ".", ".")

        # Copying debug symbols
        if self.settings.compiler == "Visual Studio" and self.options.include_pdbs:
            self.copy(pattern="*.pdb", dst="lib", src=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rdkafka"]
