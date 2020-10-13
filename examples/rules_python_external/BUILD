load("@pip//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_test")
load("@rules_proto//proto:defs.bzl", "proto_library")
load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        ":sample_py_proto",
        requirement("boto3"),
        requirement("six"),
    ],
)

py_test(
    name = "test",
    srcs = ["test.py"],
    deps = [":main"],
)

proto_library(
    name = "sample_proto",
    srcs = ["sample.proto"],
)

py_proto_library(
    name = "sample_py_proto",
    deps = [":sample_proto"],
)
