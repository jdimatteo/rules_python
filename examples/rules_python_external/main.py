import six
import boto3

def the_dir():
    return dir(boto3)

def boto3_version():
    return boto3.__version__

def six_version():
    return six.__version__

if __name__ == "__main__":
    print(the_dir())
