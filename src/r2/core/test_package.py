import os
from unittest import TestCase

from r2.core.package import Package
from r2.install import Installation

ENDPOINT = "test/endpoint"
ENDPOINT_W_ARG = "test/endpoint?first=asdfgh"
ENDPOINT_W_ARGS = "test/endpoint?first=asdfgh&second=qwerty"

TEST_RESPONSE = {"test": "test_body"}


class TestPackage(TestCase):
    def setUp(self) -> None:
        self.package = Package()

    def test_save(self):
        self.assertTrue(self.package.save(ENDPOINT, TEST_RESPONSE))

    def test_load(self):
        self.package.save(ENDPOINT, TEST_RESPONSE)
        self.assertIsNotNone(self.package.load(ENDPOINT))

    def test_save_arg_endpoint(self):
        self.assertTrue(self.package.save(ENDPOINT_W_ARGS, TEST_RESPONSE))

    def test_load_arg_endpoint(self):
        self.package.save(ENDPOINT_W_ARGS, TEST_RESPONSE)
        self.assertIsNotNone(self.package.load(ENDPOINT_W_ARGS))

    def test__make_args_dict_from_endpoint(self):
        args = self.package._make_args_dict_from_endpoint(ENDPOINT_W_ARGS)

        self.assertIs(len(args), 2, "Should return 2 elements in the dictionary")
        self.assertTrue(isinstance(args, dict), "Return should be a dictionary instance")

    def test__undress_endpoint(self):
        path, filename, args = self.package._undress_endpoint(ENDPOINT_W_ARGS)
        self.assertIsNotNone(path)
        self.assertEqual(filename, "endpoint")
        self.assertTrue(isinstance(args, dict))

    def tearDown(self) -> None:
        test_endpoint_location = os.path.join(*(Installation.DOWNLOAD_DIR, "default", "test", "endpoint"))
        if os.path.exists(test_endpoint_location):
            os.remove(test_endpoint_location)
        if os.path.isdir(os.path.join(*(Installation.DOWNLOAD_DIR, "default", "test"))):
            os.rmdir(os.path.join(*(Installation.DOWNLOAD_DIR, "default", "test")))
