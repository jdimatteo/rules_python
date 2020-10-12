import unittest
import main

class ExampleTest(unittest.TestCase):
    def test_main(self):
        self.assertIn("set_stream_logger", main.the_dir())

    def test_boto3_version(self):
        self.assertEqual("1.14.51", main.boto3_version())

    def test_six_version(self):
        self.assertEqual("1.15.0", main.six_version())

if __name__ == '__main__':
  unittest.main()
