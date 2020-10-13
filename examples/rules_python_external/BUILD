load("@rules_python//python:defs.bzl", "py_binary", "py_test")
load("@rules_proto//proto:defs.bzl", "proto_library")
load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        ":sample_py_proto",
    ],
)

proto_library(
    name = "sample_proto",
)

py_proto_library(
    name = "sample_py_proto",
    deps = [":sample_proto"],
    srcs = ["sample.proto"],
)
